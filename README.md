# 🤖 AI Incident Response Agents

This repository serves as a sanitized, production-ready reference architecture built to demonstrate enterprise agentic patterns. 
It mirrors the architectural designs, multi-agent state machines, and evaluation frameworks I deploy in enterprise environments, stripped of proprietary data and corporate logic.

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

=======
## 🎯 Project Overview

An intelligent cybersecurity system that uses AI agents to automatically detect, analyze, and respond to security threats in real-time. This project demonstrates advanced AI techniques including ReAct agents, tool usage, memory, and reasoning capabilities.

```
┌─────────────────────────────────────────────────────────────┐
│                    AI CYBER DEFENCE                         │
│                 MULTI AGENTS SYSTEM                         │
└─────────────────────────────────────────────────────────────┘

📊 Security Logs → 🤖 AI Agents → 📋 Incident Reports
     ↓                    ↓              ↓
  Raw Data           Threat Analysis   Action Plans
```

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    WORKFLOW PIPELINE                        │
└─────────────────────────────────────────────────────────────┘

┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   INGEST    │───▶│   DETECT    │───▶│  CLASSIFY   │───▶│   REPORT    │
│   AGENT     │    │   AGENT     │    │   AGENT     │    │   AGENT     │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
       │                   │                   │                   │
   📁 Reads           🔍 Finds            ⚖️ Assesses         📄 Generates
   security logs      threats &           risk levels         incident reports
   & validates        anomalies           & enriches          & action plans
   data quality       using AI tools      with context        using AI tools
```

## 🧠 Agent Capabilities

### 🤖 ReAct Agents with Reasoning
Each agent uses the ReAct (Reasoning + Acting) framework:
- **Reasoning**: Agents think through problems step-by-step
- **Acting**: Agents use specialized tools to perform tasks
- **Memory**: Agents learn from previous investigations
- **Confidence Scoring**: Agents provide confidence levels for their decisions

### 🛠️ Specialized Tools
Each agent has access to domain-specific tools:

```
┌─────────────────────────────────────────────────────────────┐
│                        AGENT TOOLS                          │
└─────────────────────────────────────────────────────────────┘

📥 INGEST TOOLS:
├── CSV Parser Tool: Reads security log files
└── Data Validator Tool: Checks data quality

🔍 DETECT TOOLS:
├── Pattern Detector Tool: Finds known attack patterns
├── Anomaly Detector Tool: Detects statistical anomalies
└── Threat Lookup Tool: Checks IP addresses against threat databases

⚖️ CLASSIFY TOOLS:
├── Risk Assessor Tool: Evaluates threat risk levels
└── Context Enricher Tool: Adds historical context

📄 REPORT TOOLS:
├── Report Generator Tool: Creates structured reports
└── Action Planner Tool: Generates response recommendations
```

## 🔄 Workflow Process

### 1. 📥 **Ingest Agent** - Data Loading & Validation
```
┌─────────────────────────────────────────────────────────────┐
│                    INGEST PROCESS                           │
└─────────────────────────────────────────────────────────────┘

📁 Security Logs → 🔍 Data Validation → ✅ Clean Events
     ↓                    ↓                    ↓
  Raw CSV files      Quality checks      Structured data
  (login attempts,   (missing fields,    ready for analysis
   downloads, etc.)   format issues)      by other agents)
```

**What it does:**
- Reads security log files (CSV format)
- Validates data quality and completeness
- Uses AI tools to parse and clean data
- Falls back to simple CSV reading if AI unavailable

**Key Functions:**
- `ingest_node()`: Main agent function
- `read_csv_events()`: Reads CSV files
- `csv_parser_tool()`: AI-powered CSV parsing
- `data_validator_tool()`: Data quality assessment

### 2. 🔍 **Detect Agent** - Threat Detection & Analysis
```
┌─────────────────────────────────────────────────────────────┐
│                    DETECT PROCESS                           │
└─────────────────────────────────────────────────────────────┘

