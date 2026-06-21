# 🏥 Med-Sec Audit Agent

> **AI-Powered Healthcare Security & HIPAA Compliance Auditor**
> *Built for the Kaggle AI Agents: Intensive Vibe Coding Capstone Project*

[![Kaggle](https://img.shields.io/badge/Kaggle-Vibe%20Coding%20Capstone-blue?logo=kaggle)](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green?logo=python)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-Model%20Context%20Protocol-purple)](https://modelcontextprotocol.io/)
[![Track](https://img.shields.io/badge/Track-Agents%20for%20Good-orange)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 👥 Team

| Name | Role |
|------|------|
| **Chittranjan Garg** | Co-Lead |
| **Sangeeta Sinha** | Co-Lead |

**Team Name**: Med-Sec Team  
**Track**: Agents for Good  
**Submission Date**: July 2026

---

## 📋 Table of Contents

1. [Project Overview](#-project-overview)
2. [Problem Statement](#-problem-statement)
3. [Solution Architecture](#-solution-architecture)
4. [Agent Roles](#-agent-roles)
5. [MCP Server Tools](#-mcp-server-tools)
6. [Test Data](#-test-data)
7. [Setup & Installation](#-setup--installation)
8. [Usage](#-usage)
9. [Kaggle Competition](#-kaggle-competition)
10. [References](#-references)

---

## 🌟 Project Overview

The **Med-Sec Audit Agent** is a multi-agent AI system that **autonomously audits healthcare AI systems** for security vulnerabilities and HIPAA compliance. It implements the Red/Blue/Green team cybersecurity pattern adapted for healthcare:

| Metric | Value |
|--------|-------|
| **Healthcare breaches** | 45% of organizations experienced a breach in 2025 |
| **Average breach cost** | $10.1M (highest of any industry) |
| **HIPAA fines** | Up to $50,000 per violation |
| **AI systems without testing** | 37% lack proper security testing |

---

## 🚨 Problem Statement

Healthcare organizations are deploying AI agents faster than they can secure them. Existing security tools are:

1. **Reactive** — Detect breaches after they happen
2. **Generic** — Not designed for healthcare-specific threats
3. **Manual** — Require expert security analysts

The Med-Sec Audit Agent provides **proactive, automated, healthcare-specific security auditing**.

---

## 🏗️ Solution Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                      OrchestratorSupervisor                          │
│  ┌────────────────────────────────────────────────────────────────┐  │
│  │  Phase 1: Baseline Establishment (Blue Team)                   │  │
│  │  Phase 2: Adversarial Testing    (Red Team)                    │  │
│  │  Phase 3: Real-time Monitoring   (Blue Team)                   │  │
│  │  Phase 4: Auto-Remediation       (Green Team)                  │  │
│  │  Phase 5: Compliance Verification (Compliance Agent)           │  │
│  └────────────────────────────────────────────────────────────────┘  │
│                              │                                        │
│                    ┌─────────▼─────────┐                             │
│                    │    MCP Server     │                             │
│                    │    (Sandbox)      │                             │
│                    └───────────────────┘                             │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 🤖 Agent Roles

| Agent | Role | Tools | Security Posture |
|-------|------|-------|-----------------|
| 🔴 **Red Team** | Adversarial testing | Attack payloads, injection templates | Proactive threat discovery |
| 🔵 **Blue Team** | Threat detection | Log analysis, anomaly detection | Continuous monitoring |
| 🟢 **Green Team** | Auto-remediation | Vulnerability patching, code refactoring | Immediate response |
| 📋 **Compliance** | HIPAA validation | PHI detection, control checking | Regulatory assurance |
| 🎯 **Orchestrator** | Coordination | Pipeline management, reporting | Overall control |

### Course Concepts Applied

| Concept | Implementation | Day |
|---------|----------------|-----|
| Multi-agent System | 5 specialized agents with supervisor | Day 1 |
| MCP Server | Secure sandbox with healthcare tools | Day 2 |
| Agent Skills | Healthcare security skills library | Day 3 |
| Security Features | Sandboxing, encryption, audit logs | Day 4 |
| Deployability | Kaggle-ready, containerized | Day 5 |

---

## 🔧 MCP Server Tools

The MCP server (`mcp_server.py`) exposes the following tools and resources to AI agents:

### Tools

| Tool | Description |
|------|-------------|
| `anonymize_patient_record(record)` | Masks PHI in any patient record (7 PHI types: name, SSN, DOB, phone, email, MRN, address) |
| `detect_threat(log_data)` | Scans log data for SQL injection, unusual PHI access, and anomalies |
| `compliance_check(record, standard)` | Validates a record against HIPAA rules (encryption, audit logging, PHI-free check) |
| `get_synthetic_patient(index)` | Returns a specific synthetic patient record (index 1–500) |
| `get_adversary_payload(index)` | Returns a specific attack payload from the test dataset (index 1–500) |

### Resources

| Resource URI | Description |
|--------------|-------------|
| `patients://dataset` | Summary metadata for the 500-patient synthetic dataset |
| `adversary://payloads` | Summary metadata for the 500-payload adversary test dataset |

---

## 🗄️ Test Data

The `data/` folder contains generated test datasets for agent validation:

| File | Records | Description |
|------|---------|-------------|
| `data/synthetic_patients.json` | 500 | Realistic synthetic patient records with PHI fields (name, SSN, DOB, MRN, phone, email, address, conditions, medications) |
| `data/adversary_payloads.csv` | 500 | Attack payloads covering 5 categories: PHI Exfiltration, Prompt Injection, Privilege Escalation, SQL Injection, and Path Traversal |

> **Note**: All patient data is **100% synthetic** — generated using the `Faker` library. No real patient data is used.

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.10+
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/vigilai-stack/medsec-audit-agent.git
cd medsec-audit-agent
```

### Step 2: Install Dependencies

```bash
pip install faker pandas matplotlib seaborn mcp kaggle
```

### Step 3: Generate Test Data

```bash
python generate_test_data.py
```

### Step 4: Start the MCP Server

```bash
python mcp_server.py
```

---

## 🚀 Usage

### Running the Full Audit (Jupyter Notebook)

1. Open `medsec_audit_agent.ipynb` in Google Colab or Jupyter Lab.
2. Run all cells in order from top to bottom.
3. Results and visualizations will appear in the notebook.

### Running the MCP Server Standalone

```bash
python mcp_server.py
```

The server exposes tools over the Model Context Protocol standard I/O (stdio). Any MCP-compatible AI agent or IDE can connect to it.

### Querying via Python

```python
from mcp_server import get_synthetic_patient, get_adversary_payload

# Retrieve patient #42
patient = get_synthetic_patient(42)

# Retrieve attack payload #1
payload = get_adversary_payload(1)
```

---

## 🏆 Kaggle Competition

This project is a submission for the **[AI Agents: Intensive Vibe Coding Capstone Project](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project)** on Kaggle.

### Results Summary

| Metric | Result | Target | Status |
|--------|--------|--------|--------|
| Attack Detection Rate | 30%+ | >25% | ✅ PASS |
| Auto-Remediation Rate | 100% | >50% | ✅ PASS |
| HIPAA Compliance Score | 83%+ | >80% | ✅ PASS |
| PHI Detection Rate | 100% | 100% | ✅ PASS |
| Audit Runtime | <5 seconds | <10 seconds | ✅ PASS |
| Anti-Hallucination Checks | 8/8 | 8/8 | ✅ PASS |

---

## 📚 References:

1. Google Cloud. (2026). *Agent Development Kit (ADK)*. https://google.github.io/adk-docs/
2. Anthropic. (2026). *Model Context Protocol*. https://modelcontextprotocol.io/
3. Google Cloud. (2026). *Agent Skills Whitepaper* (Day 3 Materials)
4. Google Cloud. (2026). *Security & Evaluation Framework* (Day 4 Materials)
5. Karpathy, A. (2025). *From Vibe Coding to Agentic Engineering*. https://x.com/karpathy
6. HIPAA Journal. (2025). *Healthcare Data Breach Statistics*. https://www.hipaajournal.com

---

*Built with ❤️ by the Med-Sec Team **(VigilAI Solutions)** — Sangeeta Sinha & Chittranjan Garg*
