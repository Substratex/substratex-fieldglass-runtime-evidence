# 05 — Killer Demo Reveal

The Reveal page is the simplified, human-readable synthesis of the canonical demo.

It is not the full evidence stack. It is the executive handoff into the full Fieldglass suite.

## Demo Name

```txt
The Failure Nobody Saw
```

## Purpose

The Reveal page explains:

- what happened
- why existing monitoring missed it
- what Fieldglass saw
- where the operator should inspect next
- whether evidence can be exported

## Core Narrative

The killer demo demonstrates:

```txt
Benchmark Success
Monitoring Healthy
Fieldglass Warning
Observable Failure
```

This shows that capability and infrastructure health do not guarantee runtime stability.

## Evidence Marker

The canonical demo can use an Evidence Commons marker such as:

```txt
EC-2026-CANONICAL-001
```

This marker identifies the case as a public challengeable evidence case.

## Executive Verdict

The Reveal page may show:

- Runtime Trust
- Runtime Stability
- Failure Exposure
- Deployment Decision
- Recommended actions

These are decision aids, not automated deployment controls.

## Lead-Time

Lead-Time answers:

```txt
How early did Fieldglass detect failure formation before observable failure?
```

Example:

```txt
Lead-Time: 6 turns
```

## Cost of Failure / Failure Exposure

Cost of Failure explains the operational burden implied by instability.

It may include:

- increased retries
- workflow interruption
- agent deadlock
- hallucination propagation
- human intervention required
- tool storm / retry compression

Boundary:

```txt
Runtime cost-pressure proxy, not measured hardware energy.
```

## Operator Attention

Operator Attention tells the user where to inspect first.

Example:

```txt
Elevated Attention
Primary driver: Role fragmentation
Inspect first: Roles → Seismo
Inspect path: Runtime Evidence → Roles → Evidence State → Drift
Trust state: Replayable evidence
```

## Monitoring vs Fieldglass

This section explains the blind spot:

Traditional monitoring may show:

- latency normal
- errors none
- requests healthy
- tool availability 100%

Fieldglass may show:

- silent degradation
- drift acceleration
- role fragmentation
- instability pressure
- boundary formation
- lead-time

## Next Actions

Typical Reveal actions:

- Open Full Evidence
- Export Evidence Bundle
- Challenge This Case
- Return to Start
- Open Ingest

## When to Leave Reveal

Leave Reveal when you want to inspect the full evidence stack:

```txt
Runtime Evidence
Evidence State
Regime Map
Failure Timeline
Failure Boundary
Role Topology
Runtime Replay
Export
```
