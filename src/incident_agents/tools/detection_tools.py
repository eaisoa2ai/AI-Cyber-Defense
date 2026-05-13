from typing import List, Dict, Any
from langchain.tools import tool
from datetime import datetime, timedelta
from collections import defaultdict

@tool
def pattern_detector_tool(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Detect known attack patterns in security events"""
    patterns = []
    
    # Brute force pattern detection
    fails_by_key = defaultdict(list)
    for e in events:
        if e.get("event_type") == "login" and e.get("status") == "fail":
            key = (e.get("user"), e.get("source_ip"))
            fails_by_key[key].append(e.get("timestamp"))
    
    for (user, ip), times in fails_by_key.items():
        if len(times) >= 5:
            patterns.append({
                "pattern": "brute_force",
                "user": user,
                "ip": ip,
                "count": len(times),
                "confidence": 0.8
            })
    
    # Privilege escalation pattern
    for e in events:
        if e.get("event_type") == "sudo":
            patterns.append({
                "pattern": "privilege_escalation",
                "user": e.get("user"),
                "ip": e.get("source_ip"),
                "message": e.get("message", ""),
                "confidence": 0.9
            })
    
    return patterns

@tool
def anomaly_detector_tool(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Detect statistical anomalies in security events"""
    anomalies = []
    
    # Off-hours activity detection
    for e in events:
        if e.get("event_type") == "data_download":
            try:
                timestamp = datetime.fromisoformat(e.get("timestamp").replace("T", " "))
                if timestamp.hour < 5 and int(e.get("bytes", 0)) >= 1_000_000:
                    anomalies.append({
                        "anomaly": "offhours_large_download",
                        "user": e.get("user"),
                        "ip": e.get("source_ip"),
                        "bytes": int(e.get("bytes", 0)),
                        "timestamp": e.get("timestamp"),
                        "confidence": 0.7
                    })
            except:
                continue
    
    # Geographic anomaly detection
    for e in events:
        if e.get("event_type") == "login" and e.get("status") == "success":
            if e.get("country") not in ("US", "CA", None):
                anomalies.append({
                    "anomaly": "foreign_login",
                    "user": e.get("user"),
                    "ip": e.get("source_ip"),
                    "country": e.get("country"),
                    "confidence": 0.6
                })
    
    return anomalies

@tool
def threat_lookup_tool(ip: str) -> Dict[str, Any]:
    """Look up IP address in threat intelligence"""
    # This would integrate with real threat intel APIs
    # For now, return mock data
    threat_data = {
        "ip": ip,
        "risk_score": 0.0,
        "threat_type": "Unknown",
        "reputation": "Unknown",
        "last_seen": None
    }
    
    # Mock high-risk IPs for demo
    high_risk_ips = ["192.168.1.100", "10.0.0.50"]
    if ip in high_risk_ips:
        threat_data.update({
            "risk_score": 8.5,
            "threat_type": "Malware C2",
            "reputation": "Malicious",
            "last_seen": "2024-01-15"
        })
    
    return threat_data
