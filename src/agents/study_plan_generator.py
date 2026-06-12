class StudyPlanGeneratorAgent:
    name = "Study Plan Generator Agent"

    def run(self, certification: dict, work_signal: dict, current_hours: int) -> dict:
        remaining_hours = max(certification["recommended_hours"] - current_hours, 0)
        focus_hours = work_signal.get("focus_hours_per_week", 10)
        preferred_slot = work_signal.get("preferred_learning_slot", "Morning")

        if remaining_hours == 0:
            plan = ["Take a final readiness assessment.", "Review weak areas for 30 minutes daily."]
        else:
            weekly_capacity = max(3, min(focus_hours, 8))
            weeks = max(1, round(remaining_hours / weekly_capacity))
            plan = [
                f"Use {preferred_slot.lower()} study blocks when possible.",
                f"Complete approximately {weekly_capacity} focused study hours per week.",
                f"Finish remaining {remaining_hours} hours over about {weeks} week(s).",
                "End each week with a short practice assessment.",
                "Spend extra time on skills with low confidence."
            ]

        return {
            "agent": self.name,
            "remaining_hours": remaining_hours,
            "study_plan": plan
        }
