from src.retrieval import simple_retrieve

class LearningPathCuratorAgent:
    name = "Learning Path Curator Agent"

    def run(self, role: str, certification: dict) -> dict:
        query = f"{role} {certification['id']} {' '.join(certification['skills'])}"
        docs = simple_retrieve(query)
        return {
            "agent": self.name,
            "recommended_skills": certification["skills"],
            "recommended_hours": certification["recommended_hours"],
            "sources": [doc["source"] for doc in docs],
            "summary": (
                f"For a {role} preparing for {certification['id']}, focus on "
                f"{', '.join(certification['skills'])}. Target at least "
                f"{certification['recommended_hours']} study hours."
            )
        }
