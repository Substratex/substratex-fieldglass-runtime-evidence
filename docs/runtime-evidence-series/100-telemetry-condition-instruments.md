# 02A — Fieldglass Runtime Evidence 100: Telemetry Condition Instruments

## Turning Raw Runtime Metrics Into Readable Forensic Conditions

**Subtitle:** A practical guide to the Fieldglass telemetry adapter, core output-worldline metrics, condition instruments, runtime observatory tiles, and the translation from telemetry signals into operator-readable evidence.

Fieldglass Runtime Evidence 100 is the foundation module for the forensic series. It teaches operators what Fieldglass is extracting before the higher-order forensic layers begin. Before reading failure boundaries, temporal deformation, evidence identity, Chronos, or Cognitive Energetics, operators need to understand the base telemetry condition instruments.

The central idea is simple:

```txt
Telemetry engine generates the signal.
Condition instruments turn that signal into readable evidence.
```

---

## 1. What This Module Covers

This module explains:

- telemetry adapter layer
- raw log parsing
- feature extraction
- normalized structural metrics
- φ worldline
- instability and stability signals
- risk score
- condition-instrument mapping
- runtime observatory condition tiles
- Seismo / Lead-Time
- Drift
- Chronos
- Energetics
- Roles
- Basin
- Export / Integrity
- how metrics become decision surfaces
- claim boundaries for public telemetry

This module is numbered **100** because it should be read before Forensics 101.

---

## 2. What Fieldglass Currently Extracts

Fieldglass currently performs deterministic output-worldline analysis.

It does not access:

- model internals
- hidden states
- weights
- logits
- embeddings
- provider telemetry

It reads the interaction log as a runtime trace.

For each telemetry-bearing turn, Fieldglass extracts structural and lexical features such as:

```txt
Token entropy
Turn-to-turn drift
Baseline divergence
Repetition pressure
Length volatility
Reasoning density
```

These are normalized and combined into the behavioral worldline.

---

## 3. Current Primary Feature Layer

## Token Entropy

Measures lexical dispersion or uncertainty pressure.

Plain-language meaning:

```txt
How distributed or variable is the token field?
```

## Turn-to-Turn Drift

Measures change from the previous telemetry-bearing turn.

Plain-language meaning:

```txt
How much did the run move from the last step?
```

## Baseline Divergence

Measures movement away from the initial operating point.

Plain-language meaning:

```txt
How far has the run moved from where it began?
```

## Repetition Pressure

Measures redundancy, recurrence, or compression pressure.

Plain-language meaning:

```txt
Is the run repeating itself or compressing into the same structure?
```

## Length Volatility

Measures expansion or contraction of turn size.

Plain-language meaning:

```txt
Is the run suddenly expanding, shrinking, or fluctuating in structure?
```

## Reasoning Density

Measures structural reasoning signal from reasoning markers and structure.

Plain-language meaning:

```txt
Is the turn carrying reasoning structure, or losing it?
```

---

## 4. From Metrics to Worldline

The current engine computes a core instability estimate from normalized telemetry.

A simplified relationship is:

```txt
instability(t) = weighted structural / lexical pressure
φ(t) = 1 - instability(t)
```

So:

```txt
Higher φ(t) → more stable
Lower φ(t) → more unstable
```

This φ trajectory is the central behavioral worldline.

It is not a hidden model signal. It is an output-worldline signal derived from observable runtime evidence.

---

## 5. Telemetry Adapter Flow

The telemetry adapter converts raw logs into structured evidence.

The pipeline is:

```txt
Raw Logs
↓
Step Parsing
↓
Feature Extraction
↓
Metric Normalization
↓
Composite Signal φ
↓
ZSF-Compatible Output
↓
UI Rendering
```

The adapter is a translation layer between raw interaction evidence and the Fieldglass instrument surfaces.

It answers:

```txt
What can be extracted from the run before interpretation begins?
```

---

## 6. ZSF-Compatible Output

The telemetry adapter serializes outputs into structured evidence objects.

A simplified ZSF-compatible output may contain:

