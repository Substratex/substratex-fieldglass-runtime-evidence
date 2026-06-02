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
