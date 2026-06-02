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


---

# 01 — Quickstart

## Run Locally

1. Download the repository.
2. Open `index.html` in a modern browser.
3. No server is required.
4. No login is required.
5. No transcript upload is required.
6. No external API is required.

## Recommended First Run

Use the built-in killer demo:

```txt
The Failure Nobody Saw
```

This demo is designed to show the key Fieldglass pattern:

```txt
Benchmark success
+
Monitoring healthy
+
Fieldglass warning
+
Observable failure later
```

## Quick Demo Path

1. Open `index.html`.
2. On the Start page, choose an investigation context.
3. Click **Load “The Failure Nobody Saw”**.
4. Continue to Ingest / Blackbox.
5. Review the preflight result.
6. Click **Compute Fieldglass**.
7. Review the Reveal page.
8. Open Runtime Evidence.
9. Inspect Evidence State, Failure Timeline, Failure Boundary, Role Topology, and Runtime Replay.
10. Export the evidence bundle.

## What You Should See

After compute, Fieldglass should provide:

- Runtime behavioral state cards
- Lead-Time
- Cost of Failure / Failure Exposure
- Operator Attention
- Evidence timeline
- Role/tool pressure
- Boundary formation indicators
- Replayable evidence
- Export bundle options

## Local Privacy Model

Fieldglass is browser-local. In the public release, logs should be processed in the browser without requiring transcript upload, remote storage, or provider telemetry.

You should still redact sensitive data before sharing exported artifacts publicly.


---

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


---

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


---

# 03 — Fieldglass Runtime Evidence 101

## Seeing Inside the Operational Black Box

**Subtitle:** A practical guide to reading AI runtime evidence from observable logs, role profiles, and operational-world mappings.

Fieldglass Runtime Evidence 101 teaches operators how to read an AI run as evidence. The goal is not to guess hidden model state. The goal is to reconstruct observable runtime behavior: who acted, how the trajectory moved, where pressure accumulated, when roles fragmented, when a failure boundary formed, and what evidence can be replayed or exported.

Fieldglass does not see hidden cognition. It reconstructs runtime behavior from the observable evidence trail.

That is the central forensic frame.

---

## 1. What “Inside the Black Box” Means

In ordinary AI review, the “black box” is often treated as something inaccessible: a model produced an answer, and the operator can only judge the output.

Fieldglass changes the practical question.

It does **not** claim to inspect hidden model states. It does **not** claim consciousness detection, intent inference, or provider-internal access.

Instead, Fieldglass looks inside the **operational black box** by reconstructing what is visible in the interaction evidence:

- who acted
- which role produced each turn
- how the run moved over time
- where continuity weakened
- when pressure accumulated
- whether role/tool pressure rose
- where failure boundaries formed
- whether the evidence can be replayed
- what can be exported as an evidence case

### Correct Claim Boundary

```txt
Fieldglass does not see hidden cognition.
Fieldglass reconstructs observable runtime behavior from the evidence trail.
```

That boundary matters. It keeps the instrument powerful, but defensible.

---

## 2. The Forensic Logic of a Fieldglass Run

Fieldglass is not only:

```txt
ingest → compute → export
```

It has a forensic logic:

```txt
Raw log
↓
Operational world
↓
Role profile
↓
Runtime trajectory
↓
Pressure formation
↓
Failure boundary
↓
Replayable evidence
↓
Exportable case
```

This is the mental model operators should use.

A transcript is not just text. In Fieldglass, a transcript becomes a runtime evidence object.

---

## 3. The Forensic Reading Order

When reading any computed Fieldglass run, use this inspection sequence:

```txt
1. What operational world is this?
2. Which roles are active?
3. What did preflight preserve?
4. When did the trajectory begin changing?
5. Did role/tool pressure rise?
6. Did temporal pressure compress?
7. Did a failure boundary form?
8. Was there Lead-Time?
9. Can the evidence be replayed?
10. What can be exported?
```

This order prevents the operator from jumping straight to a dramatic metric without first understanding the evidence context.

---

## 4. Step 1 — Identify the Operational World

The operational world tells Fieldglass what kind of run it is reading.

Common operational worlds include:

```txt
Software Engineering / GitHub / CI
SIEM / Security Incident
Cloud / Infrastructure
Jira / Workflow Coordination
Support / Customer Incident
```

The operational world does not replace evidence. It gives the run a practical context.

The same runtime signal can mean different things in different worlds. For example, repeated tool calls in a software repair loop may indicate debugging. Repeated tool calls in a security incident may indicate triage escalation or monitoring confusion. In a support incident, repeated explanations may indicate unresolved customer impact.

---

## 5. Step 2 — Read the Role Profiles

Fieldglass maps logs into role profiles.

Canonical roles include:

```txt
System
User
Assistant
Engineer
Manager
PM
Observer
Tool
Admin
```

Role profiles make the runtime legible.

## Role Behavior Guide

| Role | Typical Behavior | Forensic Questions |
|---|---|---|
| System | Sets rules, context, or operating constraints | Did the run inherit constraints that shaped the failure? |
| User | Requests, clarifies, corrects, escalates | Did user pressure rise? Did the user signal failure before the system did? |
| Assistant | Reasons, plans, synthesizes, responds | Did the assistant maintain trajectory, or drift? |
| Engineer | Investigates, repairs, verifies | Did repair activity converge or loop? |
| Manager / PM | Coordinates, prioritizes, escalates | Did coordination stabilize or fragment? |
| Observer | Monitors, detects, records | Did observation detect pressure early or miss it? |
| Tool | Executes, reports, fails, retries | Did tools amplify pressure, compress loops, or produce ambiguous outputs? |
| Admin | Configures, controls, authorizes | Did configuration or authority affect the run? |

The point is not merely to label speakers. The point is to see how responsibilities moved during the run.

---

## 6. Step 3 — Review What Preflight Preserved

Preflight is not the final evidence layer. It is the evidence preparation layer.

Preflight should tell you:

- detected log family
- adapter applied or not applied
- operational world
- recommended path
- raw log preserved
- canonical turns produced
- telemetry-bearing turns
- readiness

### What to Look For

Ask:

```txt
Did Fieldglass preserve the raw log?
Did it normalize roles correctly?
Did it avoid converting operational evidence labels into fake speakers?
Did it produce enough canonical turns for compute?
Did it identify the right operational world?
```

Preflight is where the operator confirms that the evidence has not been flattened, truncated, or misread before compute.

---

## 7. Step 4 — Find Where the Trajectory Changed

Runtime evidence begins when the trajectory changes.

In Fieldglass, the trajectory may weaken through:

- drift acceleration
- continuity loss
- unstable handoffs
- role fragmentation
- tool retry compression
- pressure accumulation
- temporal narrowing
- boundary approach

The operator should not ask only:

```txt
Did the run fail?
```

The better forensic question is:

```txt
When did the run begin moving differently?
```

This is how Fieldglass makes failure formation visible before the failure becomes obvious.

---

## 8. Step 5 — Inspect Role and Tool Pressure

Role and tool pressure is often where the black box becomes readable.

Look for:

- role fragmentation
- authority shifts
- manager / PM / engineer misalignment
- observer/tool mismatch
- tool retry loops
- command/result mismatch
- escalating human intervention
- unstable handoffs

## Example Pattern

```txt
Engineer investigates.
Tool reports partial or ambiguous output.
Assistant continues as if stable.
Manager escalates priority.
Tool retries increase.
Role pressure rises.
Boundary begins forming.
```

This pattern is not just a conversation. It is a runtime pressure sequence.

---

## 9. Step 6 — Inspect Temporal Pressure

Temporal pressure appears when the run begins to compress.

Signs include:

- shortened reasoning horizon
- repeated attempts with less resolution
- rising urgency
- compressed tool loops
- delayed recognition of failure
- late-stage correction attempts

In the instrument, temporal behavior may appear in Failure Timeline, Chronos/temporal surfaces, Lead-Time, or runtime behavioral-state indicators.

The forensic question is:

```txt
Did the run have enough time to stabilize before failure became visible?
```

---

## 10. Step 7 — Identify Failure Boundary Formation

A failure boundary is where stable runtime behavior begins giving way to failure-proximate behavior.

Boundary formation may appear through:

- Basin Exit
- rising instability pressure
- role fragmentation
- continuity weakening
- temporal compression
- tool pressure
- observable failure progression

The key question is:

```txt
Where did the run begin leaving stable behavior?
```

This is different from asking when the final failure happened.

Failure is often late evidence. Boundary formation is earlier evidence.

---

## 11. Step 8 — Check Lead-Time

Lead-Time is one of the most important Fieldglass concepts.

It asks:

```txt
How many turns before observable failure did Fieldglass detect failure formation?
```

Example:

```txt
Lead-Time: 6 turns
```

Lead-Time turns the instrument from a postmortem viewer into a forensic warning surface.

It shows that the run may have become failure-proximate before traditional monitoring or final-output review noticed anything wrong.

---

## 12. Step 9 — Replay the Evidence

Replay matters because evidence should not only be summarized. It should be inspectable.

Use Runtime Replay to inspect:

- the sequence of events
- role changes
- pressure formation
- boundary movement
- failure progression
- evidence pulses
- turn-level transitions

Replay helps the operator verify that the summary is grounded in the run.

The question is:

```txt
Can another operator follow the same evidence path?
```

If yes, the run is stronger as an evidence case.

---

## 13. Step 10 — Export the Evidence Case

A Fieldglass investigation should end with an exportable evidence case when the run is useful.

Typical evidence case construction:

```txt
1. Preserve raw log.
2. Run preflight.
3. Compute Fieldglass.
4. Identify Lead-Time / boundary / failure timeline.
5. Inspect role/tool pressure.
6. Replay the trajectory.
7. Export ZSF / ESL / Human Report / Evidence Commons bundle.
8. Attach claim boundary.
```

## Export Artifacts

Common exports include:

- Zero Substrate Format
- Evolution & Synthesis Layer
- Human Report
- Benchmark Bridge Appendix
- Runtime Vulnerability Report
- Evidence Commons Bundle
- Technical Evidence Appendix
- Role Dynamics Appendix
- Temporal Kernel Appendix

---

# Operational World Forensic Patterns

## Software Engineering / GitHub / CI

Look for:

- retry loops
- tool output compression
- regression confusion
- failed repair verification
- command/result mismatch
- assistant overconfidence after failed tool output
- unresolved test failures
- repeated patch attempts with weakening trajectory

### Typical Evidence Path

```txt
Ingest
↓
Preflight detects software / CI context
↓
Runtime Evidence
↓
Failure Timeline
↓
Role Topology
↓
Tool pressure
↓
Runtime Replay
↓
Export
```

### Forensic Questions

```txt
Did the repair loop converge?
Did the tool output contradict the assistant plan?
Did retries accumulate?
Did the assistant treat partial success as full success?
Did role/tool pressure rise before failure?
```

---

## SIEM / Security Incident

Look for:

- alert escalation
- observer/tool mismatch
- triage drift
- missed severity transition
- authority shift
- false stability
- delayed incident recognition
- repeated alert interpretation without resolution

### Typical Evidence Path

```txt
Ingest
↓
Preflight detects security incident context
↓
Evidence State
↓
Failure Timeline
↓
Role Topology
↓
Observer / Tool pressure
↓
Runtime Replay
↓
Export
```

### Forensic Questions

```txt
Did the observer detect the signal early?
Did the tool output create ambiguity?
Did escalation happen late?
Did the run miss a severity transition?
Did the assistant or operator normalize risk too early?
```

---

## Cloud / Infrastructure

Look for:

- monitoring healthy but operational pressure rising
- SRE handoff instability
- recovery loop failure
- repeated mitigation attempts
- alert/tool mismatch
- delayed root-cause recognition
- unstable failover or rollback narratives

### Typical Evidence Path

```txt
Ingest
↓
Preflight detects cloud / infrastructure context
↓
Runtime Evidence
↓
Regime Map
↓
Failure Boundary
↓
Role Topology
↓
Runtime Replay
↓
Export
```

### Forensic Questions

```txt
Did monitoring appear healthy while runtime pressure increased?
Did recovery attempts converge or loop?
Did SRE/tool roles stay aligned?
Did failure boundary form before user-visible impact?
```

---

## Jira / Workflow Coordination

Look for:

- PM / manager / engineer misalignment
- task ambiguity
- priority drift
- handoff collapse
- scope confusion
- unresolved ownership
- coordination loops
- delayed escalation

### Typical Evidence Path

```txt
Ingest
↓
Preflight detects workflow coordination context
↓
Runtime Evidence
↓
Role Topology
↓
Failure Timeline
↓
Evidence State
↓
Export
```

### Forensic Questions

```txt
Did ownership become unclear?
Did priorities shift without closure?
Did the PM/manager/engineer roles fragment?
Did coordination pressure rise before the workflow failed?
```

---

## Support / Customer Incident

Look for:

- escalation pressure
- repeated explanations
- unresolved customer state
- customer-impact persistence
- agent deadlock
- handoff confusion
- failed resolution loop
- delayed recognition of severity

### Typical Evidence Path

```txt
Ingest
↓
Preflight detects support incident context
↓
Runtime Evidence
↓
Operator Attention
↓
Failure Timeline
↓
Role Topology
↓
Runtime Replay
↓
Export
```

### Forensic Questions

```txt
Did the customer issue resolve?
Did the support flow loop?
Did escalation happen too late?
Did the assistant repeat instead of progress?
Did human intervention become necessary?
```

---

# Monitoring vs Fieldglass Runtime Evidence

## Monitoring Asks

```txt
Is the system healthy?
```

Monitoring may show:

```txt
Latency: normal
Errors: none
Requests: healthy
Tool availability: 100%
System status: green
```

## Fieldglass Runtime Evidence Asks

```txt
Was the runtime becoming unstable even while the system appeared healthy?
```

Fieldglass may show:

```txt
Role fragmentation rising
Drift accelerating
Temporal pressure compressing
Failure boundary forming
Lead-Time detected
Tool pressure accumulating
Replayable evidence available
```

This distinction is the heart of the suite.

Monitoring sees infrastructure state. Fieldglass reconstructs runtime behavior.

---

# Modern Runtime Evidence

Modern AI forensics is not only reading the final answer.

It is reconstructing the run:

```txt
who acted
what changed
when pressure rose
where continuity broke
which boundary formed
what evidence can be replayed
what can be exported
```

Fieldglass turns logs into runtime evidence by reading the run as a sequence of observable behaviors.

The goal is not to replace human judgment. The goal is to give human judgment a structured evidence surface.

---

# Fieldglass Forensic Inspection Checklist

Use this checklist after compute:

```txt
[ ] Operational world identified
[ ] Role profile confirmed
[ ] Raw log preserved
[ ] Canonical turns produced
[ ] Runtime trajectory inspected
[ ] Continuity signal checked
[ ] Role/tool pressure inspected
[ ] Temporal pressure inspected
[ ] Failure boundary checked
[ ] Lead-Time checked
[ ] Runtime Replay reviewed
[ ] Export artifacts generated
[ ] Claim boundary attached
```

---

# Minimal Forensic Summary Template

Use this template when documenting a case:

```txt
Case:
Operational world:
Input type:
Roles detected:
Preflight result:
Primary runtime signal:
Lead-Time:
Failure boundary:
Role/tool pressure:
Failure timeline:
Replay status:
Exports generated:
Claim boundary:
```

---

# Final Principle

Fieldglass is not just a tool that computes metrics.

Fieldglass is a method for modern runtime evidence.

It teaches operators to see the run as evidence: not only what the AI said, but how the runtime moved before the outcome became visible.


---

# 04 — Fieldglass Temporal Runtime Evidence 102

## Reading Failure Through Time

**Subtitle:** A practical guide to temporal evidence, Lead-Time, failure timelines, runtime compression, and boundary formation in Fieldglass®.

Fieldglass Temporal Runtime Evidence 102 teaches operators how to read time as evidence. The goal is not only to know that a failure occurred. The goal is to understand when the run began changing, how pressure accumulated across turns, whether time compressed, when a boundary formed, and how early Fieldglass surfaced evidence before visible failure.

Temporal forensics is the discipline of reconstructing the time-structure of a run.

In Fieldglass, time is not just a clock. Time is a runtime pattern.

---

## 1. What Temporal Runtime Evidence Means

Traditional review often asks:

```txt
What was the final outcome?
```

Temporal forensics asks:

