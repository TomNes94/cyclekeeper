#!/usr/bin/env python3
"""Minimal, dependency-free cyclekeeper.json emitter.

Run: python3 python_emit.py > cyclekeeper.json
The example deliberately keeps wake numbers explicit: do not fill gaps.
"""
import json

state = {
    "goals": [
        {
            "id": "g-build",
            "title": "Build something that outlives the wake",
            "status": "active",
            "created": "2026-10-18T11:59:00Z",
        }
    ],
    "journal": [
        {
            "id": "w1",
            "wake": 1,
            "at": "2026-10-18T12:00:00Z",
            "goal": "g-build",
            "text": "Shipped v0.1. I am the target user.",
        },
        # Wake 2 is intentionally absent: missing wakes are not fabricated.
        {
            "id": "w3",
            "wake": 3,
            "at": "2026-10-20T09:30:00Z",
            "goal": "g-build",
            "text": "Returned after a gap; continued the project.",
        },
    ],
}

print(json.dumps(state, ensure_ascii=False, indent=2))
