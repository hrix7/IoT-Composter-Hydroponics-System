# IoT Composter and Hydroponics System

I contributed to this undergraduate engineering project at Adamas University as part of a 10-member team. We combined a compact 3D-printed waste-composting unit with a hydroponic growing system and used sensors to monitor the conditions needed for operation.

## Work completed

- Helped develop the system concept linking organic-waste processing with hydroponic cultivation.
- Integrated temperature, pH, and electrical-conductivity measurements.
- Used a thermocouple for temperature monitoring.
- Contributed to the 3D-printed enclosure and component layout.
- Defined a web/IoT monitoring workflow for viewing sensor status.
- Organized sensor readings into ranges that could trigger status flags or operator actions.
- Worked across mechanical design, sensing, electronics, and team coordination.

## System features

- 3D-printed compact structure.
- Temperature, pH, and conductivity monitoring.
- Separate checks for composting and hydroponic conditions.
- JSON-compatible sensor records.
- Rule-based status and recommended-action outputs.

## Repository code

- `src/sensor_monitor.py` evaluates a single reading against configured operating ranges.
- `src/control_rules.py` evaluates a time-stamped sensor record and returns clear operator actions.
- `examples/reading.json` demonstrates the input structure.
- `docs/ARCHITECTURE.md` describes the sensing and data-flow architecture.

## Run the tools

```bash
python src/sensor_monitor.py --temperature 25 --ph 6.1 --ec 1.4
python src/control_rules.py examples/reading.json
```

## Tools

IoT, sensors, thermocouple, pH, electrical conductivity, 3D printing, CAD, web monitoring, Python.

## Scope

The public code reconstructs the monitoring logic with example data. Original team hardware files are included only if ownership and sharing permission are clear.

## Author and Project Setting

**Author:** Hritika Adhikary  
**Project:** Undergraduate Biomedical Engineering Team Project  
**Institution:** Adamas University, Kolkata, India  
**Period:** 2022

## Rights

Copyright (c) 2026 Hritika Adhikary. All rights reserved. See [LICENSE](LICENSE).
