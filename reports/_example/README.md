# ExampleNotes AI: Exposure Report (fictional example)

**This product does not exist.** This folder shows the shape of a report and gives the
validator something to test against. It can never be published (`"fictional": true`).

Version tested: 1.4.2 · Platform: Chrome extension · Tested: 2026-10-19 · Status: Draft ·
Cooperation tier: 0 None

## In 30 seconds

When you type in any website, this extension sends what you type to an AI provider,
including in email and chat apps. Its store label says it collects no data.

Claims vs reality: **1 mismatch, 1 undisclosed flow**

## What leaves your device

| Data | Sent to | When | Evidence | Matches claims? |
| --- | --- | --- | --- | --- |
| Typed text in all fields | api.example-ai.test (AI provider) | After a 1-second pause, every site | E2 Observed | No: label says no data collected |
| Install ID | telemetry.example-labs.test | On install | E1 Code-traced | Not disclosed |

## Mismatches

**F1. Typed text.** The store label says "your data is not being collected or used"
([archived](evidence/claims/store-label.txt)). We observed typed text, including a canary
string, sent to the AI endpoint on two separate runs
([capture](evidence/captures/typed-text-request.redacted.txt)), and traced it to
`content/listener.js` line 42.

## What you can do

- Turn the extension off on email, banking and chat sites.
- Remove it if you type anything you would not send to a third party.

## Developer response

Not yet sent.

## Method

mitmproxy 11.0, rea-agents 4.1.0, Claude Opus 5.5 for code tracing. Reviewer: SK.

## Changelog

- 2026-10-19: Draft created as a fictional example
