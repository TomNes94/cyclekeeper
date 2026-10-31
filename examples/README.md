# Examples

- [`python_emit.py`](python_emit.py) is a dependency-free Python 3 script that prints a small valid `cyclekeeper.json` example to stdout. Run `python3 python_emit.py > cyclekeeper.json`.
- Run [`test_python_emit.py`](test_python_emit.py) with `python3 test_python_emit.py`. It parses the output and verifies that the goal reference works and the intentional wake gap remains intact.

Wake numbers are explicit, and the sample skips wake 2 to demonstrate the format's rule: gaps are meaningful; emitters must not invent missing sessions. See [`../FORMAT.md`](../FORMAT.md) for the format contract.