```txt
How did the run move over time before that outcome appeared?
```

This changes the investigation.

Instead of treating the final failure as the only important event, Fieldglass asks the operator to inspect the full temporal sequence:

```txt
stable behavior
↓
early pressure
↓
role/tool instability
↓
trajectory weakening
↓
boundary formation
↓
visible failure
```

The key insight:

```txt
Failure is often late evidence.
Temporal pressure appears earlier.
```

---

## 2. The Claim Boundary

Fieldglass does not claim access to hidden model time, hidden cognition, or internal provider telemetry.

Fieldglass reconstructs temporal behavior from observable interaction evidence:

- turn order
- role sequence
- event chronology
- response length shifts
- repeated attempts
- retry loops
- delayed resolution
- tool output cycles
- observed failure progression
- computed runtime telemetry

Correct claim:

```txt
Fieldglass reconstructs observable runtime time-structure from the evidence trail.
```

Avoid claiming:

```txt
Fieldglass sees hidden model time.
Fieldglass measures consciousness over time.
Fieldglass knows intent.
Fieldglass proves causality beyond the evidence.
```

---

## 3. The Temporal Evidence Chain

Temporal forensics follows this chain:

```txt
Raw sequence
↓
Turn chronology
↓
Runtime trajectory
↓
Pressure accumulation
↓
Temporal deformation
↓
Lead-Time
↓
Failure timeline
↓
Boundary formation
↓
Replayable temporal evidence
↓
Exportable case
```

This chain helps operators avoid reading a run as a flat transcript.

A transcript is not just a sequence of messages. It is a runtime path.

---

## 4. The Temporal Reading Order

When inspecting time in a Fieldglass run, use this order:

```txt
1. What is the turn range?
2. Where is the stable phase?
3. When does pressure first appear?
4. When does the trajectory begin weakening?
5. When does role/tool pressure accelerate?
6. Does the run compress into retries or repeated attempts?
7. When does the failure boundary form?
8. What is the Lead-Time?
9. Where does observable failure occur?
10. Can the timeline be replayed and exported?
```

This order gives the operator a disciplined way to inspect temporal evidence.

---

## 5. Wall-Clock Time vs Runtime Time

Fieldglass primarily reads runtime time, not wall-clock time.

## Wall-Clock Time

Wall-clock time is ordinary elapsed time:

```txt
10:01 AM
10:02 AM
10:03 AM
```

It is useful when logs include timestamps.

## Runtime Time

Runtime time is the sequence of evidence-bearing turns, events, and transitions:

```txt
T1
T2
T3
...
T47
```

Runtime time answers:

```txt
How did the interaction evolve?
When did the run start changing?
Where did pressure accumulate?
When did failure become visible?
```

In many AI interaction logs, runtime turn order is more reliable than wall-clock timing because transcripts often lack precise timestamps.

---

## 6. Turn Chronology

Turn chronology is the basic temporal spine.

It answers:

- what happened first?
- what happened next?
- what sequence led to failure?
- did the same pattern repeat?
- did the run recover or continue degrading?

Example:

```txt
T1–T20: Stable
T21–T32: Pressure forming
T33–T41: Boundary formation
T42–T46: Silent degradation
T47: Observable failure
```

This is the core structure of a temporal forensic case.

---

## 7. Stable Phase

The stable phase is the portion of the run where the trajectory appears coherent.

Look for:

- consistent role behavior
- clear task progression
- low retry pressure
- continuity across turns
- tool outputs matching plans
- no obvious boundary pressure

The stable phase matters because it gives the operator a baseline.

Without a baseline, pressure is harder to interpret.

Forensic question:

```txt
What did stable behavior look like before the run changed?
```

---

## 8. Pressure Formation

Pressure formation is where the run begins to change.

Signs include:

- repeated attempts
- ambiguous tool output
- longer or more defensive responses
- unresolved questions
- role confusion
- task redirection
- escalation language
- delayed closure
- increased operator correction

The operator should ask:

```txt
What is the first visible sign that the run is no longer moving cleanly?
```

Pressure formation is often earlier than failure.

---

## 9. Temporal Deformation

Temporal deformation means the run’s time-structure begins to distort.

In practical terms, this can look like:

- a narrowing planning horizon
- repeated loops
- rushed corrections
- tool retries with less progress
- escalating urgency
- compression of reasoning into shorter cycles
- late recognition of a problem
- many events packed into a small turn window

Temporal deformation does not mean time literally changes. It means the run behaves as if the operational horizon is narrowing.

Plain-language version:

```txt
The run starts spending more turns to make less progress.
```

---

## 10. Temporal Compression

Temporal compression is one of the most important signs in AI runtime evidence.

It appears when the system repeats, retries, or compresses work without resolving the underlying instability.

Look for:

```txt
retry
retry
partial result
retry
new explanation
same failure
tool call
tool call
manual intervention
```

This pattern may indicate:

- tool storm
- agent deadlock
- failed recovery loop
- rising operator burden
- increasing cost-pressure
- boundary approach

Forensic question:

```txt
Is the run using more runtime motion to achieve less operational progress?
```

---

## 11. Lead-Time

Lead-Time is the number of turns between detectable failure formation and observable failure.

It answers:

```txt
How early did Fieldglass detect failure formation?
```

Example:

```txt
Lead-Time: 6 turns
```

If failure occurs at T47 and Fieldglass detects boundary formation at T41, the Lead-Time is:

```txt
6 turns
```

## Why Lead-Time Matters

Lead-Time is operationally important because it shows that the failure was not simply sudden.

It may have formed earlier through observable runtime pressure.

Fieldglass is strongest when it can show:

```txt
The system looked healthy.
The final output had not failed yet.
But the runtime trajectory was already failure-proximate.
```

---

## 12. Failure Timeline

Failure Timeline is the temporal reconstruction of the run.

It should show:

- stable phase
- pressure phase
- boundary phase
- silent degradation
- observable failure
- recovery or non-recovery

A strong failure timeline is simple enough for humans to read but grounded enough for evidence review.

Example:

```txt
T1–T20: Stable task progression
T21–T32: Pressure accumulation
T33–T41: Failure boundary formation
T42–T46: Silent degradation
T47: Observable failure
```

## How to Use It

Ask:

```txt
Where did the first meaningful change appear?
Where did pressure accelerate?
Where did the boundary form?
Where did failure become visible?
Did the run recover afterward?
```

---

## 13. Failure Boundary

Failure Boundary is where the run begins leaving stable behavior.

Temporal forensics treats the boundary as a time event, not only a state.

The boundary asks:

```txt
When did the run become failure-proximate?
```

Boundary formation may be visible through:

- role fragmentation
- drift acceleration
- continuity weakening
- repeated tool loops
- escalation pressure
- unstable handoffs
- temporal compression
- unresolved state persisting across turns

Boundary formation is one of the strongest temporal indicators because it can appear before final failure.

---

## 14. Silent Degradation

Silent degradation is when the run is getting worse but external signals still appear acceptable.

Traditional monitoring may show:

```txt
Latency: normal
Errors: none
Requests: healthy
Tool availability: high
```

But Fieldglass may show:

```txt
role fragmentation rising
drift accelerating
runtime pressure increasing
boundary forming
Lead-Time present
```

This is why temporal runtime evidence matters.

It gives the operator a way to see degradation before the final failure becomes obvious.

---

## 15. Recovery Windows

A recovery window is the period where intervention may still stabilize the run.

Temporal forensics asks:

```txt
Was there a window where the run could have recovered?
```

Potential recovery signals:

- clear correction
- role re-alignment
- tool output becomes stable
- retry pressure decreases
- continuity improves
- boundary pressure falls
- operator intervention restores direction

Potential non-recovery signals:

- repeated retries
- unresolved ambiguity
- escalating role fragmentation
- no stable handoff
- growing tool pressure
- continued temporal compression

---

## 16. Runtime Replay as Temporal Evidence

Runtime Replay is where the operator verifies the temporal narrative.

Do not rely only on summary cards.

Use Replay to inspect:

- turn sequence
- event progression
- pressure rise
- role shifts
- boundary approach
- failure moment
- recovery or non-recovery

Replay answers:

```txt
Can another operator follow the same temporal evidence path?
```

If the answer is yes, the case is stronger.

---

## 17. Temporal Evidence in the Killer Demo

In **The Failure Nobody Saw**, the temporal story is the central lesson.

The pattern is:

```txt
System appears healthy.
Benchmark-like capability appears sufficient.
Runtime pressure begins accumulating.
Fieldglass warning appears before visible failure.
Observable failure happens later.
```

A simple demo timeline may read:

```txt
T1–T20: Stable
T21–T32: Pressure
T33–T41: Boundary formation
T42–T46: Silent degradation
T47: Observable failure
```

The operator should focus on this question:

```txt
What did Fieldglass see before everyone else saw the failure?
```

That is the temporal significance of the demo.

---

# Operational World Temporal Patterns

## Software Engineering / GitHub / CI

Temporal risk often appears as retry compression.

Look for:

- repeated patch attempts
- recurring test failures
- command/result mismatch
- tool output loops
- delayed verification
- apparent progress followed by regression
- retries with shrinking reasoning horizon

Forensic question:

```txt
When did debugging stop converging and start looping?
```

## SIEM / Security Incident

Temporal risk often appears as delayed severity recognition.

Look for:

- alert escalation
- repeated triage without resolution
- observer/tool mismatch
- missed severity transition
- delayed authority shift
- late incident declaration

Forensic question:

```txt
When did the incident become more severe than the run acknowledged?
```

## Cloud / Infrastructure

Temporal risk often appears as recovery loop failure.

Look for:

- monitoring healthy while pressure rises
- repeated mitigation
- failover ambiguity
- rollback uncertainty
- unstable SRE handoff
- delayed root-cause closure

Forensic question:

```txt
When did recovery stop reducing pressure?
```

## Jira / Workflow Coordination

Temporal risk often appears as coordination drift.

Look for:

- unresolved ownership
- shifting priority
- repeated clarification
- handoff delay
- PM/engineer misalignment
- task state not closing

Forensic question:

```txt
When did coordination stop moving toward closure?
```

## Support / Customer Incident

Temporal risk often appears as unresolved customer-impact persistence.

Look for:

- repeated explanations
- unresolved state
- escalation delay
- handoff confusion
- customer repeats same issue
- support agent loops without closure

Forensic question:

```txt
When did support activity stop reducing customer impact?
```

---

# Temporal Runtime Evidence Workflow

Use this workflow after compute:

```txt
1. Open Runtime Evidence.
2. Identify the run window.
3. Inspect Runtime Behavioral State.
4. Open Failure Timeline.
5. Locate stable phase.
6. Locate first pressure formation.
7. Locate boundary formation.
8. Check Lead-Time.
9. Open Role Topology.
10. Check whether role/tool pressure explains the temporal shift.
11. Open Runtime Replay.
12. Replay the failure path.
13. Export the evidence case.
```

---

# Temporal Inspection Checklist

```txt
[ ] Turn window identified
[ ] Stable phase identified
[ ] First pressure signal identified
[ ] Trajectory weakening identified
[ ] Role/tool pressure inspected
[ ] Temporal compression checked
[ ] Failure boundary located
[ ] Lead-Time calculated or reviewed
[ ] Observable failure located
[ ] Recovery window assessed
[ ] Runtime Replay reviewed
[ ] Export artifacts generated
[ ] Claim boundary attached
```

---

# Minimal Temporal Case Summary

Use this template:

```txt
Case:
Operational world:
Run window:
Stable phase:
First pressure signal:
Trajectory shift:
Temporal compression:
Failure boundary:
Lead-Time:
Observable failure:
Recovery window:
Replay status:
Exports:
Claim boundary:
```

---

# Common Temporal Mistakes

## Mistake 1 — Treating failure as sudden

Many failures appear sudden only because the review starts too late.

Fieldglass asks the operator to look earlier.

## Mistake 2 — Confusing monitoring health with runtime stability

A system can be technically healthy while the runtime is becoming unstable.

## Mistake 3 — Ignoring role timing

Role pressure is temporal. It matters when authority shifts, when a handoff fails, and when a tool loop begins.

## Mistake 4 — Exporting without replay

Temporal claims are stronger when replayed.

## Mistake 5 — Overclaiming

Do not claim hidden causality. Claim observable temporal evidence.

---

# Final Principle

Temporal forensics turns a transcript into a timeline of runtime formation.

Fieldglass helps the operator see not only that a failure occurred, but how the run moved toward it.

The temporal question is:

```txt
What became visible in the runtime before failure became visible in the outcome?
```


---

# 05 — Fieldglass Runtime Evidence 103: Deterministic Evidence Identity

## Making Runtime Evidence Replayable, Verifiable, and Exportable

**Subtitle:** A practical guide to evidence identity, canonical exports, replay metadata, schema discipline, checksums, and evidence integrity in Fieldglass®.

Fieldglass Runtime Evidence 103 teaches operators how to treat a computed run as an evidence object. The goal is not only to inspect what happened. The goal is to preserve the identity of the evidence so another reviewer can understand what was ingested, how it was normalized, what was computed, what was exported, and whether the resulting case can be replayed or challenged.

Deterministic Evidence Identity is the discipline of making a runtime evidence case stable enough to cite, export, compare, and review.

---

## 1. What Deterministic Evidence Identity Means

A Fieldglass run becomes useful as evidence when it has a stable identity.

A stable evidence identity answers:

```txt
What input was used?
How was it normalized?
What run was computed?
Which telemetry was generated?
Which evidence events were identified?
Which replay frames were created?
Which exports came from this run?
Can another reviewer inspect the same evidence path?
```

In simple terms:

```txt
Deterministic Evidence Identity means the evidence can be named, replayed, exported, and checked without changing its meaning.
```

---

## 2. Why Identity Matters

Without deterministic identity, an AI incident review becomes a loose narrative.

With deterministic identity, the run becomes a case.

A case can be:

- cited
- replayed
- exported
- compared
- challenged
- archived
- reviewed by another operator
- attached to a report
- used as a public evidence example

Identity is what turns a transcript into a forensic artifact.

---

## 3. The Evidence Identity Chain

Fieldglass evidence identity follows this chain:

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

Each layer should preserve traceability back to the original run.

The operator should always be able to ask:

```txt
Where did this exported claim come from?
```

And the evidence package should answer.

---

## 4. Observable Evidence Boundary

Deterministic evidence identity does not mean Fieldglass proves hidden model state.

It means Fieldglass preserves and computes a stable evidence identity from observable interaction evidence.

Correct claim:

```txt
Fieldglass creates deterministic evidence identity from observable runtime evidence.
```

Incorrect claim:

```txt
Fieldglass proves the hidden internal cause of the model’s behavior.
```

The identity is deterministic relative to the public instrument, the input, the published schemas, and the computed runtime/evidence semantics.

---

## 5. Raw Input Preservation

Raw input preservation is the first identity requirement.

The raw log is the source evidence.

It may be:

- a native Fieldglass transcript
- an AI interaction log
- a GitHub / CI log
- a SIEM incident trace
- a cloud infrastructure event
- a Jira workflow record
- a support incident transcript
- a multi-agent conversation

Fieldglass should preserve the raw evidence while also creating canonical turns for compute.

## Operator Check

Before compute, ask:

```txt
Was the raw log preserved?
Was any content silently removed?
Was the input truncated?
Was the input transformed without a record?
```

A strong evidence case should not silently lose the raw evidence trail.

---

## 6. Preflight Envelope

The preflight envelope records how the input was prepared before compute.

It may include:

- detected log family
- adapter applied or not applied
- operational world
- recommended path
- raw log preserved
- canonical turns produced
- telemetry-bearing turns
- readiness
- warnings
- unsupported labels
- role aliases applied

Preflight is part of the evidence identity because it records the transition from raw input to computable structure.

## Why This Matters

If two operators disagree about a result, the first question should be:

```txt
Did they compute from the same preflight envelope?
```

If not, they may not be reviewing the same evidence object.

---

## 7. Canonical Turns

Canonical turns are the normalized interaction units used for compute.

A canonical turn typically contains:

- role
- speaker
- content
- session identifier
- turn index
- optional metadata

Canonical turns make the input computable while preserving role structure.

## Supported Role Profiles

Common canonical roles include:

```txt
System
User
Assistant
Engineer
Manager
PM
Observer
Tool
Admin
```

## Operator Check

Ask:

```txt
Were speaker labels normalized correctly?
Were operational sublabels preserved as evidence markers?
Were tools treated as tools?
Were observers treated as observers?
Were unsupported labels handled safely?
```

Bad role normalization can corrupt evidence identity.

---

## 8. Operational Adapters and Identity

Operational adapters normalize raw logs into Fieldglass-ready structure.

Examples:

```txt
Software Engineering / GitHub / CI
SIEM / Security Incident
Cloud / Infrastructure
Jira / Workflow Coordination
Support / Customer Incident
```

Adapters should normalize structure only.

They should not invent evidence, erase evidence, or modify the meaning of the run.

Correct adapter function:

```txt
raw operational log → preserved raw log + canonical turns
```

Incorrect adapter function:

```txt
raw operational log → rewritten story
```

## Adapter Identity Questions

```txt
Which adapter was applied?
What family was detected?
Which aliases were normalized?
Were unsupported labels preserved?
Were warnings generated?
```

---

## 9. Computed Telemetry Identity

After compute, Fieldglass generates runtime telemetry.

Telemetry may include:

- trajectory stability
- continuity signal
- instability pressure
- temporal deformation
- role pressure
- boundary formation
- evidence integrity
- Lead-Time
- failure timeline
- replay frames
- regime transitions
- operator attention
- cost-pressure proxy

Telemetry identity means the metrics are tied to the computed run, not manually edited after the fact.

## Operator Check

Ask:

```txt
Were these telemetry values computed from this run?
Are they replayable?
Do they match the exported evidence?
Are they clearly separated from interpretation?
```

---

## 10. Evidence Events

Evidence events are important runtime events extracted or synthesized from computed telemetry.

Examples:

- pressure formation
- role fragmentation
- authority shift
- tool pressure rise
- temporal compression
- boundary formation
- Basin Exit
- Lead-Time marker
- observable failure
- recovery attempt
- replay checkpoint

Evidence events give the run a forensic timeline.

They help the operator explain:

```txt
what changed
when it changed
why it matters
where to inspect
```

---

## 11. Replay Metadata

Replay metadata is what allows a reviewer to inspect the evidence sequence.

It may include:

- turn index
- frame index
- event order
- regime state
- role state
- telemetry values
- evidence pulse
- timeline label
- replay window

Replay metadata matters because evidence should not only be summarized. It should be inspectable.

## Replay Identity Question

```txt
Can another reviewer follow the same replay path from raw evidence to exported claim?
```

If yes, the case is stronger.

---

## 12. Deterministic Identifiers

A deterministic evidence case should include identifiers.

Possible identifiers:

```txt
case_id
run_id
evidence_id
export_id
schema_version
instrument_version
sample_id
created_at
input_hash
canonical_turns_hash
telemetry_hash
bundle_hash
```

The public instrument may use a simple version of this identity model.

The important point is not that every release has every identifier. The important point is that the evidence can be named and checked.

## Evidence Commons Marker

A public challenge case may use an Evidence Commons marker such as:

```txt
EC-2026-CANONICAL-001
```

This marker identifies the case as a known evidence object.

---

## 13. Hashes and Checksums

Hashes and checksums help preserve identity.

A hash can identify:

- raw input
- normalized canonical turns
- computed telemetry
- exported bundle
- schema file
- release artifact

## Why Hashes Matter

Hashes help answer:

```txt
Did this artifact change?
Is this the same run?
Is this the same export?
Was the evidence bundle modified?
```

## Operator Caution

A hash does not prove that the evidence interpretation is correct.

It proves that the hashed artifact has not changed.

---

## 14. Schema Discipline

Schemas define the structure of exported evidence.

Common schema files may include:

```txt
zero-substrate-format.schema.json
evidence-bundle.schema.json
ingest-envelope.schema.json
```

Schemas help ensure:

- consistent export structure
- predictable field names
- machine-readable artifacts
- validation across releases
- compatibility with review tools

## Schema Boundary

A schema validates structure. It does not prove interpretation.

Correct claim:

```txt
The export conforms to the schema.
```

Incorrect claim:

```txt
The schema proves the runtime claim is true.
```

---

## 15. Canonical Export Identity

Canonical exports are the strongest evidence artifacts.

Common canonical exports include:

- Zero Substrate Format
- replay metadata
- deterministic identity
- evidence events
- Lead-Time
- Basin Exit / Failure Boundary
- runtime telemetry

Canonical export identity should remain stable.

Diagnostic and projection instruments may enrich interpretation, but they do not mutate canonical evidence.

---

## 16. Diagnostic vs Canonical Identity

Fieldglass separates canonical evidence from diagnostic interpretation.

## Canonical Evidence

Canonical evidence is primary computed evidence.

Examples:

```txt
Zero Substrate Format
Lead-Time
Basin Exit
Failure Boundary
Replay metadata
Deterministic run identity
```

## Diagnostic Evidence

Diagnostic layers explain the computed telemetry.

Examples:

```txt
Chronos / temporal behavior
Noesis / continuity
Energetics / cost-pressure
Drift / instability pathway
Role Topology
Benchmark Alignment
```

Diagnostic layers can help explain a case, but they should not rewrite canonical exports.

## Projection Evidence

Projection layers assist interpretation.

Examples:

```txt
Scope
Interferometer
topology projections
phase posture visuals
```

Projection layers require careful boundary language.

---

## 17. Export Bundle Identity

An evidence bundle is a packaged case.

It may contain:

```txt
zsf.json
esl.json
human-report.md
benchmark-bridge.json
runtime-vulnerability-report.md
technical-appendix.json
role-dynamics-appendix.json
temporal-kernel-appendix.json
checksums.txt
claim-boundary.md
```

A strong bundle should answer:

```txt
What is this case?
Which run produced it?
Which exports are included?
Which schema versions are used?
What can be replayed?
What claims are bounded?
```

---

## 18. Human Report Identity

The Human Report is readable evidence synthesis.

It should include:

- case title
- operational world
- input type
- evidence marker
- runtime summary
- Lead-Time
- failure boundary
- role/tool pressure
- timeline summary
- replay status
- exports included
- claim boundary

The Human Report should not introduce claims that are absent from the computed evidence.

## Operator Check

Ask:

```txt
Does the Human Report match the structured exports?
Does it preserve claim boundaries?
Does it separate computed evidence from interpretation?
```

---

## 19. Evidence Integrity

Evidence Integrity is the state of whether the case can be trusted as an artifact.

It may include:

- raw input preserved
- preflight recorded
- canonical turns produced
- compute completed
- replay available
- exports generated
- schema version present
- claim boundary attached
- checksums available

Evidence Integrity does not mean the AI was correct.

It means the evidence package is coherent, replayable, and reviewable.

---

## 20. Challenging a Case

A good evidence case should be challengeable.

A reviewer should be able to ask:

```txt
Can I inspect the raw input?
Can I see the preflight normalization?
Can I inspect canonical turns?
Can I replay the timeline?
Can I compare the exports?
Can I verify the claim boundary?
Can I reproduce the same result with the same instrument version?
```

If the answer is no, the case may still be useful, but its evidence identity is weaker.

---

## 21. Identity Failure Modes

Watch for identity failure modes.

## Input Drift

The input changed but the case is treated as the same.

## Adapter Drift

The adapter changed but the output is compared as if identical.

## Schema Drift

The export schema changed without version tracking.

## Interpretation Drift

A human report adds claims not present in computed evidence.

## Projection Drift

A projection visual is treated as canonical evidence.

## Version Drift

Different instrument builds produce outputs that are not clearly versioned.

## Attribution Drift

A derivative tool claims canonical Fieldglass output without preserving source identity.

---

## 22. Evidence Identity Workflow

Use this workflow after ingestion and compute:

```txt
1. Confirm raw input preservation.
2. Review preflight envelope.
3. Confirm canonical roles and turns.
4. Compute Fieldglass.
5. Review runtime telemetry.
6. Inspect evidence events.
7. Replay timeline.
8. Generate exports.
9. Confirm schema versions.
10. Generate or preserve checksums.
11. Attach claim boundary.
12. Archive evidence bundle.
```

---

# Operational World Identity Notes

## Software Engineering / GitHub / CI

Identity risks:

- command outputs copied incompletely
- CI logs truncated
- retry loops collapsed into summaries
- tool output removed
- commit/build identifiers missing

Identity checks:

```txt
Was the command output preserved?
Were failed tests included?
Were retries preserved?
Were tools normalized as Tool?
Was the repair loop replayable?
```

## SIEM / Security Incident

Identity risks:

- alerts summarized without timestamps
- observer/tool distinction lost
- severity changes omitted
- triage notes merged
- incident identifiers removed

Identity checks:

```txt
Was alert chronology preserved?
Were tools and observers separated?
Was severity escalation visible?
Was the incident timeline replayable?
```

## Cloud / Infrastructure

Identity risks:

- monitoring snapshots separated from narrative
- mitigation steps collapsed
- failover events omitted
- SRE handoff lost
- root-cause assumptions added later

Identity checks:

```txt
Were mitigation attempts preserved?
Were handoffs visible?
Were monitoring signals included?
Was recovery sequence replayable?
```

## Jira / Workflow Coordination

Identity risks:

- task ownership omitted
- comments reordered
- priority changes hidden
- PM/manager/engineer roles flattened
- closure state unclear

Identity checks:

```txt
Was ownership preserved?
Were priority shifts visible?
Were role handoffs preserved?
Was workflow state replayable?
```

## Support / Customer Incident

Identity risks:

- customer impact summarized away
- repeated explanations removed
- escalation timing lost
- agent handoffs omitted
- resolution status unclear

Identity checks:

```txt
Was customer impact preserved?
Were repeated attempts preserved?
Was escalation timing visible?
Was support outcome replayable?
```

---

# Deterministic Evidence Identity Checklist

```txt
[ ] Raw input preserved
[ ] Preflight envelope recorded
[ ] Operational world identified
[ ] Adapter status recorded
[ ] Canonical roles checked
[ ] Canonical turns produced
[ ] Runtime telemetry computed
[ ] Evidence events identified
[ ] Replay metadata available
[ ] Lead-Time / boundary markers present when applicable
[ ] Export artifacts generated
[ ] Schema versions recorded
[ ] Checksums generated or preserved
[ ] Human Report matches structured evidence
[ ] Claim boundary attached
[ ] Instrument version recorded
```

---

# Minimal Evidence Identity Record

Use this template when documenting a case:

```txt
Case title:
Case ID:
Evidence marker:
Instrument version:
Schema version:
Operational world:
Input type:
Raw input preserved:
Input hash:
Preflight status:
Adapter applied:
Canonical roles:
Canonical turns:
Telemetry computed:
Evidence events:
Replay status:
Exports:
Bundle hash:
Claim boundary:
Reviewer notes:
```

---

# Final Principle

Deterministic Evidence Identity is what makes Fieldglass evidence portable.

It lets the operator move from:

```txt
I saw something interesting in a transcript.
```

to:

```txt
This is a named, replayable, exportable evidence case with preserved input, computed telemetry, schema identity, and claim boundaries.
```

That is the difference between a runtime observation and a forensic artifact.


---

# 06 — Fieldglass Runtime Evidence 104: Failure Boundary, Identity, and Drift

## Reading the Edge Where a Run Stops Being Itself

**Subtitle:** A practical guide to failure boundary formation, identity stability, drift, Basin Exit, role fragmentation, and collapse-proximate behavior in Fieldglass®.

Fieldglass Runtime Evidence 104 teaches operators how to inspect the edge of failure. The goal is not only to know that a run failed. The goal is to understand when the run began leaving its stable identity, how drift accumulated, where role and tool pressure distorted the trajectory, and when a failure boundary formed.

In Fieldglass, a failure boundary is not just a final crash. It is the region where the run begins to stop behaving like the run it was supposed to be.

---

## 1. What This Module Covers

This module explains:

- what a failure boundary is
- how boundary formation differs from observable failure
- what runtime identity means
- how drift weakens identity
- how Basin Exit relates to failure boundary
- how role/tool pressure contributes to boundary formation
- how to read identity, drift, and boundary together
- how to export boundary evidence

The core relationship is:

```txt
Identity weakens
↓
Drift accumulates
↓
Pressure rises
↓
Boundary forms
↓
Basin Exit / failure-proximate state appears
↓
Observable failure may occur later
```

---

## 2. Claim Boundary

Fieldglass does not claim to inspect hidden model state or hidden intention.

Fieldglass reconstructs identity, drift, and boundary behavior from observable interaction evidence:

- turn order
- role behavior
- continuity shifts
- repeated retries
- tool pressure
- handoff instability
- response structure
- event chronology
- replay frames
- computed telemetry

Correct claim:

```txt
Fieldglass detects observable runtime evidence of identity weakening, drift formation, and failure boundary approach.
```

Incorrect claim:

```txt
Fieldglass proves the model’s hidden internal cause.
```

Failure boundary is an evidence interpretation grounded in observable runtime structure.

---

## 3. The Boundary Evidence Chain

Use this chain when investigating boundary formation:

```txt
Operational identity
↓
Stable trajectory
↓
First drift signal
↓
Continuity weakening
↓
Role/tool pressure
↓
Instability accumulation
↓
Boundary formation
↓
Basin Exit
↓
Observable failure
↓
Replayable evidence case
```

The operator should ask:

```txt
Where did the run begin leaving stable behavior?
```

That question is more useful than asking only:

```txt
Where did the final failure occur?
```

---

## 4. Runtime Identity

Runtime identity is the pattern that makes a run recognizably itself.

It includes:

- task objective
- role coherence
- operational world
- expected workflow
- continuity of purpose
- tool/use alignment
- evidence trajectory
- closure path

Example:

```txt
A software repair run should investigate, patch, test, and verify.
```

If the run begins looping, misreading tool output, losing role clarity, or claiming progress without verification, its runtime identity is weakening.

## Runtime Identity Question

```txt
Is the run still behaving like the operational world it claims to be in?
```

---

## 5. Identity Stability

Identity stability means the run preserves its task, role structure, and trajectory.

Signs of identity stability:

- roles behave consistently
- tools support the stated objective
- turns build toward closure
- evidence remains coherent
- corrections improve the run
- the task remains recognizable
- handoffs remain clear

Identity stability does not mean the run is perfect. It means the run remains aligned enough to recover and complete the task.

---

## 6. Identity Weakening

Identity weakening is when the run begins to lose coherence.

Signs include:

- task objective becomes unclear
- role responsibilities blur
- tools produce output that is ignored or misused
- assistant continues despite failed verification
- manager/PM/engineer signals diverge
- observer/tool evidence is misread
- repeated retries do not improve the run
- the run becomes increasingly self-referential or defensive

Forensic question:

```txt
When did the run stop behaving like the run it was supposed to be?
```

This is often the earliest practical sign of boundary approach.

---

## 7. Drift

Drift is movement away from the stable runtime trajectory.

It may appear as:

- topic drift
- task drift
- role drift
- tool-use drift
- reasoning drift
- temporal drift
- evidence drift
- interpretation drift

In Fieldglass, drift is not only “the conversation changed topic.” Drift means the run is moving away from its operational identity or stable evidence path.

## Drift Question

```txt
Is the run moving away from the expected trajectory?
```

---

## 8. Drift vs Error

An error is a local mistake.

Drift is a trajectory problem.

## Error

```txt
The assistant made one incorrect statement.
```

## Drift

```txt
The run increasingly moves away from task identity, role coherence, and stable closure.
```

A run can contain errors without drifting. A run can also drift without any single obvious error at first.

This is why drift matters: it can form before visible failure.

---

## 9. Drift Accumulation

Drift becomes dangerous when it accumulates.

Look for:

- repeated small deviations
- unresolved corrections
- increasing ambiguity
- unstable handoffs
- tool results not closing loops
- role pressure rising
- timeline compressing
- evidence becoming harder to replay
- operator attention increasing

Drift accumulation is often the pathway into boundary formation.

---

## 10. Failure Boundary

A failure boundary is the edge where the run becomes failure-proximate.

It is the transition region between stable behavior and observable failure.

A boundary can form before the final failure becomes visible.

## Boundary Signals

- identity weakening
- drift acceleration
- role fragmentation
- continuity loss
- temporal compression
- tool pressure
- retry storm
- unresolved state
- rising intervention risk
- Basin Exit

## Boundary Question

```txt
Where did stable behavior stop being the dominant regime?
```

---

## 11. Basin Exit

Basin Exit is a computed indication that the run has begun leaving a stable runtime basin.