✅ Clean Events → 🔍 Pattern Analysis → 🚨 Detected Anomalies
     ↓                    ↓                    ↓
  Structured data    AI pattern detection   List of threats
  from ingest        (brute force,          with details
  agent              privilege escalation,   (users, IPs,
                      data exfiltration)     timestamps)
```

**What it does:**
- Analyzes security events for suspicious patterns
- Uses AI tools to detect known attack patterns and statistical anomalies
- Falls back to rule-based detection if AI unavailable
- Detects multiple threat types

**Threat Detection Rules:**
- **Rule A**: Brute force attacks (5+ failed logins in 10 minutes)
- **Rule B**: Suspicious geographic logins (success after failures from foreign countries)
- **Rule C**: Large off-hours data downloads (>1MB between 00:00-05:00)
- **Rule D**: Privilege escalation attempts (sudo commands)

**Key Functions:**
- `detect_node()`: Main agent function
- `detect_anomalies()`: Core detection logic
- `parse_ts()`: Timestamp parsing
- `pattern_detector_tool()`: AI pattern detection
- `anomaly_detector_tool()`: Statistical anomaly detection

### 3. ⚖️ **Classify Agent** - Risk Assessment & Context Enrichment
```
┌─────────────────────────────────────────────────────────────┐
│                   CLASSIFY PROCESS                          │
└─────────────────────────────────────────────────────────────┘

🚨 Detected Anomalies → ⚖️ Risk Assessment → 📊 Classified Findings
     ↓                        ↓                        ↓
  Raw threat data        AI risk evaluation      Prioritized threats
  from detect agent      (High/Medium/Low)       with context &
                        + threat intelligence    recommendations
```

**What it does:**
- Takes detected anomalies and assigns risk levels
- Enriches findings with threat intelligence
- Uses AI tools to assess risk and add context
- Falls back to simple rule-based classification

**Risk Levels:**
- **High Risk**: Known malicious IPs, privilege escalation, large off-hours downloads
- **Medium Risk**: Brute force attacks, suspicious geographic logins
- **Low Risk**: Everything else

**Key Functions:**
- `classify_node()`: Main agent function
- `classify_findings()`: Risk assessment logic
- `load_threat_intel()`: Loads threat intelligence data
- `lookup_ip()`: Checks IP addresses against threat databases
- `risk_assessor_tool()`: AI risk assessment
- `context_enricher_tool()`: Context enrichment

### 4. 📄 **Report Agent** - Report Generation & Action Planning
```
┌─────────────────────────────────────────────────────────────┐
│                    REPORT PROCESS                           │
└─────────────────────────────────────────────────────────────┘

📊 Classified Findings → 📄 Report Generation → 🎯 Action Plans
     ↓                        ↓                        ↓
  Prioritized threats    AI report creation      Recommended
  from classify agent    (markdown format)       response actions
                        + confidence scores      for security team
```

**What it does:**
- Generates human-readable incident reports
- Uses AI to create detailed, professional reports
- Falls back to simple text reports if AI unavailable
- Includes recommended actions and next steps

**Report Features:**
- Structured markdown format
- Findings grouped by severity
- Confidence scores for each agent
- Recommended response actions
- Executive summary

**Key Functions:**
- `report_node()`: Main agent function
- `_llm_report()`: AI-powered report generation
- `_fallback_report()`: Simple text report generation
- `report_generator_tool()`: AI report creation
- `action_planner_tool()`: Response action planning

## 🧠 Memory & Learning

The system includes advanced memory capabilities:

```
┌─────────────────────────────────────────────────────────────┐
│                    MEMORY SYSTEM                            │
└─────────────────────────────────────────────────────────────┘

🧠 Investigation History → 📚 Learned Patterns → 🎯 Improved Detection
     ↓                        ↓                        ↓
  Previous investigation   Patterns from past      Better threat
  steps and decisions      incidents stored        detection in
  stored in memory         for future use          future runs
