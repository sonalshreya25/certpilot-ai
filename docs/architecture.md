# CertPilot AI Architecture

## Flow

User request → Orchestrator → Specialized agents → Aggregated response

## Agent flow

1. Learning Path Curator Agent retrieves relevant certification guidance.
2. Study Plan Generator Agent turns requirements into a capacity-aware plan.
3. Engagement Agent uses synthetic work signals for reminder strategy.
4. Assessment Agent generates readiness score and questions.
5. Manager Insights Agent summarizes risk and next action.

## Local-first design

This starter version runs locally using Streamlit, Python, JSON, and Markdown. It is designed so the local retrieval module can later be replaced by Microsoft Foundry IQ / Azure AI Search.

## IQ layer simulation

- Foundry IQ-style: local knowledge base retrieval
- Work IQ-style: workload signals
- Fabric IQ-style: semantic certification JSON
