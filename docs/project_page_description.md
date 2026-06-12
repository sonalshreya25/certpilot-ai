# Project Page Description

CertPilot AI is a multi-agent certification readiness coach designed for enterprise learning and workforce upskilling.

The system helps organizations manage technical certification preparation by combining role-based learning paths, capacity-aware study plans, grounded practice assessments, and manager-level readiness insights. A learner selects their role, target certification, practice score, study hours, and synthetic workload profile. CertPilot AI then orchestrates five specialized agents to produce a complete readiness workflow.

The Learning Path Curator Agent maps the learner’s role and certification goal to required skills and approved learning materials. The Study Plan Generator Agent creates a realistic study plan based on recommended hours, current progress, and available focus time. The Engagement Agent recommends supportive reminders and study windows using synthetic work signals. The Assessment Agent generates grounded practice questions and readiness scoring. The Manager Insights Agent summarizes team-level risk and recommendations without exposing sensitive personal information.

CertPilot AI uses synthetic data only, including fictional learner IDs, employee IDs, team IDs, certification goals, workload signals, and learning documents. The project does not include real employee data, customer data, PII, secrets, or confidential information.

The architecture is aligned with Microsoft Foundry-style multi-agent orchestration. It includes a Foundry IQ-style knowledge grounding layer, a Work IQ-inspired workload context layer, and a Fabric IQ-inspired semantic model that connects roles, certifications, skills, thresholds, readiness scores, and study recommendations.

Technologies used:
- Python
- Streamlit
- JSON synthetic datasets
- Markdown synthetic knowledge base
- Local multi-agent orchestration
- GitHub for source control
- Microsoft Foundry-ready architecture

The goal of CertPilot AI is to demonstrate how reasoning agents can collaborate across knowledge retrieval, planning, assessment, and business insights to support safe, explainable, and demoable enterprise learning workflows.