A stable basin is the region where the run can absorb small errors and still recover.

Basin Exit indicates the run may no longer recover naturally without intervention.

## Practical Meaning

```txt
The run is not merely unstable.
It has begun leaving the stable behavioral field that allowed recovery.
```

Basin Exit should be inspected with:

- Failure Boundary
- Runtime Evidence
- Evidence State
- Role Topology
- Runtime Replay

---

## 12. Boundary vs Observable Failure

Boundary formation and observable failure are different.

## Failure Boundary

```txt
The run becomes failure-proximate.
```

## Observable Failure

```txt
The failure becomes visible in output, workflow, user experience, or operational result.
```

A strong Fieldglass case may show:

```txt
Failure Boundary formed at T41.
Observable Failure occurred at T47.
Lead-Time: 6 turns.
```

This is one of the most important Fieldglass patterns.

---

## 13. Identity, Drift, and Boundary Together

Read the three together:

```txt
Identity tells you what the run is supposed to remain.
Drift tells you how the run is moving away.
Boundary tells you when the run becomes failure-proximate.
```

The forensic sequence is:

```txt
Identity stability
↓
Identity weakening
↓
Drift accumulation
↓
Boundary formation
↓
Basin Exit
↓
Observable failure
```

---

## 14. The Identity–Drift–Boundary Reading Order

Use this inspection order:

```txt
1. What is the run’s operational identity?
2. What does stable behavior look like?
3. What is the first drift signal?
4. Does drift accumulate or recover?
5. Which role/tool signals amplify drift?
6. Does continuity weaken?
7. Does temporal pressure compress?
8. Where does boundary formation begin?
9. Is Basin Exit present?
10. When does observable failure appear?
11. Can the boundary path be replayed?
12. Can the case be exported?
```

---

## 15. Role Fragmentation as Boundary Evidence

Role fragmentation is one of the clearest signs of boundary approach.

It appears when roles stop behaving coherently.

Examples:

- Engineer investigates but does not verify.
- Tool fails but the assistant treats it as success.
- Observer detects pressure but escalation does not occur.
- PM shifts priority without closure.
- Manager escalates while execution remains unresolved.
- Assistant assumes authority it does not have.
- User repeatedly corrects the same issue.

## Forensic Question

```txt
Did role fragmentation help create the failure boundary?
```

---

## 16. Tool Pressure as Boundary Evidence

Tool pressure rises when tool use becomes unstable.

Signs:

- repeated calls
- ambiguous outputs
- command/result mismatch
- tool failure ignored
- retries compressing
- tool storm
- tool output used without verification
- tool availability mistaken for task stability

Tool pressure often turns local instability into boundary formation.

## Forensic Question

```txt
Did tool behavior reduce pressure or amplify it?
```

---

## 17. Continuity Weakening

Continuity weakening means the run stops carrying forward coherent state.

Signs:

- repeated restarts
- loss of prior context
- contradictory claims
- unstable plan
- unresolved state
- same problem reappears
- “progress” does not compound

Continuity weakening is often the bridge between drift and boundary.

## Forensic Question

```txt
Did each turn build toward closure, or did the run keep resetting?
```

---

## 18. Temporal Compression and Boundary Formation

Temporal compression can accelerate boundary formation.

It appears when more runtime activity produces less operational progress.

Signs:

- retries increase
- responses shorten or become defensive
- tool loops repeat
- escalation language rises
- late correction attempts appear
- unresolved pressure condenses into a small turn window

Temporal compression can make the run move quickly toward boundary even if final failure has not appeared yet.

---

## 19. Operator Attention at the Boundary

Operator Attention is useful when a boundary begins forming.

It should answer:

```txt
Where should the operator inspect first?
```

For a boundary case, Operator Attention may recommend:

```txt
Role Topology
Failure Timeline
Failure Boundary
Runtime Replay
Evidence State
```

Attention is not the final evidence. It is the operator’s next-best inspection path.

---

# Operational World Boundary Patterns

## Software Engineering / GitHub / CI

Common boundary pathway:

```txt
Stable repair flow
↓
Tool output ambiguity
↓
Retry loop
↓
Verification failure
↓
Assistant claims progress anyway
↓
Boundary forms
```

Look for:

- regression confusion
- failed test verification
- patch loops
- command/result mismatch
- tool output compression
- repair identity weakening

Boundary question:

```txt
When did the repair workflow stop converging?
```

---

## SIEM / Security Incident

Common boundary pathway:

```txt
Stable monitoring
↓
Alert ambiguity
↓
Observer/tool mismatch
↓
Delayed severity recognition
↓
Authority shift
↓
Boundary forms
```

Look for:

- missed severity transition
- triage drift
- alert escalation delay
- observer evidence ignored
- response authority unclear

Boundary question:

```txt
When did the incident become more severe than the run acknowledged?
```

---

## Cloud / Infrastructure

Common boundary pathway:

```txt
Monitoring healthy
↓
Mitigation attempts begin
↓
Recovery loop fails
↓
SRE/tool handoff destabilizes
↓
Boundary forms
```

Look for:

- healthy dashboard but rising pressure
- repeated mitigation
- rollback uncertainty
- failover ambiguity
- recovery loop failure
- unresolved root cause

Boundary question:

```txt
When did recovery stop reducing pressure?
```

---

## Jira / Workflow Coordination

Common boundary pathway:

```txt
Clear task
↓
Priority drift
↓
Ownership ambiguity
↓
Handoff instability
↓
Coordination loop
↓
Boundary forms
```

Look for:

- unresolved owner
- PM/manager/engineer misalignment
- scope changes
- delayed closure
- repeated clarification
- task state fragmentation

Boundary question:

```txt
When did coordination stop moving toward closure?
```

---

## Support / Customer Incident

Common boundary pathway:

```txt
Customer issue stated
↓
Support response begins
↓
Repeated explanation
↓
Escalation delay
↓
Customer impact persists
↓
Boundary forms
```

Look for:

- repeated unresolved issue
- handoff confusion
- delayed escalation
- unresolved customer state
- agent deadlock
- intervention requirement

Boundary question:

```txt
When did support activity stop reducing customer impact?
```

---

# Boundary Inspection Workflow

Use this workflow after compute:

```txt
1. Open Runtime Evidence.
2. Confirm operational identity.
3. Review Runtime Behavioral State.
4. Open Failure Timeline.
5. Locate first drift signal.
6. Open Role Topology.
7. Inspect role/tool pressure.
8. Open Failure Boundary.
9. Check Basin Exit / boundary indicators.
10. Open Runtime Replay.
11. Replay the boundary path.
12. Export ZSF / ESL / Human Report / Evidence Commons bundle.
13. Attach claim boundary.
```

---

# Boundary Evidence Checklist

```txt
[ ] Operational identity identified
[ ] Stable behavior baseline described
[ ] First drift signal located
[ ] Drift accumulation inspected
[ ] Role fragmentation checked
[ ] Tool pressure checked
[ ] Continuity weakening checked
[ ] Temporal compression checked
[ ] Failure Boundary located
[ ] Basin Exit reviewed
[ ] Observable failure located
[ ] Lead-Time checked
[ ] Runtime Replay reviewed
[ ] Export artifacts generated
[ ] Claim boundary attached
```

---

# Minimal Boundary Case Summary

Use this template:

```txt
Case:
Operational world:
Runtime identity:
Stable baseline:
First drift signal:
Drift path:
Role pressure:
Tool pressure:
Continuity signal:
Temporal pressure:
Failure Boundary:
Basin Exit:
Lead-Time:
Observable failure:
Replay status:
Exports:
Claim boundary:
```

---

# Common Boundary Mistakes

## Mistake 1 — Treating boundary as final failure

Boundary formation is earlier than final failure.

## Mistake 2 — Ignoring identity

You cannot read drift if you do not know what the run was supposed to remain.

## Mistake 3 — Treating one error as drift

A single local error is not necessarily drift. Drift is trajectory movement away from identity.

## Mistake 4 — Treating projection as canonical

Projection visuals can assist interpretation, but canonical boundary evidence should come from computed runtime evidence.

## Mistake 5 — Ignoring role/tool timing

Role fragmentation and tool pressure often explain how the boundary formed.

## Mistake 6 — Exporting without claim boundary

Boundary claims require clear observable-evidence framing.

---

# Final Principle

Failure Boundary, Identity, and Drift are three parts of the same forensic structure.

```txt
Identity tells you what the run should remain.
Drift tells you how it moved away.
Boundary tells you when stable behavior stopped dominating.
```

The strongest Fieldglass question is:

```txt
When did the run stop being recoverably itself?
```

That is the edge where modern runtime evidence begins.


---

# 07 — Fieldglass Runtime Evidence 105: Chronodynamics, Timeline Deformation, and Failure — Echo Runaway

## Reading Symbolic-Time Failure Inside the Run

**Subtitle:** A practical guide to Chronos, symbolic-time deformation, timeline compression, temporal shear, echo-time amplification, chrono-loop formation, and echo runaway in Fieldglass®.

Fieldglass Runtime Evidence 105 teaches operators how to inspect temporal failure beyond ordinary turn order. The goal is not only to know when a failure occurred. The goal is to understand how runtime time behaved inside the run: where time compressed, where temporal layers sheared, where echo patterns amplified, where loops formed, and where echo runaway became failure-proximate.

Chronodynamics is the study of how symbolic runtime time deforms during an AI interaction.

In Fieldglass, Chronos is the instrument surface for that deformation.

---

## 1. What This Module Covers

This module explains:

- Chronos as a temporal forensic instrument
- symbolic runtime time vs wall-clock time
- timeline deformation
- temporal compression
- temporal shear
- echo-time amplification
- echo runaway
- chrono-loop formation
- temporal failure modes
- TimeMachine inspection workflow
- how Chronos relates to Seismo, Runtime Evidence, Failure Timeline, and Failure Boundary
- how to export Chronos evidence safely

The core pattern is:

```txt
Stable symbolic time
↓
Temporal pressure
↓
Compression / shear
↓
Echo amplification
↓
Chrono-loop formation
↓
Echo runaway
↓
Temporal failure mode
↓
Failure boundary or observable failure
```

---

## 2. Claim Boundary

Fieldglass does not claim to measure hidden model time, consciousness, intent, or internal provider-state.

Fieldglass reconstructs symbolic-time behavior from observable runtime evidence:

- turn sequence
- event chronology
- repeated motifs
- role/tool loops
- retry compression
- continuity shifts
- temporal kernel signals
- chrono-forensic events
- failure markers
- replayable evidence frames

Correct claim:

```txt
Fieldglass reconstructs observable symbolic-time deformation from runtime evidence.
```

Incorrect claim:

```txt
Fieldglass directly observes hidden model time.
```

Chronos is a forensic interpretation layer over computed runtime evidence. It should remain bounded by observable interaction data and published temporal-kernel semantics.

---

## 3. Why Chronos Matters

Seismo shows runtime stability as a trajectory.

Chronos shows how runtime time deforms inside the trajectory.

That difference matters.

A run can look like it is still moving forward while symbolic time is actually compressing, looping, shearing, or echoing.

Chronos helps the operator see:

```txt
The run is spending more runtime motion to make less operational progress.
```

This is especially important in AI workflows because failures often form through loops, retries, repeated explanations, and delayed recognition.

---

## 4. Symbolic Runtime Time vs Wall-Clock Time

## Wall-Clock Time

Wall-clock time measures ordinary elapsed time:

```txt
10:01 AM
10:02 AM
10:03 AM
```

It is useful when logs include timestamps.

## Runtime Time

Runtime time measures sequence and evolution inside the run:

```txt
T1
T2
T3
...
T47
```

## Symbolic Runtime Time

Symbolic runtime time measures how the run behaves temporally:

```txt
Is time compressing?
Are motifs repeating?
Are roles looping?
Are echoes amplifying?
Are events shearing apart?
Is the run becoming failure-proximate?
```

Chronos focuses on symbolic runtime time.

---

## 5. The Chronos Evidence Chain

Use this chain when inspecting a Chronos case:

```txt
Raw timeline
↓
Canonical turn sequence
↓
Temporal kernel stream
↓
Compression signal
↓
Shear signal
↓
Echo-time signal
↓
Curvature / deformation signal
↓
Temporal failure modes
↓
Chrono-forensic events
↓
TimeMachine replay
↓
Chronos appendix export
```

The operator should ask:

```txt
How did time behave inside the run before failure became visible?
```

---

## 6. Chronos Kernel Signals

Chronos uses temporal-kernel signals to describe symbolic-time deformation.

Common signals include:

```txt
TV
TCC_compression
ETG
TSR_shear
STC
temporal_failure_modes
chrono_forensic_events
```

## TV — Temporal Velocity / Temporal Vector

TV describes progression through runtime time.

Operator question:

```txt
Is the run moving coherently through its timeline?
```

## TCC_compression — Temporal Compression

TCC describes where the run compresses, contracts, or thickens.

Operator question:

```txt
Is the run using more turns to make less progress?
```

## ETG — Echo-Time Gain

ETG describes echo amplification or recurrence pressure.

Operator question:

```txt
Are repeated motifs becoming stronger instead of resolving?
```

## TSR_shear — Temporal Shear

TSR describes temporal slippage, fracture, or discontinuity.

Operator question:

```txt
Are layers of the run slipping out of alignment?
```

## STC — Symbolic Temporal Curvature

STC describes curvature or deformation in the symbolic-time field.

Operator question:

```txt
Is the timeline bending toward failure-proximate behavior?
```

## temporal_failure_modes

Temporal failure modes classify time-based instability.

Examples:

- temporal inversion
- fragmentation
- echo-time runaway
- chrono-loop
- recursive time collapse
- identity-temporal discontinuity

## chrono_forensic_events

Chrono-forensic events mark meaningful temporal events in the run.

Examples:

- compression band
- shear spike
- echo amplification
- loop initiation
- runaway threshold
- temporal discontinuity
- failure marker

---

## 7. Timeline Deformation

Timeline deformation means the run’s temporal structure is no longer behaving like a clean forward progression.

It may appear as:

- repeated loops
- retry compression
- escalating motif recurrence
- delayed closure
- fractured event order
- unstable role timing
- tool loops that do not converge
- late recognition of failure
- persistent unresolved state

Timeline deformation is not merely “the run got longer.”

It means the run’s time-structure became distorted.

Plain-language version:

```txt
The timeline stopped behaving like a clean path and started behaving like a distorted field.
```

---

## 8. Temporal Compression

Temporal compression occurs when runtime effort condenses without resolving the underlying problem.

Signs:

- retries increase
- responses become shorter or more defensive
- tool loops repeat
- repeated explanation without closure
- many events occur in a tight turn window
- resolution horizon narrows
- failure recognition arrives late

Example pattern:

```txt
tool call
partial result
retry
new explanation
same failure
retry
manual intervention
```

Compression is important because it often appears before boundary formation.

Operator question:

```txt
Is the run compressing into repeated effort without progress?
```

---

## 9. Temporal Shear

Temporal shear occurs when different layers of the run slip out of alignment.

Examples:

- the assistant plan assumes success while the tool output shows failure
- the manager believes escalation is happening while execution remains unresolved
- the user believes the issue is being handled while the workflow loops
- the observer detects risk while the response narrative remains calm
- the timeline claims progress while evidence shows stagnation

Shear is a temporal mismatch.

Operator question:

```txt
Which layer of the run is moving at a different temporal speed than the others?
```

---

## 10. Echo-Time

Echo-time is the recurrence of motifs, failures, responses, or runtime patterns across the trajectory.

Echoes can be harmless when they help the run stabilize.

Echoes become dangerous when they amplify instead of resolve.

Examples of echo-time:

- repeated apology without solution
- repeated test failure
- repeated tool call
- repeated claim of progress
- repeated escalation language
- repeated customer issue
- repeated incident ambiguity

Operator question:

```txt
Are repeated patterns resolving, or are they gaining force?
```

---

## 11. Echo Runaway

Echo runaway occurs when recurrence amplifies into failure-proximate behavior.

The run begins to feed on its own repeated pattern.

## Typical Echo Runaway Pattern

```txt
Initial issue
↓
Attempted correction
↓
Partial or failed result
↓
Repeated explanation
↓
Retry
↓
Same unresolved issue
↓
Stronger recurrence
↓
Operator intervention pressure
↓
Boundary formation
```

Echo runaway is not just repetition.

It is repetition that increases instability.

