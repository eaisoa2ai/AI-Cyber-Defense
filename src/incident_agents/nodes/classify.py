import json
from typing import Dict, Any, List
from pathlib import Path
from ..state import AgentState
from ..config import get_llm
from ..tools.intel import load_threat_intel, lookup_ip, risk_assessor_tool, context_enricher_tool
from langgraph.prebuilt import create_react_agent

def classify_findings(anomalies: List[Dict[str, Any]], events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    intel_path = Path(__file__).resolve().parents[3] / "data" / "threat_intel.json"
    intel = load_threat_intel(str(intel_path))
    findings = []
    for a in anomalies:
        ip = a.get("ip","")
        ti = lookup_ip(ip, intel)
        severity = "Low"
        threat_type = a["rule"]
        # upgrade with intel & context
        if ti.get("risk_score",0) >= 8.5:
            severity = "High"
            threat_type = ti.get("threat_type", threat_type)
        elif a["rule"] in ("offhours_large_download","privilege_escalation"):
            severity = "High"
        elif a["rule"] in ("brute_force_burst","suspicious_geo_success"):
            severity = "Medium"
        findings.append({
            "rule": a["rule"],
            "threat_type": threat_type,
            "ip": ip,
            "user": a.get("user",""),
            "severity": severity,
            "context": a
        })
    return findings

def classify_node(state: AgentState) -> AgentState:
    anomalies = state.get("anomalies", [])
    events = state.get("events", [])
    
    # Try to use LangGraph's built-in ReAct agent
    llm = get_llm()
    if llm:
        try:
            # Create ReAct agent with classification tools
            react_agent = create_react_agent(
                model=llm,
                tools=[risk_assessor_tool, context_enricher_tool],
                prompt="You are a security threat classification specialist. Assess risk levels and enrich anomalies with context."
            )
            
            # Run the ReAct agent
            response = react_agent.invoke({
                "messages": [{
                    "role": "user",
                    "content": f"Classify these {len(anomalies)} anomalies with risk assessment and context enrichment"
                }]
            })
            
            findings = []
            
            # Process each anomaly with tools
            for anomaly in anomalies:
                # Assess risk
                risk_assessment = risk_assessor_tool.invoke({"anomaly": anomaly})
                
                # Enrich with context
                enriched_anomaly = context_enricher_tool.invoke({"anomaly": anomaly})
                
                # Create finding
                finding = {
                    "rule": anomaly.get("rule", "unknown"),
                    "threat_type": enriched_anomaly.get("context", {}).get("attack_pattern", anomaly.get("rule")),
                    "ip": anomaly.get("ip", ""),
                    "user": anomaly.get("user", ""),
                    "severity": risk_assessment.get("base_risk", "Low"),
                    "risk_score": risk_assessment.get("risk_score", 1.0),
                    "context": enriched_anomaly.get("context", {}),
                    "recommendation": risk_assessment.get("recommendation", "Monitor"),
                    "source": anomaly.get("source", "unknown")
                }
                
                findings.append(finding)
            
            # Add original findings as fallback
            original_findings = classify_findings(anomalies, events)
            for finding in original_findings:
                finding["source"] = "original_classification"
                findings.append(finding)
            
            # Update memory fields
            reasoning = f"Classify ReAct agent assessed {len(anomalies)} anomalies with risk scoring and context enrichment using specialized tools"
            agent_reasoning = state.get("agent_reasoning", []) + [reasoning]
            
            # Add to investigation history
            investigation_history = state.get("investigation_history", []) + [{
                "step": "classify",
                "action": "classified_anomalies",
                "details": {
                    "anomalies_assessed": len(anomalies),
                    "findings_created": len(findings),
                    "high_severity": len([f for f in findings if f.get("severity") == "High"]),
                    "medium_severity": len([f for f in findings if f.get("severity") == "Medium"]),
                    "low_severity": len([f for f in findings if f.get("severity") == "Low"])
                },
                "timestamp": "2025-01-27"
            }]
            
            # Learn patterns from classifications
            learned_patterns = state.get("learned_patterns", {})
            if findings:
                severity_distribution = {}
                for finding in findings:
                    severity = finding.get("severity", "Low")
                    severity_distribution[severity] = severity_distribution.get(severity, 0) + 1
                
                learned_patterns["classification_patterns"] = {
                    "severity_distribution": severity_distribution,
                    "common_threat_types": list(set(f.get("threat_type", "") for f in findings)),
                    "high_risk_ips": list(set(f.get("ip", "") for f in findings if f.get("severity") == "High")),
                    "high_risk_users": list(set(f.get("user", "") for f in findings if f.get("severity") == "High"))
                }
            
            # Calculate confidence
            avg_confidence = sum(f.get("risk_score", 1.0) for f in findings) / len(findings) if findings else 1.0
            
            return {
                "findings": findings,
                "agent_reasoning": agent_reasoning,
                "investigation_history": investigation_history,
                "learned_patterns": learned_patterns,
                "confidence_scores": {"classify": avg_confidence / 10.0}  # Normalize to 0-1
            }
            
        except Exception as e:
            # Fallback to original method if ReAct agent fails
            findings = classify_findings(anomalies, events)
            reasoning = f"Classify fallback: assessed {len(anomalies)} anomalies using original classification method"
            agent_reasoning = state.get("agent_reasoning", []) + [reasoning]
            
            investigation_history = state.get("investigation_history", []) + [{
                "step": "classify",
                "action": "classified_anomalies_fallback",
                "details": {"anomalies_assessed": len(anomalies), "findings_created": len(findings)},
                "timestamp": "2025-01-27"
            }]
            
            return {
                "findings": findings,
                "agent_reasoning": agent_reasoning,
                "investigation_history": investigation_history
            }
    else:
        # Fallback to original method if no LLM
        findings = classify_findings(anomalies, events)
        reasoning = f"Classify fallback: assessed {len(anomalies)} anomalies using original classification method"
        agent_reasoning = state.get("agent_reasoning", []) + [reasoning]
        
        investigation_history = state.get("investigation_history", []) + [{
            "step": "classify",
            "action": "classified_anomalies_no_llm",
            "details": {"anomalies_assessed": len(anomalies), "findings_created": len(findings)},
            "timestamp": "2025-01-27"
        }]
        
        return {
            "findings": findings,
            "agent_reasoning": agent_reasoning,
            "investigation_history": investigation_history
        }
    