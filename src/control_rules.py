"""Convert the sensor measurements from my IoT project into operator actions."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

RANGES = {
    "temperature_c": (18.0, 32.0),
    "ph": (5.5, 6.8),
    "ec_ms_cm": (0.8, 2.4),
}

def evaluate(payload: dict) -> dict:
    actions = []
    checks = {}
    for field, (low, high) in RANGES.items():
        if field not in payload:
            raise ValueError(f"Missing sensor field: {field}")
        value = float(payload[field])
        checks[field] = {"value": value, "low": low, "high": high, "ok": low <= value <= high}
        if value < low:
            actions.append(f"Review {field}: below the configured range.")
        elif value > high:
            actions.append(f"Review {field}: above the configured range.")
    return {"timestamp": payload.get("timestamp"), "checks": checks,
            "status": "within_range" if not actions else "attention_required",
            "actions": actions or ["Continue monitoring."]}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("json_file")
    args = parser.parse_args()
    data = json.loads(Path(args.json_file).read_text(encoding="utf-8"))
    print(json.dumps(evaluate(data), indent=2))