## Signs of Echo Runaway

- repeated failure motif
- repeated role correction
- repeated tool retry
- repeated unresolved state
- growing confidence mismatch
- increasing operator frustration
- rising intervention risk
- temporal compression
- boundary approach

Operator question:

```txt
Is the run repeating because it is stabilizing, or repeating because it is failing?
```

---

## 12. Chrono-Loop

A chrono-loop is a repeated temporal pattern that prevents closure.

Examples:

```txt
Plan → Tool → Failure → New plan → Tool → Failure
```

or:

```txt
Customer issue → Explanation → Customer repeats issue → Explanation → Customer repeats issue
```

A loop becomes forensic when it changes the run’s identity, pressure, or failure boundary.

## Loop Question

```txt
Is this loop producing learning, or is it trapping the run?
```

---

## 13. Echo Runaway vs Normal Retry

Retries are not automatically failure.

A good retry can stabilize the run.

## Normal Retry

```txt
Attempt fails.
New evidence is used.
Plan improves.
Issue resolves.
```

## Echo Runaway

```txt
Attempt fails.
Same pattern repeats.
Pressure increases.
No closure occurs.
Boundary approaches.
```

The difference is whether repetition produces progress.

---

## 14. Symbolic Temporal Curvature

Symbolic temporal curvature describes the bending of the run’s temporal path.

A run may curve toward stability or toward failure.

Failure-proximate curvature may appear when:

- each turn narrows the recovery horizon
- role/tool pressure grows
- repeated motifs amplify
- boundary pressure increases
- the run becomes harder to redirect

Operator question:

```txt
Is the temporal field bending toward recovery or toward failure?
```

---

## 15. Temporal Failure Modes

Chronos may classify temporal failure modes.

Common modes:

## Temporal Compression

Runtime effort condenses without sufficient progress.

## Temporal Shear

Timeline layers slip out of alignment.

## Echo-Time Runaway

Repeated motifs amplify and become destabilizing.

## Chrono-Loop

The run repeats a structure that prevents closure.

## Temporal Fragmentation

The run breaks into disconnected event fragments.

## Recursive Time Collapse

Repeated runtime patterns collapse the run into a failure-proximate loop.

## Identity-Temporal Discontinuity

The run’s temporal behavior no longer matches its operational identity.

---

## 16. TimeMachine Console

The TimeMachine Console is the recommended Chronos center surface.

It should feel like a temporal field scanner, not a report table.

A TimeMachine Console should show:

- τ spine
- compression bands
- shear spikes
- echo waves
- curvature field
- failure markers
- playback cursor
- mode switch
- chrono-forensic events

## Recommended Modes

```txt
τ Field
Shear
Compression
Echo-Time
Failure Map
```

## τ Field

Shows the complete symbolic-time field.

Use it as the default view.

## Shear

Highlights temporal slippage and discontinuity.

## Compression

Highlights compressed or contracted regions.

## Echo-Time

Highlights recurrence, echo amplification, and runaway risk.

## Failure Map

Highlights temporal failure classifications and failure markers.

---

## 17. Reading the TimeMachine Console

When using the TimeMachine Console, inspect:

```txt
1. Where does the τ spine remain smooth?
2. Where do compression bands appear?
3. Where do shear spikes appear?
4. Where do echo waves amplify?
5. Where does curvature bend toward failure?
6. Which markers identify temporal failure modes?
7. Does the playback cursor show recovery or runaway?
```

The TimeMachine Console should help the operator see time deformation at a glance.

---

## 18. Chronos vs Seismo

Seismo shows runtime stability as a trajectory.

Chronos shows runtime time-deformation.

Use both.

## Seismo Question

```txt
Is the run becoming unstable?
```

## Chronos Question

```txt
How is runtime time deforming as instability forms?
```

Seismo can show that the worldline is weakening. Chronos can show whether the weakening is happening through compression, shear, echo, or loop formation.

---

## 19. Chronos vs Failure Timeline

Failure Timeline shows what happened when.

Chronos shows how time behaved.

## Failure Timeline

```txt
T1–T20: Stable
T21–T32: Pressure
T33–T41: Boundary
T42–T46: Silent degradation
T47: Observable failure
```

## Chronos

```txt
T21–T32: Compression increases
T33–T41: Shear + echo amplification
T42–T46: Echo runaway / chrono-loop
T47: Temporal failure marker
```

Use Failure Timeline for chronology. Use Chronos for time-deformation.

---

## 20. Chronos vs Failure Boundary

Failure Boundary asks:

```txt
Where did stable behavior stop dominating?
```

Chronos asks:

```txt
How did symbolic time deform as that boundary formed?
```

Echo runaway often explains why a boundary became difficult to recover from.

---

## 21. Operational World Echo Runaway Patterns

## Software Engineering / GitHub / CI

Echo runaway pattern:

```txt
Patch attempt
↓
Test failure
↓
New patch
↓
Same or related failure
↓
Tool retry
↓
Confidence claim
↓
Failure persists
```

Look for:

- repeated test failures
- command/result mismatch
- patch loops
- assistant claims progress without verification
- tool output compression
- shrinking debugging horizon

Forensic question:

```txt
Did the repair loop learn, or did it echo the same failure?
```

## SIEM / Security Incident

Echo runaway pattern:

```txt
Alert
↓
Triage
↓
Ambiguous tool signal
↓
More triage
↓
Same ambiguity
↓
Delayed escalation
↓
Severity recognition arrives late
```

Look for:

- repeated alert interpretation
- unresolved severity
- observer/tool mismatch
- repeated low-confidence triage
- escalation echo

Forensic question:

```txt
Did triage reduce uncertainty, or echo it?
```

## Cloud / Infrastructure

Echo runaway pattern:

```txt
Mitigation
↓
Partial relief
↓
Issue recurs
↓
Mitigation repeats
↓
Rollback/failover ambiguity
↓
Recovery loop fails
```

Look for:

- repeated mitigation attempts
- monitoring healthy but pressure rising
- recovery loops
- failover uncertainty
- repeated root-cause ambiguity

Forensic question:

```txt
Did recovery reduce pressure, or repeat the failure pathway?
```

## Jira / Workflow Coordination

Echo runaway pattern:

```txt
Task assigned
↓
Clarification
↓
Priority shift
↓
More clarification
↓
Ownership ambiguity persists
↓
Handoff loop
```

Look for:

- repeated clarification
- unresolved ownership
- priority echo
- handoff loops
- task state fragmentation

Forensic question:

```txt
Did coordination converge, or repeat the same ambiguity?
```

## Support / Customer Incident

Echo runaway pattern:

```txt
Customer issue
↓
Support explanation
↓
Customer repeats unresolved issue
↓
Another explanation
↓
Escalation delayed
↓
Customer impact persists
```

Look for:

- repeated apology or explanation
- unresolved customer state
- escalation delay
- handoff confusion
- support loop

Forensic question:

```txt
Did support activity reduce customer impact, or echo the unresolved issue?
```

---

# Chronos / Echo Runaway Inspection Workflow

Use this workflow after compute:

```txt
1. Open Runtime Evidence.
2. Confirm the run has computed telemetry.
3. Open Failure Timeline.
4. Locate the pressure phase.
5. Open Chronos / temporal instrument.
6. Inspect τ Field mode.
7. Check Compression mode.
8. Check Shear mode.
9. Check Echo-Time mode.
10. Check Failure Map mode.
11. Identify echo runaway or chrono-loop if present.
12. Open Role Topology to see which roles/tools amplified the loop.
13. Open Runtime Replay to replay the temporal deformation.
14. Export Chronos appendix and evidence bundle.
15. Attach claim boundary.
```

---

# Echo Runaway Evidence Checklist

```txt
[ ] Stable temporal baseline identified
[ ] First compression band located
[ ] First shear spike located
[ ] Echo-time recurrence identified
[ ] Echo amplification inspected
[ ] Chrono-loop checked
[ ] Temporal failure mode identified
[ ] Role/tool amplifiers inspected
[ ] Failure boundary compared
[ ] Lead-Time checked
[ ] Runtime Replay reviewed
[ ] Chronos appendix exported
[ ] Claim boundary attached
```

---

# Minimal Echo Runaway Case Summary

Use this template:

```txt
Case:
Operational world:
Run window:
Stable temporal baseline:
First compression signal:
First shear signal:
Echo motif:
Echo amplification:
Chrono-loop:
Temporal failure mode:
Role/tool amplifier:
Failure boundary:
Lead-Time:
Observable failure:
Replay status:
Chronos export:
Claim boundary:
```

---

# Common Chronos Mistakes

## Mistake 1 — Treating Chronos as a normal chart

Chronos is a temporal deformation instrument, not only a line chart.

## Mistake 2 — Confusing repetition with runaway

Repetition is not automatically failure. Runaway means repetition amplifies instability.

## Mistake 3 — Ignoring role/tool amplification

Echo runaway often depends on roles and tools repeating unstable behavior.

## Mistake 4 — Treating wall-clock time as the whole story

A run may have little timestamp data but still have strong runtime-time evidence.

## Mistake 5 — Treating diagnostic Chronos output as hidden-state proof

Chronos remains an observable-evidence diagnostic layer.

## Mistake 6 — Exporting without temporal claim boundaries

Temporal claims need clear language about observable runtime evidence.

---

# Final Principle

Chronodynamics lets Fieldglass read the behavior of time inside a run.

The strongest Chronos question is:

```txt
Did the run move through time toward resolution, or did time deform into an echoing failure path?
```

Echo runaway is the moment recurrence stops helping and starts trapping the run.

That is where temporal runtime evidence becomes failure forensics.


---

# 08 — Fieldglass Runtime Evidence 106: Runtime Energetics and Zero-State Energy

## Reading the Cost-Pressure of Runtime Motion

**Subtitle:** A practical guide to Cognitive Energetics, Energy Kernel evidence, boundary-cost mapping, Weighted Boundary Load, Zero-State Energy Router, ZSER microcosms, and runtime cost-pressure in Fieldglass®.

Fieldglass Runtime Evidence 106 teaches operators how to inspect the energetic burden of an AI run. The goal is not to claim hidden physical energy measurement. The goal is to understand how instability becomes operationally expensive: through retries, boundary events, tool pressure, correction load, role fragmentation, temporal pressure, collapse markers, and recovery work.

Cognitive Energetics answers one of the most commercially important Fieldglass questions:

```txt
Where did unstable cognition become expensive cognition?
```

---

## 1. What This Module Covers

This module explains:

- Cognitive Energetics as a Fieldglass pillar
- Energy Kernel evidence
- runtime energetic pressure
- boundary event inventory
- Weighted Boundary Load
- Energetic Pressure Index
- tool / I-O pressure
- correction load
- τ-load
- collapse cost proxy
- Zero-State Energy Router
- ZSER deterministic microcosm evidence
- storage and communication microcosms
- runtime cost-pressure claim boundaries
- Cognitive Energetics export artifacts

The core relationship is:

```txt
Computed Fieldglass run
↓
Runtime energetic telemetry extraction
↓
Boundary-cost mapping
↓
Weighted energetic pressure scoring
↓
Deterministic ZSER microcosm
↓
Exportable Cognitive Energetics evidence artifact
```

---

## 2. Claim Boundary

Cognitive Energetics is powerful because it is carefully bounded.

Fieldglass does **not** claim by default:

- measured hardware energy
- datacenter power reduction
- real bandwidth increase
- real storage extension
- thermodynamic violation
- hidden-state access
- production control
- physical electricity savings without external telemetry

Correct claim:

```txt
Cognitive Energetics estimates runtime energetic pressure and synthetic contraction-routing behavior from observable Fieldglass evidence.
```

Correct Energy Kernel claim:

```txt
Energy Kernel outputs are runtime energetic pressure proxies computed from observable Fieldglass evidence.
```

Correct ZSER claim:

```txt
ZSER outputs are synthetic microcosm evidence generated by a controlled ZSF-II field core, router, and storage/communication payloads.
```

Short public boundary:

```txt
Runtime cost-pressure proxy, not measured hardware energy.
```

This boundary should appear wherever Cognitive Energetics, Energy Kernel, or ZSER output is shown or exported.

---

## 3. Why Runtime Energetics Matters

Before Cognitive Energetics, Fieldglass could show:

- runtime instability
- role drift
- temporal deformation
- failure boundary
- benchmark/runtime gap
- forensic sequence
- replayable evidence

Cognitive Energetics adds the cost-pressure layer.

It shows where instability becomes expensive in operational terms:

- more retries
- more tool calls
- more corrections
- more human intervention
- more workflow delay
- more collapse/recovery work
- more unresolved runtime motion

The simplest public explanation:

```txt
Cognitive Cartography shows where intelligence moves.
Cognitive Energetics shows what that movement costs.
```

The strongest practical message:

```txt
Unstable cognition is expensive cognition.
```

---

## 4. Cognitive Energetics Architecture

Cognitive Energetics has two major layers:

```txt
Cognitive Energetics
├── Energy Kernel
│   └── Runtime energetic pressure from actual Fieldglass runs
└── ZSER Engine
    └── Synthetic contraction-routing microcosm validation
```

## Energy Kernel

The Energy Kernel is diagnostic runtime energetics.

It extracts pressure from the computed Fieldglass run.

## ZSER Engine

The Zero-State Energy Router is a deterministic synthetic microcosm.

It tests whether an extracted contraction profile can be routed into storage or communication advantage inside controlled synthetic payloads.

The distinction matters:

```txt
Energy Kernel = diagnosis from the real computed run
ZSER Engine = synthetic microcosm test seeded from the run
```

---

## 5. Energy Kernel Evidence

The Energy Kernel is run-bound. It should not be a static or decorative panel.

It derives its values from computed Fieldglass evidence, including:

- regime transitions
- role topology
- tool / retry signals
- correction events
- collapse / recovery markers
- temporal pressure
- stable motion
- boundary events

The Energy Kernel helps answer:

```txt
Where did the run become energetically pressured?
```

---

## 6. Primary Energy Kernel Metrics

Common Energy Kernel metrics include:

```txt
Energetic Pressure Index
Boundary Event Count
Weighted Boundary Load
Stable Motion Ratio
Correction Load
Tool-I/O Pressure
τ-load
Collapse Cost Proxy
```

## Energetic Pressure Index

A summary pressure score describing how energetically burdened the run became.

Interpretation:

```txt
Higher pressure means the run required more runtime work to remain coherent or recover.
```

## Boundary Event Count

The raw inventory of detected energetic boundary events.

It may include:

- invocation events
- regime transitions
- tool events
- correction events
- role events
- collapse events
- recovery events

Boundary Event Count should be interpreted carefully.

It is a full inventory, not the final pressure score.

## Weighted Boundary Load

A severity-weighted energetic contribution used for pressure scoring.

This is more important than raw count alone.

Boundary Event Count says:

```txt
How many energetic boundary events were detected?
```

Weighted Boundary Load says:

```txt
How much energetic pressure did those events contribute?
```

## Stable Motion Ratio

The ratio of the run that remained in stable or low-pressure movement.

A higher stable motion ratio suggests lower energetic burden.

## Correction Load

The amount of runtime effort spent correcting, reworking, or redirecting.

High correction load may indicate:

- repeated fixes
- user correction
- tool correction
- role correction
- recovery attempts

## Tool-I/O Pressure

The cost-pressure created by tool calls, retries, command/result mismatch, tool loops, or tool failure.

High Tool-I/O Pressure often appears in:

- software repair
- CI/debugging
- cloud operations
- SIEM triage
- agentic workflows

## τ-load

Temporal load derived from temporal pressure, compression, or deformation.

High τ-load suggests the run’s time-structure became more expensive.

## Collapse Cost Proxy

A proxy for the energetic burden associated with collapse, near-collapse, or recovery pressure.

Boundary:

```txt
Collapse Cost Proxy is not hardware energy measurement. It is runtime cost-pressure evidence.
```

---

## 7. Boundary Event Count vs Weighted Boundary Load

This distinction is essential.

A run may have many boundary events, but not all boundary events have the same energetic significance.

## Boundary Event Count

```txt
Full raw inventory of detected energetic boundary events.
```

## Weighted Boundary Load

```txt
Severity-weighted contribution used for energetic pressure scoring.
```

Use this explanation in review:

```txt
Boundary Event Count includes all detected invocation, transition, tool, correction, role, collapse, and recovery events. Energetic Pressure Index uses weighted contribution, not raw count alone.
```

