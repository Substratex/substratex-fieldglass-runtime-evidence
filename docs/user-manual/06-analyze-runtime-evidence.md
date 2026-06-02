# 06 — Analyze / Runtime Evidence

The Analyze section is the main runtime evidence workspace after compute.

## Navigation Labels

The Analyze section uses these subpage labels:

```txt
Runtime Evidence
Evidence State
Regime Map
Failure Timeline
Failure Boundary
Role Topology
Runtime Replay
```

## Runtime Evidence

Runtime Evidence is the primary computed evidence overview.

It contains the behavioral-state deck, runtime story, operator attention, evidence summary, and links into deeper analysis.

## Runtime Behavioral State

The Runtime Behavioral State cards summarize how the run moved.

Cards may include:

- Runtime Trajectory
- Continuity Signal
- Instability Pressure
- Temporal Deformation
- Role Pressure
- Boundary Formation
- Evidence Integrity

Before compute, cards may be visible with details, but visualizations should not render until a computed run exists.

After compute, visualizations show the actual run state.

## Evidence State

Evidence State shows the current evidence condition of the run.

It may include:

- stable / transitional / unstable regime
- event count
- current evidence pulse
- replayability
- operator attention
- recommended inspection path

## Regime Map

Regime Map displays how the run moved across runtime regimes.

Common regimes:

- Stable
- Transitional
- Turbulent
- Collapse / failure-proximate

Regime Map helps the operator see whether a run was stable throughout or crossed into risk.

## Failure Timeline

Failure Timeline shows event chronology.

It helps answer:

- when did pressure begin?
- when did boundary formation become visible?
- when did observable failure occur?
- what happened before the failure?

This replaces generic time labels with a failure-oriented evidence timeline.

## Failure Boundary

Failure Boundary shows basin exit, boundary pressure, or collapse-proximate formation.

It helps answer:

```txt
Where did the run begin leaving stable operational behavior?
```

This is a canonical forensic surface when backed by computed telemetry.

## Role Topology

Role Topology shows role/tool pressure, fragmentation, authority shifts, and handoff instability.

It helps answer:

- did role coherence degrade?
- did tool pressure increase?
- did handoffs become unstable?
- did manager / engineer / tool roles fragment?

## Runtime Replay

Runtime Replay lets the operator inspect the trajectory through time.

Replay should help show:

- event sequence
- turn-level progression
- pressure formation
- role shifts
- observable failure progression

## Recommended Analyze Path

For the killer demo, follow:

```txt
Runtime Evidence
↓
Evidence State
↓
Failure Timeline
↓
Failure Boundary
↓
Role Topology
↓
Runtime Replay
↓
Export
```
