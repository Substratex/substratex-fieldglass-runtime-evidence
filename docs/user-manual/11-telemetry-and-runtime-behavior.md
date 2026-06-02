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
