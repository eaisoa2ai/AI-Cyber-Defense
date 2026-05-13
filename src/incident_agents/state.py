from typing import TypedDict, List, Dict, Any, Optional

class AgentState(TypedDict, total=False):
    log_path: str
    events: List[Dict[str, Any]]
    anomalies: List[Dict[str, Any]]
    findings: List[Dict[str, Any]]
    report: str
    
    # Simple memory tracking
    agent_reasoning: List[str]                    # Track agent reasoning process
    confidence_scores: Dict[str, float]           # Track confidence per agent
