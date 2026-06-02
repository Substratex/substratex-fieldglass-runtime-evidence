# Fieldglass Runtime Evidence 103 Card

## Deterministic Evidence Identity

Deterministic Evidence Identity means a Fieldglass run can be named, replayed, exported, checked, and reviewed without changing its meaning.

## Evidence Identity Chain

```txt
Raw input
↓
Input preservation
↓
Preflight envelope
↓
Canonical turns
↓
Computed telemetry
↓
Evidence events
↓
Replay metadata
↓
Deterministic identifiers
↓
Canonical exports
↓
Evidence bundle
```

## Key Identity Objects

```txt
case_id
run_id
evidence_id
export_id
schema_version
instrument_version
sample_id
input_hash
canonical_turns_hash
telemetry_hash
bundle_hash
```

## Canonical vs Diagnostic

```txt
Canonical evidence defines exported evidence.
Diagnostic evidence explains computed telemetry.
Projection evidence assists interpretation only.
```

## Evidence Integrity Checklist

```txt
[ ] Raw input preserved
[ ] Preflight envelope recorded
[ ] Canonical turns produced
[ ] Runtime telemetry computed
[ ] Evidence events identified
[ ] Replay metadata available
[ ] Export artifacts generated
[ ] Schema versions recorded
[ ] Checksums generated or preserved
[ ] Claim boundary attached
```

## Identity Failure Modes

```txt
Input drift
Adapter drift
Schema drift
Interpretation drift
Projection drift
Version drift
Attribution drift
```

## Core Rule

A strong Fieldglass case should let another reviewer trace the path:

```txt
raw input → preflight → canonical turns → telemetry → replay → export → claim boundary
```
