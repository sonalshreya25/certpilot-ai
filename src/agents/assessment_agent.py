from src.scoring import readiness_score
from src.retrieval import simple_retrieve

class AssessmentAgent:
    name = "Assessment Agent"

    def run(self, certification: dict, practice_score: int, hours_studied: int, work_signal: dict) -> dict:
        readiness = readiness_score(
            practice_score=practice_score,
            hours_studied=hours_studied,
            recommended_hours=certification["recommended_hours"],
            focus_hours=work_signal.get("focus_hours_per_week", 0)
        )

        docs = simple_retrieve(f"{certification['id']} {' '.join(certification['skills'])}")
        questions = [
            f"Explain one real-world use case for {certification['skills'][0]}.",
            f"What risk might appear if a learner has low practice scores in {certification['skills'][1]}?",
            f"How would you validate readiness before attempting {certification['id']}?"
        ]

        return {
            "agent": self.name,
            "readiness": readiness,
            "practice_questions": questions,
            "sources": [doc["source"] for doc in docs]
        }
