#!/usr/bin/env python3
"""
Gradio App Launcher for AI Incident Response Agents
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from incident_agents.app import launch_app

if __name__ == "__main__":
    print("🚀 Starting AI Cyber Defence Gradio App...")
    print("🌐 Creating public link for easy access...")
    print("🔗 Public URL will be displayed when ready")
    print("⏹️  Press Ctrl+C to stop the server")
    print("-" * 60)
    
    try:
        # Use a simple and reliable configuration
        print("🌐 Creating public link...")
        launch_app(share=True, server_port=8080)
            
    except KeyboardInterrupt:
        print("\n👋 Gradio app stopped. Goodbye!")
    except Exception as e:
        print(f"❌ Error starting app: {e}")
        print("💡 Make sure you have installed all dependencies: pip install -r requirements.txt")