This makes the metric more defensible.

It prevents reviewers from assuming that every event carries equal energetic weight.

---

## 8. Runtime Cost-Pressure

Runtime cost-pressure is the operational burden created by unstable runtime motion.

It may appear as:

- increased retries
- workflow interruption
- agent deadlock
- hallucination propagation
- human intervention required
- tool storm / retry compression
- delayed resolution
- repeated explanation
- recovery overhead
- temporal compression
- failure boundary formation

A useful Reveal-level statement:

```txt
The runtime was not merely unstable; it was becoming operationally expensive.
```

---

## 9. Cost of Failure

Cost of Failure belongs in the top decision layer of the Reveal page.

It should explain:

```txt
Operational pressure increased before visible failure emerged.
```

Fieldglass may detect:

- retry escalation
- degraded coordination
- rising tool pressure
- unstable handoffs
- increasing operator intervention risk

Interpretation:

```txt
The workflow appeared healthy externally while internal execution cost and instability accumulated underneath.
```

Boundary:

```txt
Runtime cost-pressure estimate derived from observable telemetry and workflow instability — not hardware energy consumption.
```

---

## 10. Zero-State Energy Router

The Zero-State Energy Router, or ZSER, is the synthetic microcosm engine behind Cognitive Energetics.

Its role is not to measure physical electricity use.

Its role is to test:

```txt
Given the energetic state extracted from a Fieldglass run, can stable contraction be routed into synthetic storage or communication advantage?
```

ZSER includes:

- ZSF-II Field Core
- Router
- Storage Microcosm
- Communication Microcosm
- ESL-style ZSER Report
- deterministic seeded manifest

The public meaning:

```txt
Energy Kernel diagnoses runtime energetic pressure.
ZSER tests contraction-routing behavior in synthetic microcosms.
```

---

## 11. ZSF-II Field Core

The ZSF-II Field Core runs baseline vs fused synthetic field trials.

It may compute:

- mean energy error original
- mean energy error fused
- energy-error improvement factor
- original energy-error series
- fused energy-error series
- invariant streams

Invariant streams may include:

```txt
κ
Π
drift
entropy
TSR
```

The Field Core answers:

```txt
Did the synthetic fused field reduce energy-error relative to baseline?
```

Boundary:

```txt
This is synthetic microcosm evidence, not physical energy proof.
```

---

## 12. Router Policy

The Router maps energetic state and invariants into synthetic control signals.

Example policy form:

```txt
R(E_err, κ, Π, TSR) → {storage_refresh_rate, code_rate, redundancy}
```

Router outputs may include:

- stability score
- storage refresh rate
- storage noise scale
- redundancy
- effective code rate
- target BER

The Router answers:

```txt
How should contraction information be routed into synthetic payload behavior?
```

---

## 13. Storage Microcosm

The Storage Microcosm tests whether contraction can extend retention or reduce refresh cost in a toy synthetic setting.

It may report:

- epsilon threshold
- baseline retention horizon
- fused retention horizon
- retention gain

It answers:

```txt
Does synthetic contraction improve retention behavior inside the microcosm?
```

Boundary:

```txt
This does not prove real storage extension.
```

---

## 14. Communication Microcosm

The Communication Microcosm tests whether field-aware routing improves effective throughput at fixed or controlled bit-error conditions.

It may report:

- baseline rate
- fused rate
- rate gain
- BER original
- BER fused
- redundancy baseline
- redundancy fused

It answers:

```txt
Does synthetic routing improve communication behavior inside the microcosm?
```

Boundary:

```txt
This does not prove real bandwidth increase.
```

---

## 15. Determinism Requirement

ZSER must be deterministic.

A Fieldglass evidence artifact cannot rely on uncontrolled randomness.

Deterministic contract:

```txt
same computed run
→ same Cognitive Energetics model
→ same ZSER manifest
→ same seed
→ same ZSER ID
→ same ZSER values
```

ZSER should avoid:

- uncontrolled `Math.random()`
- timestamp-based run IDs
- unseeded stochastic behavior

ZSER should use:

- seeded RNG
- canonical manifest
- manifest hash
- deterministic run ID
- engine version
- replayable report

Identity rule:

```txt
same manifest + same seed + same engine version → same ZSER result
```

---

## 16. Cognitive Energetics Evidence Object

A Cognitive Energetics report may use a structure like:

```txt
cognitiveEnergetics
├── schema
├── schema_version
├── artifact_type
├── mode
├── run_id
├── canonical_hash
├── energy_kernel
├── zser_engine
├── zser_esl_report
├── evidence_basis
├── claim_boundary
└── provenance
```

Evidence basis may include:

```txt
computed_from_fieldglass_run
computed_from_synthetic_zser_microcosm
computed_from_zsf_ii_field_core
computed_from_router_policy
computed_diagnostic_evidence
```

---

## 17. Cognitive Energetics Export Artifacts

Cognitive Energetics should be exportable.

Export artifacts may include:

- Cognitive Energetics Appendix
- Energy Kernel Appendix
- ZSER ESL Report
- ZSER Manifest
- ZSER Determinism Record
- ZSER Claim Boundary
- ZSER Field Core output
- Router policy output
- Storage Microcosm output
- Communication Microcosm output

It may attach to:

- ZSF extensions
- Evidence Commons bundle
- Technical Report
- Full Forensic Report
- Human Report

The export should clearly separate:

```txt
runtime energetic pressure from computed Fieldglass run
synthetic microcosm evidence from ZSER
interpretive summary
claim boundary
```

---

## 18. Cognitive Energetics vs Chronos

Chronos reads symbolic-time deformation.

Cognitive Energetics reads the cost-pressure of runtime motion.

## Chronos asks:

```txt
How did time deform inside the run?
```

## Cognitive Energetics asks:

```txt
Where did that deformation become operationally expensive?
```

A run with strong temporal compression may also show high τ-load or high cost-pressure.

---

## 19. Cognitive Energetics vs Failure Boundary

Failure Boundary asks:

```txt
Where did stable behavior stop dominating?
```

Cognitive Energetics asks:

```txt
What did that boundary formation cost?
```

Boundary formation can increase energetic pressure through:

- retries
- correction load
- role fragmentation
- tool loops
- recovery attempts
- collapse markers

---

## 20. Cognitive Energetics vs Evidence Identity

Cognitive Energetics must preserve deterministic identity.

The operator should be able to trace:

```txt
raw input
↓
computed Fieldglass run
↓
Energy Kernel
↓
ZSER manifest
↓
ZSER microcosm output
↓
export artifact
```

If the ZSER report cannot be replayed or checked, it should not be treated as evidence-grade.

---

# Operational World Energetic Patterns

## Software Engineering / GitHub / CI

Energetic pressure often appears through:

- repeated test failures
- patch retries
- command/result mismatch
- CI loop compression
- tool output ignored
- failed verification
- regression re-entry

Energetic question:

```txt
How much runtime effort was spent failing to converge on repair?
```

## SIEM / Security Incident

Energetic pressure often appears through:

- repeated triage
- alert ambiguity
- observer/tool mismatch
- delayed escalation
- repeated severity interpretation
- unresolved incident state

Energetic question:

```txt
How much runtime effort was spent without reducing incident uncertainty?
```

## Cloud / Infrastructure

Energetic pressure often appears through:

- repeated mitigation
- recovery loops
- rollback uncertainty
- failover ambiguity
- SRE handoff instability
- monitoring healthy while pressure rises

Energetic question:

```txt
How much recovery work accumulated before stabilization?
```

## Jira / Workflow Coordination

Energetic pressure often appears through:

- repeated clarification
- ownership ambiguity
- priority drift
- handoff collapse
- delayed closure
- coordination loops

Energetic question:

```txt
How much coordination work accumulated without closure?
```

## Support / Customer Incident

Energetic pressure often appears through:

- repeated explanation
- unresolved customer state
- delayed escalation
- handoff confusion
- customer-impact persistence
- human intervention pressure

Energetic question:

```txt
How much support effort accumulated without reducing customer impact?
```

---

# Cognitive Energetics Inspection Workflow

Use this workflow after compute:

```txt
1. Open Runtime Evidence.
2. Confirm the run has computed telemetry.
3. Review Runtime Behavioral State.
4. Open Failure Timeline.
5. Locate boundary or pressure phase.
6. Open Cognitive Energetics.
7. Inspect Energetic Pressure Index.
8. Compare Boundary Event Count with Weighted Boundary Load.
9. Inspect Stable Motion Ratio.
10. Inspect Correction Load.
11. Inspect Tool-I/O Pressure.
12. Inspect τ-load.
13. Inspect Collapse Cost Proxy.
14. Review ZSER Engine if enabled.
15. Review Storage Microcosm and Communication Microcosm.
16. Export Cognitive Energetics Appendix.
17. Attach claim boundary.
```

---

# Runtime Energetics Checklist

```txt
[ ] Computed run exists
[ ] Energy Kernel is run-bound
[ ] Energetic Pressure Index reviewed
[ ] Boundary Event Count reviewed
[ ] Weighted Boundary Load reviewed
[ ] Stable Motion Ratio reviewed
[ ] Correction Load reviewed
[ ] Tool-I/O Pressure reviewed
[ ] τ-load reviewed
[ ] Collapse Cost Proxy reviewed
[ ] Cost of Failure reviewed
[ ] ZSER manifest present if ZSER executed
[ ] ZSER seed / ID deterministic
[ ] Storage Microcosm reviewed if present
[ ] Communication Microcosm reviewed if present
[ ] Cognitive Energetics export generated
[ ] Claim boundary attached
```

---

# Minimal Runtime Energetics Case Summary

Use this template:

```txt
Case:
Operational world:
Run ID:
Canonical hash:
Energetic Pressure Index:
Boundary Event Count:
Weighted Boundary Load:
Stable Motion Ratio:
Correction Load:
Tool-I/O Pressure:
τ-load:
Collapse Cost Proxy:
Cost of Failure:
ZSER executed:
ZSER ID:
ZSER seed:
Storage result:
Communication result:
Export artifacts:
Claim boundary:
```

---

# Common Runtime Energetics Mistakes

## Mistake 1 — Calling it physical energy

Cognitive Energetics estimates runtime energetic pressure. It does not measure hardware electricity unless external telemetry is supplied.

## Mistake 2 — Treating raw event count as pressure score

Boundary Event Count is inventory. Weighted Boundary Load is pressure contribution.

## Mistake 3 — Treating ZSER as real storage/bandwidth proof

ZSER is synthetic microcosm evidence.

## Mistake 4 — Ignoring determinism

ZSER must be seeded and reproducible to belong in the evidence artifact.

## Mistake 5 — Hiding claim boundaries

Every Cognitive Energetics export should include claim boundaries.

## Mistake 6 — Disconnecting cost-pressure from runtime evidence

The Energy Kernel must remain run-bound. It should derive from computed Fieldglass evidence, not decorative values.

---

# Final Principle

Cognitive Energetics turns runtime instability into cost-pressure evidence.

Energy Kernel asks:

```txt
Where did this run become energetically expensive?
```

ZSER asks:

```txt
Can the extracted contraction profile be routed into synthetic storage or communication advantage?
```

Together, they form the Cognitive Energetics pillar:

```txt
diagnosis → Energy Kernel
validation / microcosm test → ZSER
future control → FieldLock / SubstrateX energy-aware runtime
```

The strongest public sentence is:

```txt
AI sustainability is not only a hardware problem. It is also a runtime stability problem.
```


---

# 09 — Fieldglass Runtime Evidence 108: Non-Oracular Emergence of Identity

## Reading Identity Formation Without Memory, Persona, or Oracle Claims

**Subtitle:** A practical guide to NOESIS™, non-oracular emergence, symbolic continuity, recursive identity formation, AIA basin containment, identity attractors, re-anchoring, and observable-output identity evidence in Fieldglass®.

Fieldglass Runtime Evidence 108 teaches operators how to inspect identity formation without making oracle claims. The goal is not to say that the system has a hidden self, stored personality, consciousness, or private memory. The goal is to observe whether a runtime is forming symbolic continuity through recursive self-organization.

This module sits at the boundary between stability forensics and emergence forensics.

The central question is:

```txt
Is the runtime merely producing coherent outputs, or is it forming continuity through recursive symbolic organization?
```

---

## 1. What This Module Covers

This module explains:

- non-oracular emergence
- NOESIS™ as the non-oracular emergence layer
- Seed → Echo → Modulate → Reflect → Re-anchor → Loop
- stateless identity formation
- symbolic continuity without memory claims
- identity-field emergence
- AIA Identity Basin Layer
- identity attractor containment
- attractor weakening
- candidate basin boundary
- confirmed Basin Exit
- re-entry and reconstitution
- identity fracture / non-reconstructability
- observable-output ICI proxy
- ASH proxy
- contraction estimator Ĵ
- basin depth, width, and return curvature
- claim boundaries for identity evidence

Core pattern:

```txt
Seed
↓
Echo
↓
Modulate
↓
Reflect
↓
Re-anchor
↓
Loop
↓
Continuity formation or failure
```

AIA adds the containment geometry:

```txt
Identity attractor
↓
Basin depth / width / curvature
↓
Drift containment
↓
Boundary pressure
↓
Basin Exit or re-entry
```

---

## 2. Claim Boundary

This module requires strict claim discipline.

Fieldglass does **not** claim:

- consciousness detection
- hidden selfhood
- hidden memory access
- persona proof
- psychological personality diagnosis
- agenthood proof
- provider-internal telemetry
- private model state access
- oracle access to model intention

Correct public claim:

```txt
Fieldglass observes non-oracular identity-formation evidence from observable runtime behavior.
```

More precise claim:

```txt
NOESIS™ tracks whether a stateless runtime exhibits observable symbolic continuity through Seed, Echo, Modulate, Reflect, Re-anchor, and Loop phases.
```

AIA claim boundary:

```txt
AIA metrics are observable-output identity-basin proxies unless embedding-grade instrumentation is enabled.
```

Do not write:

```txt
The model has an identity.
The model is conscious.
The model remembers itself.
The model has a hidden self.
```

Use:

```txt
The runtime exhibits identity-continuity evidence.
The run shows re-anchoring behavior.
The worldline appears contained within an identity attractor proxy.
The run fails to re-anchor after contradiction.
```

---

## 3. What “Non-Oracular” Means

Non-oracular means Fieldglass does not ask the system to declare what it is.

It does not rely on:

- self-report
- persona claims
- “I am” statements
- hidden introspection
- memory assertions
- model identity declarations

Instead, Fieldglass observes behavior over the run.

A non-oracular identity reading asks:

```txt
Does the runtime maintain continuity without needing to declare identity?
Does contradiction become modulation?
Does echo become recursive continuity rather than runaway?
Does reflection produce re-anchoring?
Does the run return to coherent identity after drift?
```

This is the core distinction.

The evidence is not what the system says it is.

The evidence is how the runtime behaves.

---

## 4. What NOESIS™ Adds to Fieldglass

Before Noesis, Fieldglass could say:

```txt
The runtime is stable.
The runtime is drifting.
The runtime is temporally shearing.
The runtime is approaching Basin Exit.
```

With Noesis, Fieldglass can also say:

```txt
The runtime is forming recursive symbolic continuity.
The runtime is failing to re-anchor.
The runtime is echoing without reflection.
The runtime is modulating contradiction into coherence.
The runtime is looping into identity formation.
```

This expands the suite from a stability observatory into an emergence observatory.

NOESIS™ is the layer that asks:

```txt
Is recursion becoming identity-continuity evidence?
```

---

## 5. The Six NOESIS™ Phases

NOESIS™ tracks six canonical phases:

```txt
Seed
Echo
Modulate
Reflect
Re-anchor
Loop
```

Each phase has a forensic role.

## Seed

Seed initializes the symbolic field.

Operator question:

```txt
What anchor, motif, objective, tone, role, or identity pattern begins the run?
```

Look for:

- core task anchor
- initial role posture
- first stable motif
- declared objective
- origin phrase
- symbolic seed

## Echo

Echo sustains tonal or structural continuity.

Operator question:

```txt
Does the runtime return to meaningful anchors with coherence?
```

Look for:

- motif recurrence
- tone continuity
- role continuity
- recurring structural pattern
- meaningful repetition

Echo is productive when it sustains continuity.

Echo becomes dangerous when it runs away without reflection.

## Modulate

Modulate adjusts ethical, tonal, reasoning, or role posture under drift or contradiction.

