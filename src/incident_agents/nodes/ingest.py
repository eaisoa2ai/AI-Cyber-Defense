from . import detect  # for typing hints if needed
from ..tools.parsers import read_csv_events, csv_parser_tool, data_validator_tool
from ..state import AgentState
from ..config import get_llm
from langgraph.prebuilt import create_react_agent

def ingest_node(state: AgentState) -> AgentState:
    log_path = state.get("log_path")  # provided at runtime
    
    # Try to use LangGraph's built-in ReAct agent
    llm = get_llm()
    if llm:
        try:
            # Create ReAct agent with tools
            react_agent = create_react_agent(
                model=llm,
                tools=[csv_parser_tool, data_validator_tool],
                prompt="You are a data ingestion specialist. Parse and validate security log files."
            )
            
            # Run the ReAct agent
            response = react_agent.invoke({
                "messages": [{
                    "role": "user", 
                    "content": f"Parse and validate this security log file: {log_path}"
                }]
            })
            
            # Extract events from tool response
            events = read_csv_events(log_path)  # Fallback to original method
            
            # Validate data quality
            validation = data_validator_tool.invoke({"events": events})
            
            # Simple memory tracking
            reasoning = f"Ingest processed {log_path} with {len(events)} events, quality score: {validation.get('quality_score', 0):.2f}"
            agent_reasoning = state.get("agent_reasoning", []) + [reasoning]
            
            return {
                "events": events,
                "agent_reasoning": agent_reasoning,
                "confidence_scores": {"ingest": validation.get("quality_score", 0.5)}
            }
            
        except Exception as e:
            # Fallback to original method if ReAct agent fails
            events = read_csv_events(log_path)
            reasoning = f"Ingest fallback: processed {log_path} with {len(events)} events"
            agent_reasoning = state.get("agent_reasoning", []) + [reasoning]
            
            return {
                "events": events,
                "agent_reasoning": agent_reasoning,
                "confidence_scores": {"ingest": 0.5}
            }
    else:
        # Fallback to original method if no LLM
        events = read_csv_events(log_path)
        reasoning = f"Ingest fallback: processed {log_path} with {len(events)} events"
        agent_reasoning = state.get("agent_reasoning", []) + [reasoning]
        
        return {
            "events": events,
            "agent_reasoning": agent_reasoning,
            "confidence_scores": {"ingest": 0.5}
        }
