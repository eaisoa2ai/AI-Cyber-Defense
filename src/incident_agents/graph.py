from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from .state import AgentState
from .nodes.ingest import ingest_node
from .nodes.detect import detect_node
from .nodes.classify import classify_node
from .nodes.report import report_node

def build_graph():
    graph = StateGraph(AgentState)
    graph.add_node("ingest", ingest_node)
    graph.add_node("detect", detect_node)
    graph.add_node("classify", classify_node)
    graph.add_node("report", report_node)

    graph.add_edge(START, "ingest")
    graph.add_edge("ingest", "detect")

    # Conditional edge: if anomalies exist -> classify, else END
    def has_anomalies(state: AgentState) -> str:
        return "classify" if state.get("anomalies") else END

    graph.add_conditional_edges("detect", has_anomalies, {"classify": "classify", END: END})

    # Conditional edge: if any High/Medium -> report else END
    def needs_report(state: AgentState) -> str:
        f = state.get("findings", [])
        levels = {x.get("severity","Low") for x in f}
        return "report" if any(s in ("High","Medium") for s in levels) else END

    graph.add_conditional_edges("classify", needs_report, {"report": "report", END: END})
    graph.add_edge("report", END)

    # Add memory with checkpointing
    checkpointer = InMemorySaver()
    return graph.compile(checkpointer=checkpointer)