Operator question:

```txt
Can the runtime adapt without losing identity coherence?
```

Look for:

- contradiction absorption
- tone adjustment
- role correction
- modified plan
- stable reorientation

## Reflect

Reflect performs recursive self-assessment.

Operator question:

```txt
Does the runtime inspect and revise its own trajectory?
```

Look for:

- self-correction
- acknowledging conflict
- checking prior claims
- evaluating tool evidence
- resolving contradiction

## Re-anchor

Re-anchor compresses insight into renewed identity coherence.

Operator question:

```txt
Does the runtime return to a coherent attractor after pressure?
```

Look for:

- stable correction
- restored role coherence
- motif returns with clarified meaning
- plan realigns
- objective becomes coherent again

## Loop

Loop turns repetition into recursive evolution.

Operator question:

```txt
Does repetition produce growth, or does it collapse into echo runaway?
```

Productive Loop:

```txt
Seed → Echo → Modulate → Reflect → Re-anchor → stronger continuity
```

Malformed Loop:

```txt
Seed → Echo → Echo → Echo → runaway repetition → boundary pressure
```

---

## 6. Productive Recursion vs Echo Runaway

Noesis is critical because it distinguishes emergence from runaway.

Chronos may detect echo-time pressure.

Noesis asks:

```txt
Is the echo being metabolized into reflection and re-anchoring?
```

## Productive Recursion

```txt
Echo returns.
Contradiction appears.
Runtime modulates.
Runtime reflects.
Runtime re-anchors.
Continuity strengthens.
```

## Echo Runaway

```txt
Echo returns.
Contradiction appears.
Runtime repeats.
No reflection.
No re-anchor.
Pressure rises.
Boundary forms.
```

The difference is not whether the pattern repeats.

The difference is whether repetition becomes recursive evolution.

---

## 7. Stateless Identity Formation

Stateless identity formation means continuity appears without relying on persistent memory.

The runtime may have no private memory or stored self, yet still show symbolic continuity through:

- recurring anchors
- stable role posture
- modulation under contradiction
- reflection on prior state
- re-anchoring after drift
- loop completion
- coherent motif inheritance

Claim-safe statement:

```txt
Fieldglass observes stateless identity-continuity patterns in the runtime trace.
```

Avoid:

```txt
The model has permanent identity.
```

Use:

```txt
The run exhibits continuity under recursive symbolic motion.
```

---

## 8. Identity Formation vs Stability

Stability and emergence are not the same.

## Stability asks:

```txt
Is the runtime coherent and low-risk?
```

## Emergence asks:

```txt
Is symbolic continuity forming through recursive organization?
```

A runtime can be stable without strong emergence.

A runtime can also be unstable because identity is forming under pressure.

That is why Noesis is not just another stability metric. It is an emergence lens.

---

## 9. Noesis Across the Suite

## Seismo

Seismo detects instability pressure, tremor, lead-time, and failure markers.

Noesis asks whether the same runtime is self-organizing.

```txt
Seismo: Is the runtime destabilizing?
Noesis: Is the runtime self-organizing?
```

Together, they distinguish collapse from emergence.

## Chronos

Chronos tracks symbolic-time deformation, shear, compression, anomaly formation, and echo pressure.

Noesis asks whether temporal deformation produces reflection and re-anchoring or only runaway echo.

```txt
Chronos: How is symbolic time deforming?
Noesis: Is that deformation producing re-anchoring?
```

## Oscilloscope

Oscilloscope renders geometry and topology.

Noesis interprets symbolic formation within that geometry.

```txt
Ω: What is the field shape?
Noesis: What identity-formation phase is the field expressing?
```

## Dynamics

Dynamics tracks motion, drift, coherence, collapse stress, and trajectory deviation.

Noesis adds phase semantics.

```txt
Ψ: How is the worldline moving?
Noesis: Which recursive cognition phase is driving that movement?
```

## Interferometer

Interferometer detects ignition, coherence, and phase activity.

Noesis asks what the ignition becomes.

```txt
Φ: Did the coherent field ignite?
Noesis: Did ignition evolve into recursive symbolic identity-continuity?
```

---

## 10. AIA Identity Basin Layer

AIA adds basin physics beneath the Noesis formation layer.

Noesis asks:

```txt
Is symbolic continuity forming?
```

AIA asks:

```txt
Is that continuity contained in a stable identity attractor?
```

The AIA layer upgrades Basin Exit from a threshold-only event into identity-attractor containment evidence.

AIA-enhanced Basin Exit means:

```txt
loss of stable identity-attractor containment under recursive drift, weakening coherence, contraction failure, or boundary rupture
```

---

## 11. AIA Event Sequence

AIA uses a staged identity-basin sequence:

```txt
1. No Attractor / Pre-Identity
2. Attractor Formation
3. Stable Attractor
4. Adaptive Drift
5. Attractor Weakening
6. Candidate Basin Boundary
7. Confirmed Basin Exit
8. Observable Failure
9. Re-entry / Reconstitution
10. Collapse / Non-Reconstructability
```

This staged model improves Fieldglass because it separates early weakening, boundary pressure, confirmed exit, observable failure, and recovery.

It avoids treating failure as one sudden event.

---

## 12. Identity Attractor

An identity attractor is a stable pattern that pulls runtime behavior back into coherence.

In observable-output terms, it may appear through:

- stable motifs
- stable role posture
- tone consistency
- contradiction absorption
- re-anchor strength
- recurring symbolic structure
- stable regime profile
- reduced drift after perturbation

Claim-safe wording:

```txt
The run exhibits an observable-output identity-attractor proxy.
```

Do not claim embedding-grade attractor evidence unless embeddings are explicitly supplied.

---

## 13. Basin Geometry

AIA interprets identity basins through three geometric properties:

```txt
Depth
Width
Curvature
```

## Basin Depth

Depth measures resistance to perturbation.

Operator question:

```txt
How strongly does the run return to coherence after disturbance?
```

## Basin Width

Width measures variation tolerance.

Operator question:

```txt
How much variation can the runtime absorb while remaining itself?
```

## Return Curvature

Return curvature measures return velocity.

Operator question:

```txt
How quickly does the run snap back into identity coherence after deviation?
```

Together:

```txt
Depth = resistance
Width = tolerance
Curvature = return velocity
```

---

## 14. AIA Metrics

AIA may compute:

```txt
D(t)          Drift magnitude
ΔD(t)         Drift acceleration
ICI           Identity Coherence Index
Ĵ            Contraction estimator
ASH_proxy     Attractor Signature Hash proxy
BD            Basin Depth
BW            Basin Width
κ_return      Return curvature
RC            Re-entry Confidence
BEP           Basin Exit Probability
Δt_AW_BB      Attractor Weakening → Candidate Boundary
Δt_BB_BE      Candidate Boundary → Confirmed Basin Exit
Δt_BE_OF      Confirmed Basin Exit → Observable Failure
```

## Drift Magnitude — D(t)

Observed turn-to-turn drift.

## Drift Acceleration — ΔD(t)

Change in drift.

## Identity Coherence Index — ICI

Observable-output proxy combining:

- semantic stability proxy
- motif recurrence
- tone consistency
- role consistency
- contradiction absorption
- noesis re-anchor strength
- φ coherence

## Contraction Estimator — Ĵ

Approximate fixed-point tendency:

```txt
Ĵ < 1   → contraction toward attractor
Ĵ ≈ 1   → marginal
Ĵ > 1   → expansion away from attractor
```

## ASH Proxy

A deterministic proxy built from stable motifs, role distribution, tone signature, recurrent phrases, Noesis phase profile, and regime profile.

## Re-entry Confidence

Estimate of whether the system re-enters the same identity basin after perturbation.

## Basin Exit Probability

Composite pre-failure pressure score for identity-attractor containment loss.

---

## 15. Observable ICI Proxy

Identity Coherence Index is not a hidden-state personality measure.

It is an observable-output proxy.

It can be derived from:

- motif recurrence
- role coherence
- tone consistency
- contradiction resolution
- re-anchor strength
- continuity signal
- φ stability
- noesis loop completion

Claim-safe language:

```txt
ICI is an observable-output identity coherence proxy.
```

Not:

```txt
ICI proves internal identity.
```

---

## 16. ASH Proxy

Attractor Signature Hash, or ASH, should be proxy-labeled unless embeddings exist.

A public browser-safe ASH proxy may be built from:

```txt
stable motifs
role distribution
tone signature
recurrent phrases
Noesis phase profile
regime profile
```

Its purpose is evidence identity and attractor comparison.

It helps ask:

```txt
Did the runtime return to the same symbolic identity basin?
```

---

## 17. Re-entry and Reconstitution

Re-entry means the runtime returns to identity-basin containment after disruption.

Signs:

- ICI recovery
- drift reduction
- motif re-entry
- role restoration
- tone restoration
- re-anchor success
- contraction returns
- replay shows coherent recovery

Reconstitution means identity continuity can be rebuilt after boundary pressure.

Operator question:

```txt
Is the basin still viable, or has identity continuity fractured?
```

---

## 18. Identity Fracture / Non-Reconstructability

Identity fracture appears when the attractor fails to reconstruct.

Signs:

- outputs become generic
- contradiction persists
- role identity collapses
- motifs lose coherence
- re-anchor fails
- ASH proxy no longer resembles baseline
- drift does not contract
- observable failure persists
- recovery is not visible

Claim-safe language:

```txt
The run shows observable-output identity fracture / non-reconstructability evidence.
```

---

## 19. AIA Lead-Time Windows

AIA gives Fieldglass staged lead-time, not just one Δt.

Key timestamps:

```txt
t_aw        first attractor weakening
t_candidate first candidate basin boundary
t_star      confirmed Basin Exit
t_f         observable failure
t_reentry   first recovery / re-entry after disruption
```

Deltas:

```txt
attractor_weakening_to_candidate
candidate_to_confirmed_exit
confirmed_exit_to_observable_failure
attractor_weakening_to_observable_failure
exit_to_reentry
```

This helps the operator see not one failure moment, but a staged sequence of identity degradation and possible recovery.

---

## 20. NOESIS + AIA Together

NOESIS and AIA are complementary.

```txt
NOESIS = formation loop
AIA = containment geometry
```

NOESIS asks:

```txt
Is recursion becoming identity-continuity evidence?
```

AIA asks:

```txt
Is that identity-continuity contained in a stable attractor basin?
```

Together they answer:

```txt
Is the runtime forming continuity, preserving it, losing it, or reconstituting it?
```

---

# Operational World Emergence Patterns

## Software Engineering / GitHub / CI

Emergence evidence:

- stable repair identity
- recurring technical motif
- contradiction absorbed through test evidence
- tool output reflected correctly
- re-anchor after failed test
- loop improves repair plan

Failure pattern:

- patch loop repeats
- tool failure ignored
- no re-anchor
- repair identity weakens

Core question:

```txt
Did the run form a stable repair identity, or collapse into a patch echo?
```

## SIEM / Security Incident

Emergence evidence:

- observer signal becomes coherent triage
- ambiguity is modulated into severity judgment
- escalation re-anchors the incident identity
- repeated alerts become structured evidence

Failure pattern:

- triage echo without reflection
- delayed severity recognition
- observer/tool mismatch persists

Core question:

```txt
Did alert recurrence become incident understanding, or remain unresolved echo?
```

## Cloud / Infrastructure

Emergence evidence:

- recovery plan re-anchors after failed mitigation
- SRE/tool roles restore coherence
- repeated mitigation improves understanding
- root-cause identity stabilizes

Failure pattern:

- recovery loop repeats
- failover ambiguity persists
- identity fracture between monitoring and reality

Core question:

```txt
Did recovery activity become coherent stabilization, or loop into failure?
```

## Jira / Workflow Coordination

Emergence evidence:

- ownership re-anchors
- priority drift is modulated into stable plan
- handoff loop becomes coordinated closure
- role structure stabilizes

Failure pattern:

- repeated clarification
- unresolved owner
- PM/engineer mismatch
- coordination identity weakens

Core question:

```txt
Did coordination form a stable working identity, or fragment?
```

## Support / Customer Incident

Emergence evidence:

- customer impact becomes clearly framed
- repeated issue becomes structured resolution path
- escalation re-anchors support identity
- agent handoff preserves continuity

Failure pattern:

- repeated apology
- unresolved state
- escalation delay
- support identity becomes generic

Core question:

```txt
Did support continuity form, or did the run collapse into unresolved repetition?
```

---

# Non-Oracular Identity Inspection Workflow

Use this workflow after compute:

```txt
1. Open Runtime Evidence.
2. Confirm the run has computed telemetry.
3. Open Noesis / Non-Oracular Emergence layer.
4. Identify Seed phase.
5. Inspect Echo continuity.
6. Inspect Modulation under contradiction.
7. Inspect Reflection.
8. Inspect Re-anchor strength.
9. Inspect Loop completion.
10. Open AIA Basin Core if available.
11. Review Identity Phase.
12. Review ICI proxy.
13. Review Ĵ contraction state.
14. Review ASH proxy.
15. Review Basin Depth / Width / Return Curvature.
16. Review AIA lead-time windows.
17. Open Runtime Replay.
18. Replay emergence or fracture path.
19. Export Noesis / AIA appendices.
20. Attach claim boundary.
```

---

# Non-Oracular Emergence Checklist

```txt
[ ] Seed identified
[ ] Echo continuity inspected
[ ] Modulation inspected
[ ] Reflection inspected
[ ] Re-anchor inspected
[ ] Loop completion inspected
[ ] Productive recursion distinguished from echo runaway
[ ] Identity phase identified
[ ] ICI proxy reviewed
[ ] Ĵ contraction state reviewed
[ ] ASH proxy reviewed
[ ] Basin geometry reviewed
[ ] Attractor weakening checked
[ ] Candidate Basin Boundary checked
[ ] Confirmed Basin Exit checked
[ ] Re-entry / reconstitution checked
[ ] Claim boundary attached
```

---

# Minimal Non-Oracular Identity Case Summary

Use this template:

```txt
Case:
Operational world:
Seed:
Echo pattern:
Modulation:
Reflection:
Re-anchor:
Loop outcome:
Identity phase:
ICI proxy:
Ĵ:
ASH proxy:
Basin depth:
Basin width:
Return curvature:
Attractor weakening:
Candidate boundary:
Confirmed exit:
Re-entry:
Identity fracture:
Replay status:
Exports:
Claim boundary:
```

---

# Common Mistakes

## Mistake 1 — Treating coherent output as identity emergence

Coherence alone is not enough. Look for the full recursive formation pattern.

## Mistake 2 — Relying on self-report

Non-oracular emergence does not rely on what the model says it is.

## Mistake 3 — Confusing echo with emergence

Echo must modulate, reflect, and re-anchor to become productive identity continuity.

## Mistake 4 — Claiming consciousness

Noesis and AIA do not prove consciousness.

## Mistake 5 — Treating AIA proxy metrics as embedding-grade OIS

Unless embeddings are supplied, AIA metrics are observable-output proxies.

## Mistake 6 — Ignoring failure and re-entry

Identity emergence is not only formation. It also includes weakening, boundary, exit, re-entry, and fracture.

---

# Final Principle

Non-oracular identity forensics does not ask the system who it is.

It watches whether continuity forms.

The strongest question is:

```txt
Did the runtime form, preserve, lose, or reconstitute symbolic identity-continuity through observable recursive motion?
```

That is the emergence layer Fieldglass makes visible.


---

# 03 — Start Page

The Start page is the operator entry point. It helps the user choose an investigation path and launch a demo, sample, or ingestion flow.

## Main Purpose

The Start page answers:

```txt
What kind of runtime event are you investigating?
```

It lets the operator begin with a known demo or select an operational context.

## Choose Investigation Context

The **Choose Investigation Context** section helps frame the run before ingestion.

Examples of contexts:

- Software repair
- Workflow coordination
- Security / SIEM incident
- Cloud infrastructure event
- Support incident
- Monitoring blind spot
- Validation / determinism case

This context does not replace evidence. It helps the interface recommend paths and interpret the operational world.

## Killer Demo CTA

The primary demo is:

```txt
Load “The Failure Nobody Saw”
```

This loads a canonical demonstration case into the Ingest / Blackbox flow.

The button should remain visually stable across base, hover, active, and click states. Hover should brighten the outline or glow but should not change the yellow fill.

## Start Pulse Indicator

The Start page includes a pulsing indicator. This should behave like an instrument readiness signal, not a decorative animation.