```

**Memory Features:**
- **Investigation History**: Tracks previous investigation steps
- **Learned Patterns**: Stores patterns from past incidents
- **Agent Reasoning**: Records agent decision-making process
- **Confidence Scores**: Tracks agent performance over time

## 🚀 Getting Started

### Prerequisites
```bash
# Python 3.8+ required
python --version
```

### Environment Setup
```bash
# Create environment file
cp my_env.env.example my_env.env

# Add your OpenAI API key (optional - system works without it)
echo "OPENAI_API_KEY=your_api_key_here" >> my_env.env

# Create virtual environment
python -m venv ai_cyber_defence
ai_cyber_defence\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```


### Basic Usage

#### 🖥️ Command Line Interface (CLI)
```bash
# Run with default data
python -m src.incident_agents.run

# Run with custom log file
python -m src.incident_agents.run --logs data/security_logs.csv

# Run with reasoning display
python -m src.incident_agents.run --show-reasoning

# Save report to file
python -m src.incident_agents.run --out reports/incident_report.md

# All options
python -m src.incident_agents.run --logs data/security_logs.csv --out reports/incident_report.md --show-reasoning
```

#### 🌐 Web Interface (Gradio)
```bash
# Launch the beautiful web interface
python run_gradio_app.py

# Access the web app at: http://localhost:7860
```

### Complete Command Example
```bash
# Run with all features enabled
python -m src.incident_agents.run --logs data/security_logs.csv --out reports/incident_report.md --show-reasoning
```

## 🌐 Gradio Web Interface

The project includes a beautiful, modern web interface built with Gradio that provides an intuitive way to interact with the AI incident response agents.

### 🎨 Interface Features

```
┌─────────────────────────────────────────────────────────────┐
│                GRADIO WEB INTERFACE                         │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ 🤖 AI Incident Response Agents                             │
│ Automated cybersecurity threat detection using AI agents   │
└─────────────────────────────────────────────────────────────┘

┌─────────────────┐  ┌─────────────────────────────────────────┐
│ 📁 Upload       │  │ 📋 Analysis Results                    │
│ Security Logs   │  │                                         │
│                 │  │ 📊 Analysis Summary                     │
│ [Upload CSV]    │  │ • Total Findings: 5                    │
│                 │  │ • 🔴 High Severity: 2                  │
│ ⚙️ Configuration│  │ • 🟡 Medium Severity: 2                │
│                 │  │ • 🟢 Low Severity: 1                   │
│ [Show Reasoning]│  │                                         │
│ [Model: GPT-4]  │  │ 📋 Detailed Report                     │
│ [Temperature]   │  │ [Full incident report with findings]   │
│                 │  │                                         │
│ 🚀 [Analyze]    │  │ 🤖 Agent Reasoning Process             │
│                 │  │ [Detailed AI agent reasoning steps]    │
│ 📊 Status       │  │                                         │
│ ✅ Complete     │  │ 📊 Agent Confidence Scores              │
└─────────────────┘  │ [Confidence bars for each agent]       │
                     └─────────────────────────────────────────┘
```

### 🚀 Quick Start with Web Interface

1. **Launch the App**
   ```bash
   python run_gradio_app.py
   ```

2. **Access the Interface**
   - Open your browser to `http://localhost:7860`
   - The interface will load with a welcome message

3. **Upload Security Logs**
   - Drag and drop a CSV file or click to browse
   - Or leave empty to use sample data

4. **Configure Analysis**
   - **Show Agent Reasoning**: Toggle to see detailed AI reasoning
   - **AI Model**: Choose between GPT-4o-mini, GPT-4o, or GPT-3.5-turbo
   - **Temperature**: Adjust AI creativity (0.0 = deterministic, 1.0 = creative)

5. **Run Analysis**
   - Click the "🚀 Analyze Security Logs" button
   - Watch real-time status updates
   - View comprehensive results

### 🎯 Interface Components

#### 📁 File Upload Section
- **Drag & Drop Support**: Modern file upload with visual feedback
- **File Type Validation**: Automatically accepts CSV files
- **Sample Data**: Works without upload using built-in sample data
- **File Preview**: Shows uploaded file information

