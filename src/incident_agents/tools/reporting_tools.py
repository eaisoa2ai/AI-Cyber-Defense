from typing import List, Dict, Any
from langchain.tools import tool

@tool
def report_generator_tool(findings: List[Dict[str, Any]]) -> str:
    """Generate markdown incident report from findings"""
    if not findings:
        return "No security incidents detected."
    
    report_lines = ["# Security Incident Report\n"]
    
    # Summary
    severity_counts = {"High": 0, "Medium": 0, "Low": 0}
    for finding in findings:
        severity = finding.get("severity", "Low")
        severity_counts[severity] = severity_counts.get(severity, 0) + 1
    
    report_lines.append(f"## Summary\n")
    report_lines.append(f"- **High Severity**: {severity_counts['High']}")
    report_lines.append(f"- **Medium Severity**: {severity_counts['Medium']}")
    report_lines.append(f"- **Low Severity**: {severity_counts['Low']}\n")
    
    # Findings by severity
    for severity in ["High", "Medium", "Low"]:
        severity_findings = [f for f in findings if f.get("severity") == severity]
        if severity_findings:
            report_lines.append(f"## {severity} Severity Findings\n")
            for finding in severity_findings:
                report_lines.append(f"- **{finding.get('threat_type', 'Unknown')}**")
                report_lines.append(f"  - User: {finding.get('user', 'Unknown')}")
                report_lines.append(f"  - IP: {finding.get('ip', 'Unknown')}")
                report_lines.append(f"  - Rule: {finding.get('rule', 'Unknown')}\n")
    
    return "\n".join(report_lines)

@tool
def action_planner_tool(findings: List[Dict[str, Any]]) -> List[str]:
    """Generate recommended actions based on findings"""
    actions = []
    
    if not findings:
        actions.append("No immediate actions required.")
        return actions
    
    # High severity actions
    high_severity = [f for f in findings if f.get("severity") == "High"]
    if high_severity:
        actions.append("🚨 IMMEDIATE ACTIONS:")
        actions.append("- Isolate affected systems")
        actions.append("- Reset compromised account passwords")
        actions.append("- Block malicious IP addresses at firewall")
        actions.append("- Initiate incident response procedures")
    
    # Medium severity actions
    medium_severity = [f for f in findings if f.get("severity") == "Medium"]
    if medium_severity:
        actions.append("\n⚠️ URGENT ACTIONS:")
        actions.append("- Review and update access controls")
        actions.append("- Enable multi-factor authentication")
        actions.append("- Monitor affected accounts for suspicious activity")
    
    # General recommendations
    actions.append("\n📋 GENERAL RECOMMENDATIONS:")
    actions.append("- Conduct security awareness training")
    actions.append("- Review and update security policies")
    actions.append("- Implement additional monitoring")
    actions.append("- Schedule security assessment")
    
    return actions
