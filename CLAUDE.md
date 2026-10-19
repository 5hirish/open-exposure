# CLAUDE.md

Guidance for Claude Code (and any AI agent) working in this repository.

## What this repo is

OpenExposure publishes verified reports on where AI software sends user data. Accuracy and
legal defensibility matter more than speed. Read `CHARTER.md` and `METHODOLOGY.md` before
changing anything under `reports/`.

## Hard rules

1. **Never mark a finding above the evidence you hold.** E1 needs a code reference, E2 needs
   a redacted capture reproduced on 2+ runs, E3 needs a developer statement. If unsure,
   downgrade.
2. **Never set a report's status to `published`, `corrected` or `outdated`.** Only a human
   editor does that after legal review. Agents work in `draft` and may propose `in-review`.
3. **Facts, not characterizations.** Never write "spyware", "malicious", "steals",
   "keylogger" or similar in summaries or descriptions. Write what is sent, to whom, when.
4. **Canary data only.** Never type, store or commit real personal data, credentials or
   payment details. Use the values in `tools/canary-session.md`.
5. **No raw captures or secrets in git.** Commit only redacted exports. Strip auth headers,
   cookies, tokens and API keys.
6. **No exploit code.** Security bugs found during testing go to `SECURITY.md` handling, not
   into reports.
7. **Disclose AI use.** Every report lists the AI models used in `method.ai_models`, and any
   relationship with the product's model provider in `method.conflicts`.
8. **No bypassing protections.** Do not decrypt, crack or circumvent DRM or access controls.

## Commands

```bash
pip install -r requirements.txt
python tools/validate.py            # validate every report
python tools/validate.py reports/x  # validate one report
```

`tools/validate.py` must pass before any commit that touches `reports/`.

## Adding a report

1. Create `reports/<slug>/` where `<slug>` matches `pilot/targets.yaml`.
2. Copy `reports/_example/report.json` as a starting point and set `"fictional": false`.
3. Put archived claims under `evidence/claims/` and redacted captures under
   `evidence/captures/`.
4. Write `README.md` from `templates/report.md`.
5. Run the validator and fix every error.

## Writing style for reports

Plain words, sentences under 25 words, the real recipient named, the mismatch first. A
reader with no technical background should understand the 30-second summary.
