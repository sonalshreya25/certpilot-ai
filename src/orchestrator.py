from src.data_loader import get_certification, get_work_signal
from src.agents.learning_path_curator import LearningPathCuratorAgent
from src.agents.study_plan_generator import StudyPlanGeneratorAgent
from src.agents.engagement_agent import EngagementAgent
from src.agents.assessment_agent import AssessmentAgent
from src.agents.manager_insights_agent import ManagerInsightsAgent

def run_certpilot_workflow(
    role: str,
    certification_id: str,
    employee_id: str,
    practice_score: int,
    hours_studied: int
) -> dict:
    certification = get_certification(certification_id)
    work_signal = get_work_signal(employee_id)

    curator = LearningPathCuratorAgent().run(role, certification)
    study_plan = StudyPlanGeneratorAgent().run(certification, work_signal, hours_studied)
    engagement = EngagementAgent().run(work_signal)
    assessment = AssessmentAgent().run(certification, practice_score, hours_studied, work_signal)

    result = {
        "input": {
            "role": role,
            "certification": certification_id,
            "employee_id": employee_id,
            "practice_score": practice_score,
            "hours_studied": hours_studied
        },
        "curator": curator,
        "study_plan": study_plan,
        "engagement": engagement,
        "assessment": assessment
    }
    result["manager_insights"] = ManagerInsightsAgent().run(result)
    return result
