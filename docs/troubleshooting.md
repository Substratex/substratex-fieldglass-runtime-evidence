# Troubleshooting

## The HTML file opens but some browser behavior looks restricted

Serve the folder locally:

```bash
python -m http.server 8000
```

Then open:

```text
http://localhost:8000
```

## My log will not parse

Check that the pasted input contains clear speaker labels or recognizable operational log structure.

Preferred transcript format:

```text
Engineer:
Regression reproduced.

Tool:
Command executed.

Assistant:
Investigating root cause.
```

## My log is very long

Fieldglass prioritizes evidence completeness over visualization complexity.

Recommended public limit:

```text
250 turns / ~250k characters
```

Extended local runs may work, but browser performance depends on the machine and log structure.

## Should I paste private logs into GitHub issues?

No. Do not include private logs, secrets, access tokens, proprietary prompts, or confidential transcripts in public issues.