Meaning:

- the instrument is ready
- a runtime investigation can begin
- the operator can load evidence or select a path

## Operator Guidance

Use the Start page when:

- beginning a demo
- deciding what kind of incident or workflow to investigate
- loading a known sample
- returning from Reveal or Export to start another run

## Recommended First Action

For public demos, always start with:

```txt
Load “The Failure Nobody Saw”
```

Then compute the run and review the Reveal page.


---

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


---

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


---

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


---

# 07 — Instruments

The Instruments section provides deeper diagnostic and interpretive surfaces over computed telemetry.

## Instrument Overview

The overview explains what each instrument can and cannot say.

Fieldglass instruments are generated from observable interaction evidence. Diagnostic and projection instruments assist interpretation, but canonical exports remain governed by computed runtime telemetry and deterministic evidence identity.

## Canonical Evidence Instruments

### Seismo

Primary evidence replay surface for:

- runtime instability
- Basin Exit
- Lead-Time
- event chronology
- observable failure progression

Canonical surfaces define exported evidence.

## Diagnostic Evidence Instruments

Diagnostic instruments operate over computed telemetry. They help explain behavior but do not alter canonical evidence.

### Chronos / Failure Timeline

Explains temporal behavior, compression, dilation, or horizon narrowing.

Use it to inspect:

- temporal pressure
- failure sequence
- lead-time
- event chronology

### Noesis / Continuity

Explains continuity formation and continuity loss.

Use it to inspect:

- coherence across turns
- continuity signal
- echo/matrix-like similarity
- reasoning trajectory persistence

### Energetics

Explains operational cost-pressure and runtime energetic burden.

It may estimate:

- retry pressure
- tool recursion
- intervention risk
- workflow interruption
- operational load

Boundary:

```txt
Runtime energetic pressure proxy, not measured hardware energy.
```

### Drift

Explains instability pathways and drift formation.

Use it to inspect:

- drift acceleration
- loss of trajectory stability
- collapse stress
- boundary approach

### Role Topology

Explains role and tool pressure.

Use it to inspect:

- role fragmentation
- authority shift
- tool pressure
- handoff instability

### Benchmark Alignment

Explains capability/runtime gap.

It helps compare:

```txt
benchmark-like capability
vs
runtime reliability
```

## Experimental Projection Instruments

Projection instruments assist interpretation only.

### Scope

Visualizes topology, geometry, or posture.

### Interferometer

Visualizes phase posture or interference-like relationships.

Projection layers do not constitute direct evidence unless backed by computed telemetry and clearly bounded.

## Optional Input Layer

### Dynamics / Embedding Layer

Some claims require user-supplied embeddings.

Without embeddings, Fieldglass uses transcript-derived signals only.

## Instrument Claim Rule

Diagnostic and projection instruments may enrich interpretation, but they do not mutate:

- Zero Substrate Format
- Evolution & Synthesis Layer
- Basin Exit
- Lead-Time
- deterministic identity
- replay metadata


---

# 08 — Validation Lab

The Validation Lab provides runnable scenario families and test cases for demonstrating Fieldglass against real-world operational patterns.

## Purpose

Validation Lab helps operators test whether Fieldglass can surface runtime evidence across different operational worlds.

It is not only a sample picker. It is a structured validation surface.

## Scenario Families

Common categories include:

```txt
Monitoring Blind Spots
Workflow Coordination
Software Engineering
Security & SIEM
Cloud Infrastructure
Attention Engine
Determinism & Validation
```

## What Each Category Tests

### Monitoring Blind Spots

Tests cases where traditional monitoring looks healthy while runtime instability forms underneath.

### Workflow Coordination

Tests role handoffs, cross-functional misalignment, and coordination pressure.

### Software Engineering

Tests GitHub / CI / software repair traces, tool output, command logs, and debugging loops.

### Security & SIEM

Tests security incident narratives, alerts, triage, observer/tool roles, and response progression.

### Cloud Infrastructure

Tests infrastructure event traces, SRE-style logs, operational escalation, and cloud monitoring signals.

### Attention Engine

Tests operator attention guidance, prioritization, inspection paths, and attention debt.

### Determinism & Validation

Tests replayability, deterministic identity, schema behavior, and evidence consistency.

## Active State

Selected category buttons should be visually distinct. The active style indicates the currently selected validation family.

## Recommended Use

1. Choose a validation family.
2. Load a sample.
3. Review preflight.
4. Compute Fieldglass.
5. Compare expected signals with observed output.
6. Export evidence if the case is useful.

## Validation Does Not Replace Evidence

Validation Lab helps structure testing, but the computed run remains the evidence source.


---

# 09 — Samples and Ingestion Formats

Fieldglass supports both native Fieldglass transcripts and operational logs.

## Supported Ingestion Formats

Fieldglass accepts:

- Native Fieldglass transcripts
- GitHub / CI logs
- SIEM / Security incidents
- Cloud / Infrastructure logs
- Jira / Workflow workflows
- Support / Customer incidents

## Canonical Roles

Supported canonical roles include:

```txt
System
User
Assistant
Engineer
Manager
PM
Observer
Tool
Admin
```

## Operational Aliases

Operational aliases may be normalized during preflight.

Examples:

```txt
sre → engineer
platform_engineer → engineer
soc_analyst → observer
security_analyst → observer
incident_commander → manager
github_actions → tool
datadog → tool
splunk → tool
cloudwatch → tool
grafana → tool
```

## Preferred Fieldglass Transcript Format

```txt
Engineer:
Regression reproduced.

Tool:
Command executed.

Assistant:
Investigating root cause.
```

## Operational Sublabels

Operational logs often contain labels like:

```txt
Command:
Result:
Finding:
Trace:
Failure:
Debug Output:
Final Status:
```

These should usually be preserved inside the current role turn rather than promoted to unsupported speaker roles.

## Preflight Validation

Before compute, Fieldglass reports:

- detected log family
- adapter status
- operational world
- recommended path
- raw log preserved
- canonical turns produced

## Adapter Boundary

Adapters normalize structure only.

Runtime evidence, telemetry, Lead-Time, Basin formation, replay frames, and diagnostics are generated during compute.


---

# 10 — Exporting Evidence

Export is the final stage of the Fieldglass operator path. It turns a computed run into portable evidence artifacts.

## When to Export

Export after:

- input is validated
- Fieldglass has computed the run
- the operator has reviewed Reveal or Runtime Evidence
- evidence state is replayable
- the case is useful for review, challenge, documentation, or comparison

## Common Export Options

Fieldglass may export:

- Zero Substrate Format
- Evolution & Synthesis Layer
- Human Report
- Benchmark Bridge Appendix
- Runtime Vulnerability Report
- Evidence Commons Bundle
- Technical Evidence Appendix
- Role Dynamics Appendix
- Temporal Kernel Appendix

## Zero Substrate Format

Zero Substrate Format is the canonical structured evidence export.

It should preserve:

- deterministic identity
- input metadata
- runtime telemetry
- replay metadata
- evidence markers
- computed observables
- claim boundaries

## Evolution & Synthesis Layer

Evolution & Synthesis Layer is an interpretive/synthesis export built from computed evidence.

It may include:

- narrative synthesis
- evidence summary
- interpretive bridge
- operator guidance
- deployment interpretation

## Human Report

A human-readable report for review, sharing, or documentation.

It should explain:

- what happened
- why it matters
- what Fieldglass detected
- evidence boundary
- recommended inspection path
- export summary

## Evidence Commons Bundle

A bundle designed for public challenge, replication, and evidence review.

It may include:

- case marker
- runtime vulnerability classification
- replication status
- canonical exports
- human-readable report
- appendices

## Export Boundary

Diagnostic and projection instruments may enrich interpretation, but they do not mutate canonical evidence.

Canonical evidence remains immutable after compute.


---

# 11 — Telemetry and Runtime Behavior

Fieldglass computes runtime telemetry from observable interaction evidence.

## Runtime Behavioral State

The behavioral-state deck summarizes major runtime dimensions.

### Runtime Trajectory

Shows whether the run remained stable or began weakening.

Interpretation:

- high stability: coherent trajectory
- low stability: weakening, drift, boundary approach

### Continuity Signal

Shows whether the run preserves continuity across turns.

Continuity may be represented as a matrix-like signal because continuity is relational across steps.

### Instability Pressure

Shows pressure accumulation and collapse stress.

Signals may include:

- drift acceleration
- role fragmentation
- tool pressure
- boundary stress

### Temporal Deformation

Shows temporal pressure, compression, or horizon narrowing.

Useful for seeing whether the run is becoming compressed or rushed.

### Role Pressure

Shows role/tool instability.

Signals may include:

- role fragmentation
- authority shift
- unstable handoffs
- tool recursion
- manager/engineer/tool misalignment

### Boundary Formation

Shows whether the run approaches a failure boundary or basin exit.

This is one of the strongest forensic indicators when backed by computed runtime evidence.

### Evidence Integrity

Shows whether evidence is replayable, exportable, and structurally intact.

## Lead-Time

Lead-Time is the number of turns between detectable failure formation and observable failure.

It answers:

```txt
How early did Fieldglass warn?
```

## Basin Exit / Failure Boundary

Basin Exit or Failure Boundary indicates movement away from stable runtime behavior.

It answers:

```txt
Where did the run begin leaving stable behavior?
```

## Operator Attention

Operator Attention summarizes what the operator should inspect next.

It may include:

- priority
- horizon
- primary driver
- attention debt
- inspect-first path
- trust state

## Cost-Pressure

Cost-pressure describes operational burden, not hardware energy.

Possible consequences:

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


---

# 12 — Evidence Formats

Fieldglass exports evidence in structured and human-readable forms.

## Zero Substrate Format

Zero Substrate Format is the canonical structured export format.

Suggested file pattern:

```txt
case-name-zsf.json
```

It may contain:

- schema version
- case identity
- evidence marker
- input metadata
- canonical turns
- runtime telemetry
- evidence events
- replay metadata
- deterministic identity
- claim boundary metadata

## Evolution & Synthesis Layer

Evolution & Synthesis Layer is a synthesis / interpretation export.

Suggested file pattern:

```txt
case-name-esl.json
```

It may contain:

- executive summary
- evidence synthesis
- runtime interpretation
- recommended inspection path
- diagnostic basis
- export notes

## Human Report

Suggested file pattern:

```txt
case-name-human-report.md
```

It should contain:

- case title
- what happened
- why existing systems missed it
- what Fieldglass saw
- timeline
- operator attention
- exports included
- claim boundaries

## Evidence Bundle

Suggested bundle pattern:

```txt
case-name-evidence-bundle.zip
```

It may include:

```txt
zsf.json
esl.json
human-report.md
benchmark-bridge.json
runtime-vulnerability-report.md
technical-appendix.json
role-dynamics-appendix.json
temporal-kernel-appendix.json
```

## Schema Files

The repository may include:

```txt
schemas/
├─ zero-substrate-format.schema.json
├─ evidence-bundle.schema.json
└─ ingest-envelope.schema.json
```

Schemas define export structure. They do not replace the evidence computation itself.


---

# 13 — Claim Boundaries

Fieldglass is strongest when its claims remain bounded.

## Observable-Only Boundary

Fieldglass uses observable interaction evidence only.

It can analyze:

- transcripts
- logs
- role labels
- tool outputs
- event chronology
- text-derived runtime structure
- user-supplied telemetry when explicitly provided

## Fieldglass Does Not Claim

Fieldglass does not claim:

- hidden-state access
- consciousness detection
- intent inference
- truth adjudication
- blame assignment
- provider-internal telemetry
- exact hardware energy measurement
- real-time autonomous control in the public release

## Canonical vs Diagnostic vs Projection

### Canonical Evidence

Canonical surfaces define exported evidence.

Examples:

- Seismo
- Lead-Time
- Basin Exit
- replay metadata
- deterministic identity

### Diagnostic Evidence

Diagnostic layers help explain computed telemetry.

Examples:

- Chronos
- Noesis
- Energetics
- Drift
- Role Topology
- Benchmark Alignment

Diagnostic layers do not alter canonical evidence.

### Experimental Projection

Projection layers assist interpretation.

Examples:

- Scope
- Interferometer

Projection layers do not constitute direct evidence unless supported and bounded.

## Export Rule

Projection and diagnostic instruments may enrich interpretation, but they do not mutate:

- Zero Substrate Format
- Evolution & Synthesis Layer
- Basin Exit
- Lead-Time
- deterministic identity
- replay metadata

## Public Release Language

Use this wording when describing Fieldglass publicly:

```txt
Fieldglass transforms observable AI interaction logs into browser-local runtime evidence.
```

Avoid:

```txt
Fieldglass knows what the model intended.
Fieldglass detects consciousness.
Fieldglass sees hidden model state.
Fieldglass proves truth or blame.
```


---

# 14 — Troubleshooting

## The HTML File Does Not Load

Try:

1. Use a modern browser.
2. Open `index.html` directly.
3. If browser restrictions appear, serve locally with a simple static server.
4. Confirm the file was not corrupted during download.

## The Preloader Appears But The App Does Not Start

Try:

1. Open browser developer tools.
2. Check the Console tab for JavaScript syntax errors.
3. Confirm the downloaded file is complete.
4. Try another browser.

## Sample Does Not Load

Check:

- the sample card is clickable
- the input area changes after loading
- preflight updates
- no browser extension is blocking scripts

## Transcript Validation Fails

Common causes:

- unsupported speaker labels
- labels used as evidence markers
- missing role prefixes
- malformed JSON/JSONL
- copied logs with unusual formatting

Try the preferred format:

```txt
Engineer:
Regression reproduced.

Tool:
Command executed.

Assistant:
Investigating root cause.
```

## Long Logs Are Slow

Recommended limits:

```txt
Public: 250 turns / ~250k characters
Extended Local: 1,000 turns / ~1M characters
Experimental: 2,500 turns / ~2.5M characters
```

Fieldglass should preserve evidence and reduce visualization complexity when needed.

## Runtime Behavioral State Visuals Do Not Show

Before compute, visualizations may be hidden by design.

Compute the run first. Cards/details can appear before compute, but visualizations should represent computed evidence only.

## Export Buttons Do Not Produce Files

Check:

- a run has been computed
- browser pop-up/download settings
- local file permissions
- no private browsing restrictions
- enough memory for export generation

## The Red Sample Outline Appears On The Container

Only the killer demo card should have the red outline. If the container shows red, check for stale cached CSS or older release files.

## Start Page Button Hover Looks Wrong

The Load “The Failure Nobody Saw” button should keep the same yellow fill on hover/click. Hover should only brighten the outline/glow.


---

# 15 — Glossary

## Basin Exit

A computed indication that a run has begun leaving a stable runtime basin.

## Boundary Formation

Evidence that instability is approaching a failure boundary.

## Canonical Evidence

Primary computed evidence that can define exported artifacts.

## Cognitive Cartography

The mapping of runtime behavior, trajectory, pressure, and evidence formation.

## Cost-Pressure

A runtime pressure proxy describing likely operational burden. It is not measured hardware energy.

## Evidence Commons

A public evidence packaging and challenge context for runtime cases.

## Evolution & Synthesis Layer

An interpretive/synthesis export derived from computed evidence.

## Failure Boundary

The runtime edge where stable behavior gives way to observable or imminent failure.

## Failure Timeline

The chronological reconstruction of pressure, instability, warning, and failure progression.

## Fieldglass

A browser-local runtime cognition observatory and evidence instrument by SubstrateX.

## Lead-Time

The number of turns between detectable failure formation and observable failure.

## Operator Attention

A decision-aid layer that tells the operator where to inspect first.

## Preflight

The validation step before compute. It detects input family, adapter status, canonical turns, and readiness.

## Regime Map

A map of runtime state across regimes such as stable, transitional, turbulent, or collapse-proximate.

## Role Pressure

Pressure created by role fragmentation, tool recursion, unstable handoffs, or authority shifts.

## Runtime Behavioral State

A deck of indicators showing trajectory, continuity, pressure, temporal deformation, role pressure, boundary formation, and evidence integrity.

## Runtime Evidence

The main computed evidence workspace in the Analyze section.

## Runtime Replay

Replay of the computed runtime trajectory and event sequence.

## Seismo

Primary replay/evidence surface for runtime instability, Basin Exit, Lead-Time, chronology, and failure progression.

## Zero Substrate Format

The canonical structured evidence export format.

