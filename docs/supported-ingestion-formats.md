# Supported Ingestion Formats

Fieldglass accepts:

- Native Fieldglass transcripts
- GitHub / CI logs
- SIEM / Security incidents
- Cloud / Infrastructure logs
- Jira / Workflow workflows
- Support / Customer incidents

## Canonical Roles

Fieldglass normalizes to:

```text
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

Operational aliases are normalized during preflight. Examples include:

```text
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

## Preferred Format

```text
Engineer:
Regression reproduced.

Tool:
Command executed.

Assistant:
Investigating root cause.
```

## Preflight Validation

Before compute, Fieldglass shows:

- detected log family
- adapter status
- operational world
- recommended path
- raw log preserved
- canonical turns produced

Adapters normalize structure only. Runtime evidence, telemetry, Lead-Time, Basin formation, replay frames, and diagnostics are generated during compute.
