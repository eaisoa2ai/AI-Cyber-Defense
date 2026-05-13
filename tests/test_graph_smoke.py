from incident_agents.graph import build_graph

def test_compiles():
    app = build_graph().compile()
    assert app is not None