#### ⚙️ Configuration Panel
- **Show Agent Reasoning**: Toggle for detailed AI reasoning display
- **Model Selection**: Dropdown with available AI models
- **Temperature Slider**: Real-time adjustment of AI creativity
- **Tooltips**: Helpful information for each setting

#### 📊 Status Display
- **Real-time Updates**: Live status during analysis
- **Color-coded States**: 
  - 🟢 Ready to analyze
  - 🟡 Analyzing in progress
  - 🟢 Analysis complete
  - 🔴 Analysis failed
- **Progress Indicators**: Visual feedback during processing

#### 📋 Results Display
- **Rich Markdown**: Formatted reports with headers, lists, and emphasis
- **Severity Breakdown**: Color-coded severity levels (🔴🟡🟢)
- **Agent Confidence**: Visual confidence bars for each agent
- **Detailed Reasoning**: Step-by-step AI reasoning process
- **Configuration Summary**: Analysis parameters and timestamp

### 🎨 UI/UX Features

#### Modern Design
- **Responsive Layout**: Works on desktop, tablet, and mobile
- **Gradient Headers**: Beautiful purple gradient design
- **Professional Styling**: Clean, modern interface
- **Custom CSS**: Enhanced visual appeal

#### User Experience
- **Intuitive Workflow**: Logical step-by-step process
- **Visual Feedback**: Clear status indicators and progress
- **Error Handling**: Graceful error messages and recovery
- **Accessibility**: Keyboard navigation and screen reader support

### 🔧 Advanced Configuration

#### Customizing the Interface
Edit `src/incident_agents/app.py` to customize:

```python
# Custom CSS styling
custom_css = """
.gradio-container {
    max-width: 1200px !important;
    margin: auto !important;
}
.main-header {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 20px;
    border-radius: 10px;
}
"""

# Launch options
def launch_app(share=False, server_name="0.0.0.0", server_port=7860):
    demo = create_gradio_interface()
    demo.launch(
        share=share,              # Enable public sharing
        server_name=server_name,  # Server hostname
        server_port=server_port,  # Port number
        show_error=True           # Show detailed errors
    )
```

#### Deployment Options
```bash
# Local development
python run_gradio_app.py

# Public sharing (temporary public URL)
# Edit run_gradio_app.py and set share=True

# Custom port
python -c "from src.incident_agents.app import launch_app; launch_app(server_port=8080)"

# Production deployment
# Use with reverse proxy (nginx) for production use
```

### 📱 Mobile Support

The Gradio interface is fully responsive and works on:
- **Desktop**: Full-featured experience
- **Tablet**: Optimized layout for medium screens
- **Mobile**: Touch-friendly interface for phones

### 🔒 Security Considerations

#### File Upload Security
- **File Type Validation**: Only accepts CSV files
- **Temporary Storage**: Uploaded files are stored temporarily
- **Automatic Cleanup**: Files are deleted after processing
- **No Persistent Storage**: Files are not saved permanently

#### Network Security
- **Local by Default**: Runs on localhost only
- **Optional Public Sharing**: Can be enabled for demos
- **No Authentication**: Basic interface (add auth for production)

### 🎬 Perfect for Demos

The web interface is ideal for:
- **YouTube Content**: Beautiful, professional appearance
- **Client Presentations**: Easy to demonstrate capabilities
- **Training Sessions**: Interactive learning experience
- **Live Demos**: Real-time analysis and results
- **Screenshots**: Professional-looking interface for documentation

### 🚨 Troubleshooting Web Interface

#### Common Issues

**1. Port Already in Use**
```
OSError: [Errno 98] Address already in use
```
**Solution**: Change port or kill existing process
```bash
python -c "from src.incident_agents.app import launch_app; launch_app(server_port=7861)"
```

**2. Gradio Not Installed**
```
ModuleNotFoundError: No module named 'gradio'
```
**Solution**: Install Gradio
```bash
pip install gradio>=4.0.0
```

