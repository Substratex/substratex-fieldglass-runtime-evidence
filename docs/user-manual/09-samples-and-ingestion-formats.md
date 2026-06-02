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
