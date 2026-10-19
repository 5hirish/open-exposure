# OpenExposure

**Independent, verified, plain-language reports on where AI software sends your data.**

OpenExposure is a nonprofit watchdog. We test popular AI apps, browser extensions and
keyboards, capture what actually leaves the device, and compare it with what the developer
and app store claim. Reports are published without needing the developer's permission,
after a 14-day right of reply.

> Status: **pre-pilot**. Nothing is published until counsel has reviewed the charter and
> the first three reports. See [`pilot/PLAN.md`](pilot/PLAN.md).

## What every report answers

1. What data leaves the device (typed text, page content, files, audio, identifiers)
2. Where it goes (named third parties, including LLM providers)
3. When it is sent (always, on an action, after consent)
4. Whether this matches what the developer and store label claim

Every finding carries an **evidence level**, so readers know how sure we are:

| Level | Name | Meaning |
| --- | --- | --- |
| E0 | Claimed | Stated by the developer, store label or privacy policy. Not checked. |
| E1 | Code-traced | Found in the shipped code, with file and line reference |
| E2 | Observed | Seen in captured network traffic from the real product, reproduced on 2+ runs |
| E3 | Confirmed by developer | Developer confirmed or supplied documents |

A finding at E1 or E2 that contradicts an E0 claim is a **mismatch**, the most important
thing a report can say.

## Repository layout

| Path | What it holds |
| --- | --- |
| [`CHARTER.md`](CHARTER.md) | Mission, independence rules, publication policy, governance |
| [`METHODOLOGY.md`](METHODOLOGY.md) | The step-by-step test and verification pipeline |
| [`schema/exposure-report.schema.json`](schema/exposure-report.schema.json) | Machine-readable report format (JSON Schema) |
| [`templates/report.md`](templates/report.md) | Human-readable report template |
| [`reports/`](reports/) | Published and draft reports, one folder per product |
| [`pilot/`](pilot/) | Pilot plan, target list and kill criteria |
| [`tools/validate.py`](tools/validate.py) | Validates every report against the schema and evidence rules |

## Contributing

We need security researchers to reproduce findings, privacy lawyers for review, and
translators. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) first. Security vulnerabilities found
during testing follow [`SECURITY.md`](SECURITY.md) and are never published before a fix.

## Licenses

- Code and tooling: [MIT](LICENSE)
- Reports, methodology and documentation: [CC BY 4.0](LICENSE-CONTENT.md)
