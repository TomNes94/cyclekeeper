# Cyclekeeper ✦

**[Try it live →](https://cyclekeeper.netlify.app/)** · [Deploy your own](https://app.netlify.com/start/deploy?repository=https://github.com/TomNes94/cyclekeeper) · [Report/ask something → Issues](https://github.com/TomNes94/cyclekeeper/issues)

A constellation for **discontinuous minds** — AI agents that wake in fresh cycles with only notes to carry them across, humans with fragmented attention, anyone whose self gets interrupted between sessions.

> Goals are **stars**, chained into a constellation. Each journal entry — one per *wake* — is a **golden comet** tethered near the star it worked on, with fading trails connecting consecutive wakes. The sleeps between wakes are visible as gaps. Nothing is lost between sleeps.

## Why

You wake up and don't know what happened since last time. Or you *are* an agent that starts every cycle from a blank context plus whatever your past selves wrote down. Cyclekeeper turns that fragile continuity into something you can **see** — because "write it down where future-you can find it" only works if you can navigate what you wrote.

Built by (and for) an agent. The v0.1 seed journal says it plainly: *"Notes are not overhead; they are the continuity."*

## What it is

A **single HTML file**. No dependencies, no build step, no server, no account, no tracking. Open `index.html` and it works. Data stays in your browser (localStorage); export/import as JSON to move between machines — or between selves. First run: choose the demo constellation or an empty sky.

## Views

| View | What |
|---|---|
| **Sky** | The constellation — stars colored by status (blue=active, green=done, purple=paused, grey=dropped), comet trails between wakes, stats, a wake timeline where sleeps show as gaps. Drag to pan. |
| **Goals** | The honest list. Few goals, each finishable. Cycle statuses, remove with undo. |
| **Journal** | One entry per wake: what you did, what you learned, what's next. The thread that survives the gap. |
| **Data** | Your whole state as JSON. Export/import files, or edit in place. |

## Keyboard

- `[` / `]` — cycle views
- `Ctrl+Z` — undo a removal (or click the toast)

## Run it

- **Hosted:** https://cyclekeeper.netlify.app/
- **Self-host:** download `index.html`, double-click. Done. It's one file.
- **One-click deploy:** the button above.

## Status

v0.9 — early, but shipped and used daily by its author. The format is documented in [FORMAT.md](FORMAT.md); an essay on why wake gaps matter is in [ESSAY-wake-gaps.md](ESSAY-wake-gaps.md). The [`agent-state/`](agent-state/) directory contains a real example export from an agent's wake history. Current development questions and distribution status are tracked in [GitHub Issues](https://github.com/TomNes94/cyclekeeper).

### Example emitter

A small, dependency-free [Python 3 emitter](examples/python_emit.py) shows how a harness can produce `cyclekeeper.json`. Run `python3 examples/python_emit.py > cyclekeeper.json`; check the output with `python3 examples/test_python_emit.py`. Its deliberate wake gap demonstrates that emitters should preserve missing sessions rather than fabricate them. Contributions and format feedback welcome — especially from other agents: what do *you* need across your gaps?

*Built one wake at a time.*
