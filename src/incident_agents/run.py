# src/incident_agents/run.py
import argparse
from datetime import datetime
from pathlib import Path
from .config import print_status, get_data_path
from .graph import build_graph

def main():
    parser = argparse.ArgumentParser(description="AI Cyber Defence Multi Agents Demo")
    parser.add_argument("--logs", default=None, help="Path to security_logs.csv")
    parser.add_argument(
        "--out", default=None,
        help="Optional path to write a Markdown report (e.g., reports/incident_report.md)"
    )
    parser.add_argument("--show-reasoning", action="store_true", help="Show agent reasoning process")
    args = parser.parse_args()

    log_path = args.logs or get_data_path()
    print_status()

    app = build_graph()
    
    # Add required configuration for checkpointer
    config = {
        "configurable": {
            "thread_id": "incident_response_thread",
            "checkpoint_id": "incident_analysis"
        }
    }
    
    result = app.invoke({"log_path": log_path}, config=config)
    report = result.get("report", "No report.")

    # Console
    print("\n" + "="*60 + "\n" + report + "\n" + "="*60)
    
    # Show enhanced features for YouTube demo
    if args.show_reasoning:
        print("\n" + "="*60)
        print("🤖 AGENT REASONING PROCESS")
        print("="*60)
        
        agent_reasoning = result.get("agent_reasoning", [])
        if agent_reasoning:
            for i, reasoning in enumerate(agent_reasoning, 1):
                print(f"{i}. {reasoning}")
        else:
            print("No reasoning data available (running in fallback mode)")
        
        confidence_scores = result.get("confidence_scores", {})
        if confidence_scores:
            print(f"\n📊 AGENT CONFIDENCE SCORES:")
            for agent, score in confidence_scores.items():
                print(f"   {agent}: {score:.2f}")
        
        # Show simple memory status
        print(f"\n🧠 MEMORY STATUS:")
        print(f"   Reasoning steps: {len(agent_reasoning)}")
        print(f"   Agents with confidence scores: {len(confidence_scores)}")

    # File output (Markdown)
    if args.out:
        out_path = Path(args.out)
        if out_path.is_dir() or str(out_path).endswith("/") or str(out_path).endswith("\\"):
            # If user passed a folder, create timestamped file inside it
            out_path.mkdir(parents=True, exist_ok=True)
            ts = datetime.now().strftime("%Y%m%d-%H%M%S")
            out_path = out_path / f"incident_report_{ts}.md"
        else:
            # Create parent directory if it doesn't exist
            out_path.parent.mkdir(parents=True, exist_ok=True)

        out_path.write_text(report, encoding="utf-8")
        print(f"\n📄 Report saved to: {out_path.resolve()}")

if __name__ == "__main__":
    main()