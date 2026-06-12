import json
from pathlib import Path
from typing import Any

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "synthetic"

def load_json(filename: str) -> Any:
    return json.loads((DATA_DIR / filename).read_text(encoding="utf-8"))

def get_certification(cert_id: str) -> dict:
    data = load_json("certifications.json")
    for cert in data["certifications"]:
        if cert["id"].lower() == cert_id.lower():
            return cert
    raise ValueError(f"Certification not found: {cert_id}")

def get_work_signal(employee_id: str) -> dict:
    for signal in load_json("work_signals.json"):
        if signal["employee_id"] == employee_id:
            return signal
    return {}
