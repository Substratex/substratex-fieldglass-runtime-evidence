# 04 — Ingest / Blackbox

The Ingest / Blackbox page converts raw input into validated runtime evidence preparation.

## What the Blackbox Does

Blackbox transforms operational logs into runtime evidence.

It can accept:

- pasted transcripts
- uploaded logs
- built-in samples
- role-aware traces
- incident logs
- workflow coordination records
- multi-agent conversations

Blackbox preserves the original evidence, reconstructs runtime structure, identifies telemetry-bearing turns, and prepares the run for deterministic analysis and replay.

## Ideal Pane Order

The Ingest pane follows this operator sequence:

```txt
Start Here
↓
1. Choose Source
↓
2. Paste or Upload Input
↓
3. Preflight
↓
4. Compute Fieldglass
↓
5. Advanced
```

## 1. Choose Source

This section contains:

- Input Interpretation selector
- Load sample / upload / paste options
- Operational world preview

### Input Interpretation Options

Fieldglass can use:

- Auto-detect operational log
- Fieldglass transcript
- Software Engineering / GitHub / CI
- SIEM / Security Incident
- Cloud / Infrastructure
- Jira / Workflow Coordination
- Support / Customer Incident

Use **Auto-detect operational log** for most pasted logs.

## 2. Paste or Upload Input

Use this area to paste:

- AI conversations
- assistant/user transcripts
- CI logs
- SIEM incidents
- cloud event traces
- Jira workflows
- support incident logs

The preferred transcript format is:

```txt
Engineer:
Regression reproduced.

Tool:
Command executed.

Assistant:
Investigating root cause.
```

## 3. Preflight

Before compute, Fieldglass reports:

- detected log family
- adapter status
- operational world
- recommended path
- raw log preserved
- canonical turns produced
- telemetry-bearing turns
- readiness

Preflight does not produce final evidence. It checks whether the run is ready to compute.

## 4. Compute Fieldglass

The Compute Fieldglass button starts the deterministic runtime computation.

After compute, Fieldglass generates:

- runtime telemetry
- evidence state
- behavioral state
- lead-time
- failure timeline
- boundary / basin indicators
- role and tool pressure
- replay frames
- exportable evidence objects

## 5. Advanced

Advanced options may include:

- streaming append
- embedding trace
- ensemble runs
- reference manifold
- calibration

These are not required for the main demo path.

## Sample Library

The sample library includes canonical and operational samples. The killer demo sample should be visually distinguished from ordinary samples.

Primary sample:

```txt
SF-1 · The Failure Nobody Saw
```

Expected behavior:

- It appears as the primary canonical sample.
- It is outlined in red as the canonical demo.
- Other samples should not inherit the red outline.
- Loading the sample prepares it for compute.

## Ingestion Limits

Fieldglass prioritizes evidence completeness over visualization.

### Small Run

```txt
0–250 turns
Full telemetry • Full visualization • Full export
```

### Long Run

```txt
251–1,000 turns
Full telemetry • Sampled visualization • Chunked export
```

### Very Long Run

```txt
1,001–2,500 turns
Batch mode • Summary-first • Limited live visuals
```

## Preservation Policy

Fieldglass computes all available evidence first and reduces visualization complexity only when necessary.

Evidence is preserved. Visualization adapts.

Fieldglass should never silently truncate evidence.
