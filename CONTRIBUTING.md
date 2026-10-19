# Contributing

Thanks for helping. OpenExposure needs three kinds of contributors:

- **Reviewers** reproduce findings from scratch and do hostile second reviews.
- **Legal and policy volunteers** review reports for EU and Spanish law before publication.
- **Translators**, starting with Spanish.

## Before you start

1. Read `CHARTER.md`, especially the independence and recusal rules. If you worked for,
   consulted for or compete with a developer in the last 24 months, you cannot review that
   product.
2. Read `METHODOLOGY.md` and run `tools/canary-session.md` once on the fictional setup.

## Workflow

1. Open an issue to claim a target from `pilot/targets.yaml`.
2. Work on a branch named `report/<slug>`.
3. Keep the report in `draft`. Run `python tools/validate.py reports/<slug>`.
4. Open a pull request. Two reviewers who did not produce the findings must reproduce every
   E2 finding before the status moves to `in-review`.

## What we will not accept

- Findings without evidence, or evidence levels higher than the evidence supports
- Real personal data, credentials, raw captures or unredacted tokens
- Exploit code or step-by-step abuse instructions
- Characterizations such as "spyware" in place of facts

## AI assistance

You may use AI tools. List every model used in the report's `method.ai_models`. You remain
responsible for every claim.
