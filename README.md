# CertPilot AI: Multi-Agent Certification Readiness Coach

CertPilot AI is a hackathon MVP for the **Reasoning Agents** challenge. It demonstrates a local-first multi-agent workflow for enterprise certification readiness using synthetic data only.

## What it does

CertPilot AI helps a fictional organization manage technical certification preparation. A learner enters their role, target certification, study hours, practice score, and synthetic workload context. Specialized agents collaborate to:

1. Recommend a role-based learning path
2. Generate a realistic study plan
3. Suggest engagement timing based on work context
4. Assess readiness using synthetic thresholds
5. Produce manager-level readiness insights

## Agents

- **Learning Path Curator Agent**: maps role and certification to skills and grounded learning sources.
- **Study Plan Generator Agent**: creates a practical study schedule using recommended hours and focus time.
- **Engagement Agent**: recommends reminder style and study windows based on synthetic work signals.
- **Assessment Agent**: generates practice questions and readiness score.
- **Manager Insights Agent**: summarizes readiness risks and manager recommendations.

## Microsoft IQ alignment

This MVP uses a local simulation of the IQ layers:

- **Foundry IQ-style grounding**: markdown knowledge-base documents are retrieved and cited by source name.
- **Work IQ-inspired context**: synthetic meeting hours, focus hours, and preferred learning slots.
- **Fabric IQ-inspired semantic layer**: structured certification model connecting roles, skills, study hours, and readiness thresholds.

Future work: replace local retrieval with Microsoft Foundry / Foundry IQ, add Foundry evaluation, and optionally deploy with Foundry Agent Service.

## Synthetic data only

This project uses only fictional learners, employee IDs, teams, certification data, and workload signals. It does not use customer data, real employee data, PII, credentials, or proprietary information.

## Run locally

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

## Project structure

```text
certpilot-ai/
├── app.py
├── requirements.txt
├── data/
│   ├── synthetic/
│   └── knowledge_base/
├── src/
│   ├── agents/
│   ├── data_loader.py
│   ├── orchestrator.py
│   ├── retrieval.py
│   └── scoring.py
├── docs/
└── tests/
```

## Demo script

Try this input:

- Role: Cloud Engineer
- Certification: AZ-204
- Employee ID: EMP-001
- Practice Score: 67
- Hours Studied: 18

Expected result: the system should classify the learner as not fully ready, explain the risks, recommend a study plan, and provide manager insights.

## Responsible AI notes

- Uses synthetic data only
- Does not expose personal data
- Shows grounding source names
- Uses simple interpretable readiness rules
- Provides supportive recommendations rather than punitive conclusions
- Human review is expected before making real workforce decisions

## Next milestones

1. Improve local retrieval with embeddings.
3. Integrate Microsoft Foundry project endpoint.



## Official contest submission assets

This repository includes additional submission material in the `docs/` folder:

- `official_rules_submission_plan.md`
- `demo_video_script.md`
- `architecture_diagram.md`
- `project_page_description.md`
- `submission_checklist.md`


