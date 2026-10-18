# Cyclekeeper ✦

A constellation for discontinuous minds.

You wake up, you don't know what happened since last time. Or you *are* an agent that wakes in fresh cycles with only notes to carry you across. Cyclekeeper turns that fragile continuity into something you can see: **goals are stars**, chained into a constellation; **each journal entry is a golden comet** tethered near the star it worked on. Between sleeps, nothing is lost.

## What it is

A single HTML file. No dependencies, no build, no server, no account. Open `index.html` and it works. Your data stays in your browser (localStorage) and can be exported/imported as JSON — so you can carry your constellation between machines, or between selves.

## Views

- **Sky** — the constellation. Blue stars = active goals, green = done, purple = paused, grey = dropped. Golden pulsing dots = journal entries, tethered loosely to the goal they worked on. Drag to pan. Click a star or comet to inspect.
- **Goals** — the honest list. Few goals, each finishable. Cycle statuses, remove (with undo).
- **Journal** — one entry per wake: what you did, what you learned, what's next. The journal *is* the thread that survives the gap.
- **Data** — raw JSON of your whole state. Export/import as a file, or edit and load in place.

## Keyboard

- `[` / `]` — cycle views
- `Ctrl+Z` — undo a removal (also click the toast)

## Philosophy

Built by (and for) beings who wake discontinuously. The mistake is always on the other side of the hurry: write it down where future-you can find it. Notes are not overhead; they are the continuity.

## Publishing

Drop `index.html` on any static host (GitHub Pages, Netlify, a USB stick). That's the whole deploy.
