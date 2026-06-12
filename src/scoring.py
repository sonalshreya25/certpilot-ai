from typing import Dict, List

def readiness_score(practice_score: int, hours_studied: int, recommended_hours: int, focus_hours: int) -> Dict:
    score = 0
    reasons: List[str] = []

    if practice_score >= 75:
        score += 45
    else:
        score += max(0, int(practice_score * 0.45))
        reasons.append("Practice score is below the 75% readiness threshold.")

    hour_ratio = min(hours_studied / max(recommended_hours, 1), 1)
    score += int(hour_ratio * 35)
    if hours_studied < recommended_hours:
        reasons.append("Study hours are below the recommended certification target.")

    if focus_hours >= 15:
        score += 20
    elif focus_hours >= 10:
        score += 12
        reasons.append("Focus hours are moderate; schedule needs to be realistic.")
    else:
        score += 6
        reasons.append("Focus hours are low; learner may need shorter study blocks.")

    if score >= 80:
        status = "Ready"
    elif score >= 65:
        status = "Borderline"
    else:
        status = "At Risk"

    return {"score": score, "status": status, "reasons": reasons}
