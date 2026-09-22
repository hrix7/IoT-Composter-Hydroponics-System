"""Evaluate composter/hydroponics readings against configurable ranges."""
from __future__ import annotations
import argparse
import json
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class Reading:
    temperature_c: float
    ph: float
    ec_ms_cm: float

def evaluate(reading: Reading) -> dict:
    checks = {
        "temperature_ok": 18.0 <= reading.temperature_c <= 32.0,
        "ph_ok": 5.5 <= reading.ph <= 6.8,
        "ec_ok": 0.8 <= reading.ec_ms_cm <= 2.4,
    }
    return {"reading": asdict(reading), "checks": checks, "all_ok": all(checks.values())}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--temperature", type=float, required=True)
    parser.add_argument("--ph", type=float, required=True)
    parser.add_argument("--ec", type=float, required=True)
    args = parser.parse_args()
    print(json.dumps(evaluate(Reading(args.temperature, args.ph, args.ec)), indent=2))
