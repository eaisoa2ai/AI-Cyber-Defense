import json
from typing import Dict, Any, List
from langchain.tools import tool

def load_threat_intel(path: str) -> Dict[str, Any]:
    with open(path, "r") as f:
        return json.load(f)

def lookup_ip(ip: str, intel: Dict[str, Any]) -> Dict[str, Any]:
    return intel.get(ip, {"risk_score": 0.0, "threat_type": "Unknown", "source": "None"})

@tool
def risk_assessor_tool(anomaly: Dict[str, Any]) -> Dict[str, Any]:
    """Assess risk level of an anomaly based on type and context"""
    risk_assessment = {
        "anomaly_type": anomaly.get("rule", "unknown"),
        "base_risk": "Low",
        "risk_score": 1.0,
        "factors": [],
        "recommendation": "Monitor"
    }
    
    # Assess based on anomaly type
    if anomaly.get("rule") == "privilege_escalation":
        risk_assessment.update({
            "base_risk": "High",
            "risk_score": 8.5,
            "factors": ["Privilege escalation detected"],
            "recommendation": "Immediate investigation required"
        })
    elif anomaly.get("rule") == "brute_force_burst":
        risk_assessment.update({
            "base_risk": "Medium",
            "risk_score": 6.0,
            "factors": ["Multiple failed login attempts"],
            "recommendation": "Investigate and potentially block IP"
        })
    elif anomaly.get("rule") == "offhours_large_download":
        risk_assessment.update({
            "base_risk": "Medium",
            "risk_score": 5.5,
            "factors": ["Large data transfer during off-hours"],
            "recommendation": "Review data access patterns"
        })
    
    return risk_assessment

@tool
def context_enricher_tool(anomaly: Dict[str, Any]) -> Dict[str, Any]:
    """Enrich anomaly with historical context and patterns"""
    enriched_anomaly = anomaly.copy()
    
    # Add context based on anomaly type
    if anomaly.get("rule") == "brute_force_burst":
        enriched_anomaly["context"] = {
            "attack_pattern": "Credential stuffing",
            "likely_automated": True,
            "common_targets": ["admin", "root", "service accounts"],
            "mitigation": "Implement account lockout policies"
        }
    elif anomaly.get("rule") == "privilege_escalation":
        enriched_anomaly["context"] = {
            "attack_pattern": "Privilege escalation",
            "likely_automated": False,
            "common_targets": ["sudo", "runas", "elevation"],
            "mitigation": "Implement least privilege principle"
        }
    elif anomaly.get("rule") == "offhours_large_download":
        enriched_anomaly["context"] = {
            "attack_pattern": "Data exfiltration",
            "likely_automated": True,
            "common_targets": ["sensitive data", "large files"],
            "mitigation": "Implement data loss prevention"
        }
    
    return enriched_anomaly