**3. File Upload Issues**
```
Error: File format not supported
```
**Solution**: Ensure file is CSV format and properly formatted

**4. Slow Loading**
```
Interface takes long to load
```
**Solution**: Check internet connection for model downloads, or use local models

#### Performance Tips
- **Use Sample Data**: Faster for demos and testing
- **Reduce File Size**: Smaller CSV files process faster
- **Close Other Apps**: Free up system resources
- **Use Local Models**: Avoid network latency for model loading

## 📊 Sample Output

### Console Output
>>>>>>> cdf477d6b3713a60db70cfacdf4b4b7d4d37702c
```
=== Configuration Status ===
OpenAI API Key: ✅ Set
Model: gpt-4o-mini
<<<<<<< HEAD
=======
Temperature: 0.0
Dataset Path: data/security_logs.csv
>>>>>>> cdf477d6b3713a60db70cfacdf4b4b7d4d37702c

============================================================
# Security Incident Report

## Summary
<<<<<<< HEAD
- **High Severity**: 20
- **Medium Severity**: 1  
- **Low Severity**: 31

## High Severity Findings
- **Privilege Escalation** | user=adoyle ip=23.195.123.128
- **Brute Force Login** | user=jsmith ip=185.231.112.45
=======
- **High Severity**: 2
- **Medium Severity**: 1
- **Low Severity**: 0

## High Severity Findings

- **Privilege Escalation**
  - User: admin
  - IP: 192.168.1.100
  - Rule: privilege_escalation

- **Large Off-hours Download**
  - User: user123
  - IP: 10.0.0.50
  - Rule: offhours_large_download
>>>>>>> cdf477d6b3713a60db70cfacdf4b4b7d4d37702c

## Recommended Actions
🚨 IMMEDIATE ACTIONS:
- Isolate affected systems
- Reset compromised account passwords
- Block malicious IP addresses at firewall
<<<<<<< HEAD
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
=======
- Initiate incident response procedures
============================================================
```

### Agent Reasoning Display
```
🤖 AGENT REASONING PROCESS
============================================================
1. Ingest ReAct agent processed data/security_logs.csv with data quality score: 0.95
2. Detect ReAct agent analyzed 150 events and found 3 anomalies using pattern and anomaly detection tools
3. Classify ReAct agent assessed 3 anomalies with risk scoring and context enrichment using specialized tools
4. Report ReAct agent generated comprehensive report with 3 findings and 8 recommended actions using specialized tools

📊 AGENT CONFIDENCE SCORES:
   ingest: 0.95
   detect: 0.82
   classify: 0.78
   report: 0.90

🧠 MEMORY STATUS:
   Investigation history: 5 entries
   Learned patterns: 12 patterns
```

## 🛠️ Configuration Options

### Environment Variables
```bash
# Required for AI features (optional for basic functionality)
OPENAI_API_KEY=your_openai_api_key

# Optional configuration
MODEL_NAME=gpt-4o-mini          # AI model to use
TEMPERATURE=0.0                 # AI creativity level (0.0 = deterministic)
DATA_PATH=data/security_logs.csv # Default log file path
```

### Command Line Options
```bash
python -m src.incident_agents.run [OPTIONS]

Options:
  --logs PATH              Path to security_logs.csv
  --out PATH               Output path for report (e.g., reports/incident_report.md)
  --show-reasoning         Display agent reasoning process
  --help                   Show help message
>>>>>>> cdf477d6b3713a60db70cfacdf4b4b7d4d37702c
```

## 📁 Project Structure

