# 🤖 AI Incident Response Agents

> **Automated cybersecurity threat detection using AI agents** - Perfect for SOC teams, security professionals, and anyone interested in AI-powered security!

## 🎯 What This Does

This system automatically analyzes security logs and detects threats using 4 AI agents:

```
📊 Security Logs → 🤖 AI Agents → 📋 Professional Reports
```

**Detects:**
- 🔥 Brute force attacks
- 🚨 Privilege escalation attempts  
- 🌍 Suspicious geographic logins
- 📥 Large off-hours data downloads
- 🎯 And more...

## ⚡ Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# 🖥️ Option 1: Command Line Interface
python -m src.incident_agents.run

# 🌐 Option 2: Beautiful Web Interface (Gradio)
python run_gradio_app.py

# 📊 Run with all features (CLI)
python -m src.incident_agents.run --logs data/security_logs.csv --out reports/incident_report.md --show-reasoning
```

## 🚀 Key Features

- **🤖 AI-Powered**: Uses OpenAI GPT models for intelligent analysis
- **🌐 Beautiful Web Interface**: Modern Gradio app with drag-and-drop file upload
- **🛡️ Robust**: Works with or without AI (fallback mode)
- **📊 Professional Reports**: Generates markdown reports with actionable recommendations
- **🧠 Memory**: Learns from previous investigations
- **⚙️ Customizable**: Easy to add new detection rules
- **🎯 Confidence Scoring**: Shows how confident each agent is

## 📊 Sample Output

```
=== Configuration Status ===
OpenAI API Key: ✅ Set
Model: gpt-4o-mini

============================================================
# Security Incident Report

## Summary
- **High Severity**: 20
- **Medium Severity**: 1  
- **Low Severity**: 31

## High Severity Findings
- **Privilege Escalation** | user=adoyle ip=23.195.123.128
- **Brute Force Login** | user=jsmith ip=185.231.112.45

## Recommended Actions
🚨 IMMEDIATE ACTIONS:
- Isolate affected systems
- Reset compromised account passwords
- Block malicious IP addresses at firewall
============================================================
```

## 🏗️ How It Works

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   INGEST    │───▶│   DETECT    │───▶│  CLASSIFY   │───▶│   REPORT    │
│   AGENT     │    │   AGENT     │    │   AGENT     │    │   AGENT     │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
   📁 Reads         🔍 Finds         ⚖️ Assesses      📄 Generates
   security logs    threats &        risk levels      incident reports
   & validates      anomalies        & enriches       & action plans
```

## 🛠️ Setup (Optional AI Features)

```bash
# Add OpenAI API key for full AI capabilities
echo "OPENAI_API_KEY=your_api_key_here" >> my_env.env
```

## 📁 Project Structure

```
ai-incident-response-agents2/
├── 📁 data/                    # Sample security logs
├── 📁 src/incident_agents/     # Main code
│   ├── 📁 nodes/              # 4 AI agents
│   ├── 📁 tools/              # Specialized AI tools
│   └── run.py                 # Main script
├── 📁 reports/                # Generated reports
└── requirements.txt           # Dependencies
```

## 🌐 Gradio Web Interface

The beautiful web interface provides:

- **📁 Drag & Drop Upload**: Easy CSV file upload
- **⚙️ Real-time Configuration**: Adjust AI model and temperature
- **📊 Live Status Updates**: See analysis progress in real-time
- **🎨 Professional UI**: Modern, responsive design
- **📋 Rich Results**: Formatted reports with severity breakdowns
- **🤖 Agent Insights**: Optional detailed reasoning process

**Access the web app at:** `http://localhost:7860`

## 🎬 Perfect For

- **YouTube Content** 🎥
- **Security Demos** 🛡️
- **AI Learning** 🤖
- **SOC Teams** 🔍
- **Research** 📚

## 🚨 Troubleshooting

**No OpenAI API Key?** → System works in fallback mode!

**Import Errors?** → `pip install -r requirements.txt`

**File Not Found?** → Check your log file path

## 📞 Support

- **Issues**: Create GitHub issue
- **Questions**: Check the detailed README_DETAILED.md
- **Customization**: See examples in the code

---

**🎯 Ready to automate your security analysis?** 

```bash
git clone <your-repo>
cd ai-incident-response-agents2
python -m src.incident_agents.run
```

**⭐ Star this repo if it helps!**
