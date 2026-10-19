# Methodology v0.1

AI agents may draft findings; a human verifies every one before publication. Verification,
not discovery, is the bottleneck by design.

## Pipeline per product

1. **Snapshot.** Download the exact public version. Record version, store URL, platform and
   SHA-256 of the installer or package.
2. **Collect claims (E0).** Archive the store listing, store data label (Chrome Web Store
   privacy tab, Google Play Data safety) and privacy policy on the same day. Save each as a
   file under `reports/<slug>/evidence/claims/` and record an archive URL.
3. **Trace (E1).** Trace what happens to typed text, page content, files and audio in the
   shipped code (for example with a coding agent plus [REA](https://rea.tools/)). Record
   file path, line and a short excerpt for every claim.
4. **Observe (E2).** Run the product in a clean test profile behind mitmproxy. Run the
   scripted test session in [`tools/canary-session.md`](tools/canary-session.md) using
   unique canary strings. Record every request that carries canary data.
5. **Diff.** Compare observed behavior with claims. Draft findings and mismatches in
   `report.json`.
6. **Human verification.** A reviewer reproduces every E2 finding from scratch and checks
   every E1 reference by hand. Anything not reproduced is dropped or downgraded.
7. **Second review.** A second reviewer reads the report as a hostile developer would,
   looking for overclaims.
8. **Right of reply.** Send to the developer (see [`CHARTER.md`](CHARTER.md) section 4).
9. **Publish** with the evidence pack.

## Evidence bar

| Level | Required to claim it |
| --- | --- |
| E0 Claimed | An archived copy of the claim (store label, policy, listing) with retrieval date |
| E1 Code-traced | At least one code reference: file, line, excerpt, product version |
| E2 Observed | Redacted capture of a request carrying canary data, reproduced on 2+ separate runs |
| E3 Confirmed | A written statement or document from the developer, stored in the evidence pack |

## Rules

- Canary data only. Never type real personal data, passwords or payment details into a
  tested product.
- Every published claim links to evidence: a code reference, a redacted capture or an
  archived document.
- Agent output is never published unreviewed. Reports state which steps used AI and which
  models.
- `tools/validate.py` must pass before a report moves from `draft` to `in-review`.
- Methodology, scripts and canary plans are open source so anyone can rerun them.
