class EngagementAgent:
    name = "Engagement Agent"

    def run(self, work_signal: dict) -> dict:
        meetings = work_signal.get("meeting_hours_per_week", 0)
        focus = work_signal.get("focus_hours_per_week", 0)
        slot = work_signal.get("preferred_learning_slot", "Morning")

        if meetings > 20:
            reminder_style = "Light-touch reminders because meeting load is high."
        elif focus >= 15:
            reminder_style = "Regular reminders with weekly progress checkpoints."
        else:
            reminder_style = "Short reminders and micro-study sessions."

        return {
            "agent": self.name,
            "recommended_slot": slot,
            "reminder_strategy": reminder_style,
            "work_context_summary": f"{meetings} meeting hours/week, {focus} focus hours/week."
        }
