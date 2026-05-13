from datetime import datetime, timedelta
from collections import defaultdict
from typing import List, Dict, Any
from ..state import AgentState
from ..config import get_llm
from ..tools.detection_tools import pattern_detector_tool, anomaly_detector_tool, threat_lookup_tool
from langgraph.prebuilt import create_react_agent

FMT = "%Y-%m-%d %H:%M:%S"

def parse_ts(ts: str) -> datetime:
    # tolerate both " " and "T"
    ts = ts.replace("T", " ")
    return datetime.strptime(ts.split(".")[0], FMT)

def detect_anomalies(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    anomalies = []
    # Rule A: Brute-force burst: >=5 fails same user+ip in 10 minutes, then success
    fails_by_key = defaultdict(list)
    for e in events:
        if e["event_type"] == "login" and e["status"] == "fail":
            key = (e["user"], e["source_ip"])
            fails_by_key[key].append(parse_ts(e["timestamp"]))
    for (user, ip), times in fails_by_key.items():
        times.sort()
        burst = [t for t in times if (times[-1] - t) <= timedelta(minutes=10)]
        if len(burst) >= 5:
            anomalies.append({"rule": "brute_force_burst", "user": user, "ip": ip, "count": len(burst)})
    # Rule B: Success from foreign after burst (simple: success from different country than 'US' within 30 min of last fail)
    last_fail = {}
    for e in events:
        if e["event_type"] == "login" and e["status"] == "fail":
            last_fail[e["user"]] = parse_ts(e["timestamp"])
        if e["event_type"] == "login" and e["status"] == "success":
            t = parse_ts(e["timestamp"])
            lf = last_fail.get(e["user"])
            if lf and (t - lf) <= timedelta(minutes=30) and e.get("country") not in ("US","CA"):
                anomalies.append({"rule": "suspicious_geo_success", "user": e["user"], "ip": e["source_ip"], "country": e.get("country","?")})
    # Rule C: Large off-hours download (00:00–05:00) with bytes > 1e6
    for e in events:
        if e["event_type"] == "data_download":
            t = parse_ts(e["timestamp"])
            if t.hour < 5 and int(e.get("bytes",0)) >= 1_000_000:
                anomalies.append({"rule": "offhours_large_download", "user": e["user"], "ip": e["source_ip"], "bytes": int(e.get("bytes",0))})
    # Rule D: Privilege escalation
    for e in events:
        if e["event_type"] == "sudo":
            anomalies.append({"rule": "privilege_escalation", "user": e["user"], "ip": e["source_ip"], "message": e.get("message","")})
    return anomalies

def detect_node(state: AgentState) -> AgentState:
    events = state.get("events", [])
    
    # Try to use LangGraph's built-in ReAct agent
    llm = get_llm()
    if llm:
        try:
            # Create ReAct agent with detection tools
            react_agent = create_react_agent(
                model=llm,
                tools=[pattern_detector_tool, anomaly_detector_tool, threat_lookup_tool],
                prompt="You are a security threat detection specialist. Analyze security events for threats and anomalies."
            )
            
            # Run the ReAct agent
            response = react_agent.invoke({
                "messages": [{
                    "role": "user",
                    "content": f"Investigate these security events for threats and anomalies: {len(events)} events found"
                }]
            })
            
            # Use tools to detect patterns and anomalies
            patterns = pattern_detector_tool.invoke({"events": events})
            anomalies = anomaly_detector_tool.invoke({"events": events})
            
            # Combine results
            all_anomalies = []
            
            # Add pattern-based detections
            for pattern in patterns:
                all_anomalies.append({
                    "rule": pattern.get("pattern"),
                    "user": pattern.get("user"),
                    "ip": pattern.get("ip"),
                    "confidence": pattern.get("confidence", 0.5),
                    "source": "pattern_detection"
                })
            
            # Add anomaly-based detections
            for anomaly in anomalies:
                all_anomalies.append({
                    "rule": anomaly.get("anomaly"),
                    "user": anomaly.get("user"),
                    "ip": anomaly.get("ip"),
                    "confidence": anomaly.get("confidence", 0.5),
                    "source": "anomaly_detection"
                })
            
            # Add original rule-based detections as fallback
            original_anomalies = detect_anomalies(events)
            for anomaly in original_anomalies:
                anomaly["source"] = "rule_based"
                all_anomalies.append(anomaly)
            
            # Simple memory tracking
            reasoning = f"Detect analyzed {len(events)} events and found {len(all_anomalies)} anomalies"
            agent_reasoning = state.get("agent_reasoning", []) + [reasoning]
            
            # Calculate confidence
            avg_confidence = sum(a.get("confidence", 0.5) for a in all_anomalies) / len(all_anomalies) if all_anomalies else 0.5
            
            return {
                "anomalies": all_anomalies,
                "agent_reasoning": agent_reasoning,
                "confidence_scores": {"detect": avg_confidence}
            }
            
        except Exception as e:
            # Fallback to original method if ReAct agent fails
            anomalies = detect_anomalies(events)
            reasoning = f"Detect fallback: found {len(anomalies)} anomalies using rule-based detection"
            agent_reasoning = state.get("agent_reasoning", []) + [reasoning]
            
            return {
                "anomalies": anomalies,
                "agent_reasoning": agent_reasoning,
                "confidence_scores": {"detect": 0.5}
            }
    else:
        # Fallback to original method if no LLM
        anomalies = detect_anomalies(events)
        reasoning = f"Detect fallback: found {len(anomalies)} anomalies using rule-based detection"
        agent_reasoning = state.get("agent_reasoning", []) + [reasoning]
        
        return {
            "anomalies": anomalies,
            "agent_reasoning": agent_reasoning,
            "confidence_scores": {"detect": 0.5}
        }