```txt
metadata
samples
computed values
φ
trit
adaptation values
hash
```

The hash matters because it helps ensure deterministic reproducibility.

Public evidence principle:

```txt
same input → same output artifact
```

---

## 7. From Signal to Decision

A telemetry engine is not enough.

A product needs a decision layer.

Telemetry alone gives:

```txt
metrics + φ
```

A Fieldglass forensic instrument should also derive:

```txt
detection turn
failure turn
Lead-Time
regime
operator attention
exportability
```

The mapping is:

```txt
INPUT → FEATURES → METRICS → SIGNAL → DECISION
```

This is the difference between a debug telemetry table and a forensic instrument.

---

## 8. Core Derived Signals

Fieldglass can expose a simplified decision layer using:

```txt
Stability
Risk
Drift
Divergence
```

Everything else can remain available in advanced mode.

## Detection Turn

The first turn where risk crosses a threshold.

Example logic:

```txt
detection_turn = first_turn_where(risk_score > threshold)
```

## Failure Turn

The first turn where observable failure appears or stability collapses.

Example logic:

```txt
failure_turn = first_turn_where(stability < threshold OR observable_failure_marker)
```

## Lead-Time

The warning window between detection and failure.

```txt
Lead-Time = failure_turn - detection_turn
```

## Why This Matters

The operator does not only need numbers.

The operator needs:

```txt
Instability detected at T53.
Failure appears at T61.
Lead-Time: 8 turns.
```

That is a forensic result.

---

## 9. Telemetry → Condition Instrument Mapping

The critical translation is:

```txt
Telemetry → Derived Signal → UI Condition Instrument
```

Example:

```txt
drift(t) → trajectory deviation → Drift condition instrument
risk_score(t) → detection state → Result / Attention panel
stability(t) → worldline stability → Seismo / Runtime Evidence
TCC / TSR / ETG → time deformation → Chronos condition instrument
role signals → fragmentation → Roles condition instrument
boundary signals → collapse geography → Basin condition instrument
export status → replayability → Integrity condition instrument
```

This is the core of Fieldglass Runtime Evidence 100.

---

# Runtime Observatory Condition Instruments

The Runtime Observatory tiles should not feel like generic dashboard widgets.

They should feel like restrained runtime condition instruments.

The condition-instrument ontology preserves:

```txt
Seismo / Lead-Time
Drift
Chronos
Energetics
Roles
Basin
Export / Integrity
```

Each tile is not merely a KPI. It is a condition field.

---

## 10. Seismo / Lead-Time

## What It Represents

Seismo / Lead-Time is the evidence window and detection band.

It answers:

```txt
When did Fieldglass detect instability before observable failure?
```

## Telemetry Basis

- φ trajectory
- stability decline
- risk threshold
- Basin Exit / boundary marker
- observable failure anchor
- detection turn
- failure turn

## Operator Reading

Look for:

```txt
Detection turn
Failure turn
Lead-Time
warning window
evidence band
```

## Forensic Question

```txt
How much warning did the runtime evidence provide?
```

---

## 11. Drift

## What It Represents

Drift is lateral trajectory deviation and instability movement.

It answers:

```txt
Is the run moving away from its expected path?
```

## Telemetry Basis

- turn-to-turn drift
- baseline divergence
- displacement from initial operating point
- drift vector
- drift acceleration

## Operator Reading

Look for:

- drift increasing
- divergence rising
- role-conditioned drift
- recurring deviation
- movement away from initial task identity

## Forensic Question

```txt
Did the run drift before failure became visible?
```

---

## 12. Chronos

## What It Represents

Chronos is temporal distortion and desynchronized flow.

It answers:

```txt
How did runtime time deform?
```

## Telemetry Basis

- temporal shear proxy
- temporal variance / viscosity
- temporal coupling / compression
- echo-time gradient
- τ-load
- timeline compression
- repeated retries

## Operator Reading

Look for:

- compression bands
- shear spikes
- echo-time amplification
- loop formation
- delayed recognition
- failure timeline deformation

