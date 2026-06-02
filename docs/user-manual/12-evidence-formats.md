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
