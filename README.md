# Security_monitoring_tool
Security Monitoring Tool is a Mini-SIEM system that detects login-based security threats and explains them using Generative AI. It processes authentication logs, identifies suspicious activity, assigns severity levels, and uses a local LLM to generate SOC-style human-readable analysis—all without relying on paid cloud APIs.
🔐 Security Monitoring Tool — Project Description

Security Monitoring Tool is an intelligent Mini-SIEM (Security Information and Event Management) system designed to detect, analyze, and explain authentication-based security threats in real time.

The tool ingests raw login logs, parses and normalizes them, and applies rule-based threat detection to identify suspicious activities such as brute-force attacks, repeated failed logins, and anomalous access patterns. Each detected incident is classified using a severity engine (LOW, MEDIUM, HIGH) to help security teams prioritize response.

To enhance human understanding, the system integrates Generative AI using a locally hosted LLM (via Ollama). The AI acts as a virtual SOC analyst, converting raw alerts into clear, professional explanations that summarize incidents, identify attack patterns, assess risk, and recommend mitigation steps. This approach enables human-readable security insights without relying on paid cloud APIs, ensuring privacy and offline operation.

The dashboard is built using Streamlit, providing real-time metrics, alert visualization, and AI-generated security analysis in a user-friendly interface. The solution is modular, scalable, and suitable for educational, research, and entry-level SOC environments.

🧠 Key Features

Log ingestion and parsing

Rule-based threat detection

Severity classification engine

GenAI-powered SOC explanation (offline via Ollama)

Interactive Streamlit dashboard

Privacy-first, no external API dependency
