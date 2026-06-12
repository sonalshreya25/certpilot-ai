# 5-Minute Demo Video Script

## 0:00–0:30 — Intro
Hi, I’m Sonal Shreya, and this is CertPilot AI, a multi-agent certification readiness coach built for the Microsoft Agents League Reasoning Agents challenge.

The problem is that organizations often struggle to manage certification readiness across teams. Employees need personalized study plans, while managers need safe, privacy-conscious visibility into progress and risk.

## 0:30–1:15 — Architecture
CertPilot AI uses five specialized agents:
1. Learning Path Curator Agent
2. Study Plan Generator Agent
3. Engagement Agent
4. Assessment Agent
5. Manager Insights Agent

The workflow is orchestrated locally in Python and designed to align with Microsoft Foundry patterns. The system uses a Foundry IQ-style grounding layer, Work IQ-inspired workload context, and a Fabric IQ-inspired semantic model.

## 1:15–2:30 — Demo Input
In the app, I select:
- Role: Cloud Engineer
- Certification: AZ-204
- Employee ID: EMP-001
- Practice score: 67
- Hours studied: 18

This is all synthetic data. No real employee data, customer data, PII, or confidential information is used.

## 2:30–3:45 — Agent Outputs
The Learning Path Curator maps the role to required skills and grounded learning sources.
The Study Plan Generator creates a capacity-aware study plan.
The Engagement Agent uses synthetic workload signals like meeting hours and focus hours.
The Assessment Agent generates practice questions and readiness scoring.
The Manager Insights Agent summarizes risk areas and next actions.

## 3:45–4:30 — Safety and Reliability
The system is designed with responsible AI principles:
- Synthetic data only
- No secrets in the repository
- Grounding source names shown
- Human review expected for real workforce decisions
- Supportive recommendations instead of punitive decisions

## 4:30–5:00 — Closing
CertPilot AI demonstrates multi-agent reasoning, grounded knowledge, semantic business understanding, and safe enterprise learning workflows. Future improvements include direct Microsoft Foundry integration, stronger evaluation, and hosted deployment.
