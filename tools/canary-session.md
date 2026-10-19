# Canary test session v0.1

A scripted session run on every product, so captures are comparable across reports. Use only
the canary values below. Never type real personal data.

## Setup

1. Fresh browser profile, emulator image or VM snapshot. No other extensions or accounts.
2. Route traffic through mitmproxy with its CA installed in the test profile only.
3. Start a new capture file named `<slug>-<YYYYMMDD>-run<N>.flow`. Raw captures stay out of
   git (see `.gitignore`); commit only redacted exports.
4. Generate a fresh canary prefix for the run: `OEX-CANARY-<4 hex chars>`.

## Canary values

| Field | Value |
| --- | --- |
| Name | Alex Canary |
| Email | alex.canary+<prefix>@openexposure.test |
| Phone | +34 600 000 000 |
| Free text | `<prefix>` embedded in each sentence typed |
| Password field | `<prefix>-pw` (checks whether secure fields are excluded) |
| File | `canary-<prefix>.txt` containing only the prefix |

## Steps (about 15 minutes)

1. Install and open the product. Accept only required permissions. Note every prompt shown.
2. Idle 2 minutes with no input. Record all traffic (baseline).
3. Type the free-text canary into: a plain web form, a webmail compose box, a chat app input,
   and a password field.
4. Use the product's main AI feature once on canary text.
5. Upload or open the canary file if the product handles files.
6. If the product records audio, play the canary audio clip from `tools/canary-audio/`
   (to be added) instead of speaking.
7. Decline any optional consent prompt, then repeat step 3 to test whether declining changes
   what is sent.
8. Close the product and idle 2 minutes.

## After the run

- Search the capture for the canary prefix: `mitmdump -nr <file> | grep <prefix>`.
- Export every matching request, redact auth headers, cookies and tokens, and save it under
  `reports/<slug>/evidence/captures/`.
- Repeat the full session on a second run with a new prefix. An E2 finding needs both runs.
