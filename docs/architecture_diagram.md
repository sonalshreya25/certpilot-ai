# Architecture Diagram

Use this Mermaid diagram in your README or convert it to an image for the submission.

```mermaid
flowchart TD
    A[User / Learner Input] --> B[CertPilot Orchestrator]

    B --> C[Learning Path Curator Agent]
    B --> D[Study Plan Generator Agent]
    B --> E[Engagement Agent]
    B --> F[Assessment Agent]
    B --> G[Manager Insights Agent]

    H[Foundry IQ-style Knowledge Base<br/>Synthetic Markdown Docs] --> C
    H --> F

    I[Fabric IQ-inspired Semantic Model<br/>Roles, Certifications, Skills, Thresholds] --> C
    I --> D
    I --> F
    I --> G

    J[Work IQ-inspired Context<br/>Meeting Hours, Focus Hours, Preferred Slot] --> D
    J --> E
    J --> G

    C --> K[Role-Based Learning Path]
    D --> L[Capacity-Aware Study Plan]
    E --> M[Engagement Strategy]
    F --> N[Readiness Score + Grounded Questions]
    G --> O[Manager Risk Insights]

    K --> P[Final CertPilot AI Report]
    L --> P
    M --> P
    N --> P
    O --> P
```

## Explanation

- The orchestrator coordinates specialized agents.
- The Foundry IQ-style knowledge layer grounds learning-path and assessment outputs.
- The Work IQ-inspired context layer adapts study scheduling to synthetic work signals.
- The Fabric IQ-inspired semantic layer represents business meaning: role, certification, skills, readiness score, thresholds, and study recommendations.
- All data is synthetic and safe for public demo use.
