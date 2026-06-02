# 02 — Suite Architecture and Tiers

Fieldglass is organized as a tiered instrumentation suite. Each tier has a different evidence status.

## Tier 0 — Input and Preflight

Purpose: receive logs, validate structure, detect operational family, preserve raw input, and prepare canonical turns.

Includes:

- Start page context selection
- Ingest / Blackbox
- Input interpretation selector
- Sample library
- Paste / upload input
- Preflight validation
- Operational adapter detection

## Tier 1 — Canonical Evidence Layer

Purpose: compute and replay primary runtime evidence.

Includes:

- Runtime Evidence
- Evidence State
- Regime Map
- Failure Timeline
- Failure Boundary
- Runtime Replay
- Canonical export identity

This is the strongest evidence layer. It supports exported evidence artifacts.

## Tier 2 — Diagnostic Evidence Layer

Purpose: explain runtime behavior using diagnostic instruments over computed telemetry.

Includes:

- Chronos / temporal behavior
- Noesis / continuity formation
- Energetics / operational cost-pressure
- Drift / instability pathways
- Role Topology / role and tool pressure
- Benchmark bridge / deployment exposure

Diagnostic layers help interpret canonical evidence. They do not mutate canonical evidence.

## Tier 3 — Experimental Projection Layer

Purpose: visualize topology, geometry, phase posture, and recovery pathways.

Includes:

- Scope
- Interferometer
- Projection surfaces

Projection layers assist interpretation only. They are not direct evidence unless supported by computed runtime evidence and clearly bounded.

## Optional Input Layer

Some surfaces may accept optional embeddings or external telemetry. When not supplied, Fieldglass remains transcript-derived and observable-only.

## Interpretation Ladder

```txt
L0 — Raw interaction
L1 — Structural extraction
L2 — Runtime observables
L3 — Evidence synthesis
L4 — Interpretation
L5 — Projection
```

Interpretive freedom increases upward. Deterministic certainty decreases upward.

## Export Rule

Diagnostic and projection instruments may enrich interpretation, but they do not mutate:

- Zero Substrate Format
- Evolution & Synthesis Layer
- Basin Exit
- Lead-Time
- deterministic identity
- replay metadata

Canonical evidence remains immutable.
