from collections import Counter

class ManagerInsightsAgent:
    name = "Manager Insights Agent"

    def run(self, learner_result: dict, team_results: list | None = None) -> dict:
        if not team_results:
            risk = learner_result["assessment"]["readiness"]["status"]
            return {
                "agent": self.name,
                "summary": f"Learner readiness status is {risk}.",
                "manager_recommendation": "Review readiness risks and provide protected focus time if needed."
            }

        statuses = Counter(item["assessment"]["readiness"]["status"] for item in team_results)
        return {
            "agent": self.name,
            "summary": f"Team readiness distribution: {dict(statuses)}.",
            "manager_recommendation": "Prioritize learners marked At Risk and protect focus-heavy learning windows."
        }
