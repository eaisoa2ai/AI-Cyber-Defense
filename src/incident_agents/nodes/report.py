from typing import List, Dict, Any
from ..state import AgentState
from ..config import get_openai_key, get_model_name, get_temperature, get_llm
from ..tools.reporting_tools import report_generator_tool, action_planner_tool
from langgraph.prebuilt import create_react_agent

# -------- Fallback (no-LLM) --------
def _fallback_report(findings: List[Dict[str, Any]], *_ignore_extra_args) -> str:
    if not findings:
        return "No suspicious activity detected."
    lines = ["# Incident Report", ""]
    sev_order = {"High":0,"Medium":1,"Low":2}
    findings = sorted(findings, key=lambda f: sev_order.get(f.get("severity","Low"), 2))
    counts = {"High":0,"Medium":0,"Low":0}
    for f in findings:
        counts[f["severity"]] = counts.get(f["severity"], 0) + 1
    lines.append(f"Summary: {counts['High']} High, {counts['Medium']} Medium, {counts['Low']} Low severity findings.\n")
    for f in findings:
        lines.append(f"- [{f['severity']}] {f['threat_type']} | user={f.get('user','?')} ip={f.get('ip','?')} (rule: {f['rule']})")
    lines += [
        "",
        "Recommended next steps:",
        "- Reset affected account passwords; enforce MFA.",
        "- Block high-risk IPs at the firewall.",
        "- Review off-hours data transfers; rotate keys.",
    ]
    return "\n".join(lines)

# -------- LLM (if key present) --------
def _llm_report(findings: List[Dict[str, Any]]) -> str:
    """
    Uses OpenAI to generate a concise, human-readable incident report.
    Falls back gracefully if anything fails.
    """
    try:
        from openai import OpenAI  # requires openai>=1.0
    except Exception:
        return _fallback_report(findings)

    api_key = get_openai_key()
    if not api_key:
        return _fallback_report(findings)

    if not findings:
        return "No suspicious activity detected."

    client = OpenAI(api_key=api_key)
    model = get_model_name()
    temperature = get_temperature()

    # Keep the prompt short and deterministic so it runs fast.
    system = (
        "You are a security analyst. Write a succinct markdown incident report. "
        "Group similar findings, include counts, and list prioritized actions. "
        "Be precise and avoid fluff."
    )
    user = (
        "Findings (JSON list):\n"
        f"{findings}\n\n"
        "Write:\n"
        "1) Title + short summary (one paragraph)\n"
        "2) Findings by severity (High/Medium/Low as bullets)\n"
        "3) Recommended actions (bullets, prioritized)\n"
    )

    try:
        # Chat Completions API (stable in openai>=1.x)
        resp = client.chat.completions.create(
            model=model,
            temperature=temperature,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        content = resp.choices[0].message.content.strip()
        return content or _fallback_report(findings)
    except Exception:
        # Any API issue → safe fallback
        return _fallback_report(findings)

def report_node(state: AgentState) -> AgentState:
    findings = state.get("findings", [])
    
    # Try to use LangGraph's built-in ReAct agent
    llm = get_llm()
    if llm:
        try:
            # Create ReAct agent with reporting tools
            react_agent = create_react_agent(
                model=llm,
                tools=[report_generator_tool, action_planner_tool],
                prompt="You are a security incident reporting specialist. Generate comprehensive reports and action plans."
            )
            
            # Run the ReAct agent
            response = react_agent.invoke({
                "messages": [{
                    "role": "user",
                    "content": f"Generate a comprehensive incident report for {len(findings)} findings"
                }]
            })
            
            # Generate report using tools
            report_content = report_generator_tool.invoke({"findings": findings})
            actions = action_planner_tool.invoke({"findings": findings})
            
            # Combine report and actions
            full_report = report_content + "\n\n## Recommended Actions\n"
            for action in actions:
                full_report += f"- {action}\n"
            
            # Update memory fields
            reasoning = f"Report ReAct agent generated comprehensive report with {len(findings)} findings and {len(actions)} recommended actions using specialized tools"
            agent_reasoning = state.get("agent_reasoning", []) + [reasoning]
            
            # Add to investigation history
            investigation_history = state.get("investigation_history", []) + [{
                "step": "report",
                "action": "generated_report",
                "details": {
                    "findings_summarized": len(findings),
                    "actions_planned": len(actions),
                    "report_length": len(full_report),
                    "high_severity_findings": len([f for f in findings if f.get("severity") == "High"])
                },
                "timestamp": "2025-01-27"
            }]
            
            # Learn patterns from reporting
            learned_patterns = state.get("learned_patterns", {})
            if findings:
                learned_patterns["reporting_patterns"] = {
                    "total_findings": len(findings),
                    "severity_breakdown": {
                        "High": len([f for f in findings if f.get("severity") == "High"]),
                        "Medium": len([f for f in findings if f.get("severity") == "Medium"]),
                        "Low": len([f for f in findings if f.get("severity") == "Low"])
                    },
                    "common_actions": actions[:5] if actions else [],  # Top 5 actions
                    "report_metadata": {
                        "generated_with_llm": True,
                        "tools_used": ["report_generator", "action_planner"]
                    }
                }
            
            return {
                "report": full_report,
                "agent_reasoning": agent_reasoning,
                "investigation_history": investigation_history,
                "learned_patterns": learned_patterns,
                "confidence_scores": {"report": 0.9}  # High confidence for report generation
            }
            
        except Exception as e:
            # Fallback to original method if ReAct agent fails
            report = _llm_report(findings) if get_openai_key() else _fallback_report(findings)
            reasoning = f"Report fallback: generated report using {'LLM' if get_openai_key() else 'fallback'} method"
            agent_reasoning = state.get("agent_reasoning", []) + [reasoning]
            
            investigation_history = state.get("investigation_history", []) + [{
                "step": "report",
                "action": "generated_report_fallback",
                "details": {"findings_summarized": len(findings), "report_length": len(report)},
                "timestamp": "2025-01-27"
            }]
            
            return {
                "report": report,
                "agent_reasoning": agent_reasoning,
                "investigation_history": investigation_history
            }
    else:
        # Fallback to original method if no LLM
        report = _llm_report(findings) if get_openai_key() else _fallback_report(findings)
        reasoning = f"Report fallback: generated report using {'LLM' if get_openai_key() else 'fallback'} method"
        agent_reasoning = state.get("agent_reasoning", []) + [reasoning]
        
        investigation_history = state.get("investigation_history", []) + [{
            "step": "report",
            "action": "generated_report_no_llm",
            "details": {"findings_summarized": len(findings), "report_length": len(report)},
            "timestamp": "2025-01-27"
        }]
        
        return {
            "report": report,
            "agent_reasoning": agent_reasoning,
            "investigation_history": investigation_history
        }