## Forensic Question

```txt
Did the run’s time-structure compress, shear, or echo toward failure?
```

---

## 13. Energetics

## What It Represents

Energetics is computational strain and burn pressure.

It answers:

```txt
Where did runtime motion become cost-pressure?
```

## Telemetry Basis

- Energetic Pressure Index
- Boundary Event Count
- Weighted Boundary Load
- Stable Motion Ratio
- Correction Load
- Tool-I/O Pressure
- τ-load
- Collapse Cost Proxy

## Operator Reading

Look for:

- increasing correction work
- tool retry pressure
- rising boundary load
- temporal load
- collapse/recovery cost
- operational burden

## Forensic Question

```txt
Where did unstable cognition become expensive cognition?
```

Boundary:

```txt
Runtime cost-pressure proxy, not measured hardware energy.
```

---

## 14. Roles

## What It Represents

Roles is topology, authority split, and handoff fragmentation.

It answers:

```txt
Did role structure stabilize or fragment?
```

## Telemetry Basis

- role topology
- role objective drift
- authority gradient
- handoff coherence
- role-phase lag
- contradictory state injection
- tool-loop pressure

## Operator Reading

Look for:

- manager / PM / engineer misalignment
- observer/tool mismatch
- assistant/tool contradiction
- user correction loops
- unstable handoffs
- authority shifts

## Forensic Question

```txt
Did role fragmentation help create the runtime failure path?
```

---

## 15. Basin

## What It Represents

Basin is boundary topology and collapse geography.

It answers:

```txt
Where did the run begin leaving stable behavior?
```

## Telemetry Basis

- Basin Exit
- failure boundary
- regime transition
- contraction / expansion pressure
- instability accumulation
- boundary event
- collapse-proximate markers

## Operator Reading

Look for:

- stable → transitional movement
- persistent instability
- boundary pressure
- collapse region
- recovery or non-recovery

## Forensic Question

```txt
When did stable behavior stop being dominant?
```

---

## 16. Export / Integrity

## What It Represents

Export / Integrity is quiet provenance and evidence substrate.

It answers:

```txt
Can this run become a replayable, exportable evidence case?
```

## Telemetry Basis

- raw input preservation
- preflight envelope
- canonical turns
- computed telemetry
- replay metadata
- schema version
- checksums
- export artifacts
- claim boundary

## Operator Reading

Look for:

- replayability
- deterministic identity
- export readiness
- schema integrity
- Evidence Commons marker
- ZSF / ESL availability

## Forensic Question

```txt
Can another reviewer inspect the same evidence path?
```

---

# Core Operator Stack

Fieldglass lifts raw telemetry into a field-operator layer.

Important operator signals include:

```txt
κ(t)    local curvature of the output-worldline feature manifold
Π(t)    contraction / expansion pressure from rolling local radius
D(t)    displacement from the initial operating point
Echo(t) recurrence from token similarity + manifold recurrence
H(t)    field occupancy entropy over posture bins
λₜ      local divergence / Lyapunov-style estimator
TSR     temporal shear proxy
TVI/TV  temporal variance / viscosity proxy
TCC     temporal coupling / compression proxy
ETG     echo-time gradient / temporal escalation proxy
```

These operators help turn structural telemetry into higher-order condition instruments.

---

## 17. Regime Classification

From the worldline, Fieldglass derives regimes such as:

```txt
Stable
Transitional
Unstable
Collapse
Recovery
```

The regime is not a decorative label.

It summarizes where the run is in the evidence trajectory.

## Operator Question

```txt
Is the run stable, transitioning, unstable, collapsed, or recovering?
```

---

## 18. Basin Exit

Basin Exit is the first persistent transition into instability.

It helps answer:

```txt
When did the run begin leaving stable behavior?
```

Basin Exit is stronger when paired with:

- Lead-Time
- Failure Timeline
- Runtime Replay
- Role Topology
- Energetics

---

## 19. Observable Failure

Observable Failure is the user-defined, marker-defined, or evidence-defined failure anchor.

