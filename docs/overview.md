# Fieldglass Overview

Fieldglass is a standalone, browser-local runtime cognition observatory for analyzing AI interaction logs as runtime evidence.

It treats an interaction log as a trajectory rather than a flat transcript. The instrument ingests observable turns, canonicalizes runtime structure, computes telemetry, and surfaces evidence about instability formation, lead-time, basin movement, role/tool pressure, failure boundaries, runtime behavioral state, and export integrity.

## Design Principle

Fieldglass is:

- local-first
- output-only
- non-interventional
- deterministic where canonical exports are concerned
- observable-evidence bounded
- portable as a single HTML file

## Evidence Layers

Fieldglass separates:

1. raw interaction evidence
2. structural extraction
3. runtime observables
4. evidence synthesis
5. interpretation
6. projection

Interpretive freedom increases upward. Deterministic certainty decreases upward.