```
ai-incident-response-agents2/
<<<<<<< HEAD
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
=======
├── 📁 data/                          # Sample data files
│   ├── security_logs.csv             # Sample security logs
│   └── threat_intel.json             # Threat intelligence data
├── 📁 src/incident_agents/           # Main source code
│   ├── 📁 nodes/                     # Agent nodes
│   │   ├── ingest.py                 # Data ingestion agent
│   │   ├── detect.py                 # Threat detection agent
│   │   ├── classify.py               # Risk classification agent
│   │   └── report.py                 # Report generation agent
│   ├── 📁 tools/                     # Specialized AI tools
│   │   ├── detection_tools.py        # Threat detection tools
│   │   ├── intel.py                  # Threat intelligence tools
│   │   ├── parsers.py                # Data parsing tools
│   │   └── reporting_tools.py        # Report generation tools
│   ├── app.py                        # Gradio web interface
│   ├── config.py                     # Configuration management
│   ├── graph.py                      # Workflow graph definition
│   ├── run.py                        # Main CLI execution script
│   └── state.py                      # State management
├── 📁 tests/                         # Test files
├── 📁 reports/                       # Generated reports
├── run_gradio_app.py                 # Gradio app launcher
├── requirements.txt                  # Python dependencies
├── README.md                         # Basic documentation
└── README_DETAILED.md                # Comprehensive documentation
```

## 🔧 Customization

### Adding New Detection Rules
Edit `src/incident_agents/nodes/detect.py`:
```python
def detect_anomalies(events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    anomalies = []
    
    # Your new rule here
    for e in events:
        if e["event_type"] == "your_event_type" and your_condition:
            anomalies.append({
                "rule": "your_rule_name",
                "user": e["user"],
                "ip": e["source_ip"],
                "details": "your_details"
            })
    
    return anomalies
```

### Adding New AI Tools
Create new tools in `src/incident_agents/tools/`:
```python
from langchain.tools import tool

@tool
def your_new_tool(input_data: str) -> Dict[str, Any]:
    """Description of what your tool does"""
    # Your tool logic here
    return {"result": "your_result"}
```

### Modifying Risk Assessment
Edit `src/incident_agents/nodes/classify.py`:
```python
def classify_findings(anomalies: List[Dict[str, Any]], events: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    # Your custom risk assessment logic here
    pass
```

## 🧪 Testing

### Run Tests
```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_graph_smoke.py
```

### Smoke Test
```bash
# Quick functionality test
python tests/test_graph_smoke.py
```

## 🚨 Troubleshooting

### Common Issues

**1. OpenAI API Key Not Set**
```
OpenAI API Key: ❌ Not set
```
**Solution**: Add your API key to `my_env.env` or run without AI features (system will use fallback methods)

**2. Import Errors**
```
ModuleNotFoundError: No module named 'langchain'
```
**Solution**: Install dependencies with `pip install -r requirements.txt`

**3. File Not Found**
```
FileNotFoundError: [Errno 2] No such file or directory: 'data/security_logs.csv'
```
**Solution**: Ensure the data file exists or specify correct path with `--logs`

**4. Memory Issues**
```
MemoryError: Unable to allocate array
```
**Solution**: Reduce batch size or use smaller log files

### Debug Mode
```bash
# Enable verbose logging
export DEBUG=1
python -m src.incident_agents.run --show-reasoning
```

## 🤝 Contributing

### Development Setup
```bash
# Clone repository
git clone <repository-url>
cd ai-incident-response-agents2

# Create virtual environment
python -m venv incident_agents_env
incident_agents_env\Scripts\activate   # Windows

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If available
```

### Code Style
- Follow PEP 8 guidelines
- Use type hints
- Add docstrings to functions
- Write tests for new features

### Pull Request Process
1. Fork the repository
2. Create feature branch
3. Make changes with tests
4. Submit pull request with description

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built with LangGraph for agent orchestration
- Uses OpenAI GPT models for AI capabilities
- Inspired by modern incident response practices
- Designed for educational and demonstration purposes

## 📞 Support

For questions, issues, or contributions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review the code examples in this README

---

**🎯 Perfect for:**
- Cybersecurity professionals learning AI
- Incident response teams
- Security operations centers (SOC)
- Educational demonstrations
- YouTube content creation
- Research and development

**🚀 Key Benefits:**
- Automated threat detection
- AI-powered analysis
- Professional reporting
- Memory and learning
- Robust fallback systems
- Easy customization

