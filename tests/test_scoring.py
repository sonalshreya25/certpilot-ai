from src.scoring import readiness_score

def test_ready_status():
    result = readiness_score(practice_score=82, hours_studied=25, recommended_hours=20, focus_hours=18)
    assert result["status"] == "Ready"

def test_at_risk_status():
    result = readiness_score(practice_score=50, hours_studied=5, recommended_hours=20, focus_hours=5)
    assert result["status"] == "At Risk"
