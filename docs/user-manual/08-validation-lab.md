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
