# V270 Navigation Source Restore Lock

## Issue

The V270 navigation remained broken after the first repair attempt because the safest correction is not a DOM patch. The correct source of truth is the working V269 navigation implementation.

## Fix

This build restores navigation from:

```txt
V269_FINAL_UI_HARMONY_LOCK
```

and reapplies only the public release provenance / license / citation stamp.

## Hard lock

```txt
No DOM-level navigation reordering.
No post-render movement of Vue-owned nav nodes.
No modification to Vue nav click handlers.
No rewrite of setMode / setTab / activeModeTabs.
Navigation source: V269.
```

## Preserved Analyze order from V269 navModel

```txt
Runtime Evidence
Evidence State
Regime Map
Failure Timeline
Failure Boundary
Role Topology
Runtime Replay
Drift Evidence
Energetic Pressure
Noesis Evidence
```

## Provenance preserved

```txt
Fieldglass® Runtime Evidence Observatory
SubstrateX® Runtime Evidence Infrastructure
Recursive Science®
SubstrateX Public Research and Accountability License v1.0
Citation required
No provenance removal
```

## Generated

```txt
2026-05-30T02:04:02Z
```
