# 00 — Overview

## What Fieldglass® Is

Fieldglass® is a standalone, browser-local runtime cognition observatory by SubstrateX. It is designed to help operators, researchers, reviewers, and investigators turn AI interaction logs into deterministic runtime evidence.

The suite runs as a single HTML instrument. It can be opened locally in a browser or served through GitHub Pages. It does not require a backend, login, cloud storage, or transcript upload.

## What Fieldglass Does

Fieldglass accepts operational logs and transcripts, validates the input locally, normalizes supported roles and aliases, computes runtime telemetry, and displays the resulting evidence through a structured instrument suite.

It helps answer:

- What happened during the run?
- When did instability begin forming?
- Did failure become visible only after internal pressure accumulated?
- Which roles, tools, or handoffs contributed to runtime pressure?
- What evidence can be replayed, challenged, and exported?
- What does the instrument claim, and what does it not claim?

## What Fieldglass Is Not

Fieldglass is not a model provider, agent framework, benchmark runner, hallucination detector, consciousness detector, or truth adjudication engine.

Fieldglass does not inspect hidden model states. It operates on observable interaction evidence only.

## Why It Matters

Most AI evaluation focuses on the final answer, benchmark score, latency, cost, or uptime. Fieldglass focuses on runtime movement: trajectory, continuity, pressure, role stability, failure formation, lead-time, and evidence replay.

This makes it useful for incident review, operational testing, AI workflow validation, governance review, safety analysis, and public challenge cases.

## Primary Operator Path

```txt
Start
↓
Choose investigation context
↓
Load demo, paste transcript, or upload log
↓
Preflight validates input
↓
Compute Fieldglass
↓
Review simplified Reveal
↓
Inspect full Runtime Evidence
↓
Replay evidence
↓
Open instruments
↓
Export evidence bundle
```

## The Public Release Model

The public release is designed as a scientific instrument package:

```txt
index.html          ← the instrument
docs/               ← operator and evidence guidance
samples/            ← runnable logs
schemas/            ← export contracts
examples/           ← screenshots and known outputs
releases/           ← frozen historical builds
README.md           ← public entry point
```
