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
