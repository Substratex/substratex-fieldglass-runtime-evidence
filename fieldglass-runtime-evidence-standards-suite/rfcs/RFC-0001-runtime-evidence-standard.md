# RFC-0001: Runtime Evidence Standard

## Abstract

This RFC defines Runtime Evidence as observable, replayable, challengeable, and preservable evidence reconstructed from interaction logs and computed instrument telemetry.

## Core Principle

```txt
Runtime behavior becomes evidence.
```

## Normative Requirements

1. Raw evidence MUST be preserved or referenced.
2. Canonical turns MUST be versioned.
3. Computed telemetry MUST be traceable to the input.
4. Replay MUST preserve event order.
5. Exports MUST include claim boundaries.
6. EvidenceCommons artifacts MUST preserve provenance and checksums.
