"""Smoke test for the dependency-free example emitter."""
import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name("python_emit.py")
result = subprocess.run(
    [sys.executable, str(SCRIPT)],
    check=True,
    capture_output=True,
    text=True,
)
state = json.loads(result.stdout)
assert set(("goals", "journal")).issubset(state)
assert state["goals"] and state["journal"]
assert [entry["wake"] for entry in state["journal"]] == [1, 3]
assert state["journal"][0]["goal"] == state["goals"][0]["id"]
print("ok: valid JSON, linked goal, wake gap preserved")
