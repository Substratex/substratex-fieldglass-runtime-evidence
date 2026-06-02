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