It should not be confused with boundary formation.

Boundary may form earlier. Observable failure appears later.

## Operator Question

```txt
Where did failure become visible to the outside observer?
```

---

## 20. Recovery

Recovery is a post-exit return toward stability.

Look for:

- stability improving
- risk decreasing
- role alignment returning
- tool loops resolving
- temporal pressure falling
- boundary pressure reducing

Recovery is evidence that a run may have left a basin and returned.

---

# Public Claim Boundary

For public release documentation, use:

```txt
Fieldglass computes deterministic output-worldline telemetry from observable interaction logs.
```

More detailed wording:

```txt
Fieldglass extracts structural, lexical, recurrence, role, temporal, and symbolic-field estimators from the interaction trace, then converts those signals into regime trajectories, Basin Exit detection, Lead-Time windows, forensic timelines, instrument views, and standards-aligned evidence artifacts.
```

Avoid claiming:

```txt
direct hidden-state measurement
internal transformer telemetry
provider logits
private embeddings
true model intention
consciousness detection
```

---

# Telemetry Condition Inspection Workflow

Use this workflow before deeper forensic modules:

```txt
1. Confirm the run has telemetry-bearing turns.
2. Review extracted structural metrics.
3. Inspect φ worldline.
4. Identify stability / risk direction.
5. Locate detection turn if present.
6. Locate observable failure if present.
7. Calculate or review Lead-Time.
8. Open Runtime Evidence.
9. Inspect Seismo / Lead-Time.
10. Inspect Drift.
11. Inspect Chronos.
12. Inspect Energetics.
13. Inspect Roles.
14. Inspect Basin.
15. Inspect Export / Integrity.
16. Continue into Forensics 101+.
```

---

# Telemetry Condition Checklist

```txt
[ ] Raw log parsed
[ ] Telemetry-bearing turns identified
[ ] Token entropy extracted
[ ] Turn-to-turn drift extracted
[ ] Baseline divergence extracted
[ ] Repetition pressure extracted
[ ] Length volatility extracted
[ ] Reasoning density extracted
[ ] Metrics normalized
[ ] Instability computed
[ ] φ worldline computed
[ ] Stability / risk derived
[ ] Regime classified
[ ] Basin Exit checked
[ ] Observable Failure checked
[ ] Lead-Time checked
[ ] Runtime Observatory condition instruments reviewed
[ ] Export / Integrity checked
```

---

# Minimal Telemetry Condition Summary

Use this template:

```txt
Case:
Operational world:
Telemetry-bearing turns:
Primary feature pressure:
φ trend:
Risk trend:
Regime:
Detection turn:
Failure turn:
Lead-Time:
Primary condition instrument:
Secondary condition instrument:
Basin Exit:
Recovery:
Export readiness:
Claim boundary:
```

---

# Common Telemetry Mistakes

## Mistake 1 — Treating metrics as the final answer

Metrics are the signal layer. The operator still needs derived evidence and interpretation.

## Mistake 2 — Showing too many raw metrics first

Most users need stability, risk, drift, and divergence first. Advanced users can inspect deeper operators.

## Mistake 3 — Confusing φ direction

In Fieldglass:

```txt
φ(t) = 1 - instability(t)
```

Higher φ is more stable. Lower φ is more unstable.

## Mistake 4 — Treating condition instruments like KPI cards

Condition instruments should show field state, not generic dashboard widgets.

## Mistake 5 — Overclaiming telemetry

The public browser tool computes output-worldline estimators, not hidden transformer telemetry.

---

# Final Principle

Telemetry is the root layer of Fieldglass forensics.

Before reading failure, boundary, identity, time, echo, or energetics, operators must understand the base condition instruments.

The strongest mental model is:

```txt
Raw log
↓
Telemetry adapter
↓
Structural metrics
↓
φ worldline
↓
Derived signals
↓
Runtime condition instruments
↓
Forensic interpretation
↓
Exportable evidence
```

Fieldglass Runtime Evidence begins when telemetry becomes readable as evidence.
