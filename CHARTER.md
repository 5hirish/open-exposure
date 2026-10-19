# OpenExposure Charter v0.1

OpenExposure is an independent nonprofit that tells people, in plain language, where their
data goes when they use AI software. It publishes verified exposure reports without needing
the developer's permission.

Changes to this charter are proposed as pull requests, open for 14 days of public comment,
and approved by the advisory board.

## 1. Mission and scope

**Mission:** close the gap between what AI software claims about user data and what it
actually does.

**In scope (pilot):**

- AI chat assistants: desktop (Electron) and Android apps of ChatGPT, Claude, Gemini,
  Copilot, Perplexity and DeepSeek
- AI companions: Character AI and Replika (web and Android)
- AI meeting recorders: Otter, Fireflies and Granola
- AI writing and keyboard tools: Grammarly and Gboard
- AI browser extensions (Chrome Web Store, Firefox Add-ons): 15 popular extensions
- Open source MCP servers and agent plugins, after the pilot

**Out of scope:**

- Finding exploitable vulnerabilities. Bugs found along the way go to the developer through
  coordinated disclosure ([`SECURITY.md`](SECURITY.md)), never into a public report first.
- iOS apps, until a legal and technical path exists without decrypting App Store binaries.
- Server-side behavior we cannot observe. We report what is declared and label it E0.
- Star ratings or single scores. We publish findings with evidence levels, not grades.

## 2. Independence rules

These adapt the four evaluator requirements Anthropic published in October 2026:
expertise, independence, access and freedom to publish.

1. **No paid reports.** No developer can pay for a report, a higher evidence level, or the
   removal of a finding.
2. **Funding firewall.** No funding from a company whose product is in scope for a report
   in the next 12 months. AI lab grants are allowed only as unrestricted funding, listed
   publicly, and every report on a product built on that lab's models states the
   relationship.
3. **No equity.** Reviewers hold no shares or advisory roles in reviewed companies or their
   direct competitors.
4. **Recusal.** A reviewer who has worked for, consulted for, or competes with a developer
   in the last 24 months does not review that product.
5. **Public funder list.** Every funder above EUR 500 per year, with amount band, published
   on the site and updated quarterly.
6. **Tool neutrality.** Reports name the tools and AI models used to produce them. No vendor
   gets review or approval rights over findings.

## 3. Evidence levels and cooperation tiers

Every finding carries its own evidence level (E0 Claimed, E1 Code-traced, E2 Observed,
E3 Confirmed by developer). See [`METHODOLOGY.md`](METHODOLOGY.md) for the exact bar.

Developers can raise what we can see by cooperating. Cooperation never buys silence.

| Tier | Developer provides | What they get |
| --- | --- | --- |
| 0. None | Nothing | Report published from public evidence only, after right of reply |
| 1. Responsive | Answers our questions within 14 days | Answers quoted, marked E0 or E3 |
| 2. Open | Source access or architecture docs and backend data-flow description | Backend claims can reach E3 |
| 3. Audited | Tier 2 plus a test account and re-test after each major release | "Verified current" status while re-tests pass |

Tiers change what we can see, never what we may say.

## 4. Publication, right of reply, corrections

**Before publication**

1. Draft sent to the developer's listed contact and store support email, with the full
   evidence pack.
2. The developer has **14 calendar days** to respond, plus one 7-day extension on request.
3. Factual corrections backed by evidence are applied before publication.
4. Other disagreements are published alongside the finding as the developer's response,
   unedited, up to 300 words.
5. No response is noted as "Developer did not respond by [date]."

**After publication**

- Every report shows the version tested and the test date. Reports older than 6 months, or
  older than the latest major version, show "May be outdated."
- Developers can request a re-test after a fix. Re-tests are queued by user impact.
- Corrections are made in place and logged in the report's changelog with date and reason.
  The original text stays visible, struck through.
- Errors we find ourselves are corrected the same way within 72 hours.

## 5. Legal and safety guardrails

No report is published until an EU tech lawyer has reviewed this charter and the first three
reports. This section is a working draft, not legal advice.

- Analyze only products obtained lawfully as an ordinary user.
- Prefer observing the running product over decompiling; counsel to confirm how the EU
  Software Directive (2009/24/EC) applies to each method.
- Never bypass DRM, encryption or access controls.
- Never test beyond normal user behavior: no fuzzing, no load, no access to other users' data.
- Publish facts with evidence, not characterizations: "sends typed text to Provider X",
  never "spyware" or "steals".
- Redact secrets, API keys and personal data from evidence. Never publish exploit code.
- Canary data only: tests never process real personal data.
- Operate as a registered nonprofit association before the first publication, with media
  liability or professional indemnity insurance once reports go public.

## 6. Governance and funding

| Role | Responsibility |
| --- | --- |
| Founder / editor (Shirish Kadam) | Final call on publication, methodology owner |
| Reviewers (volunteer security researchers) | Reproduce findings, second reviews |
| Advisory board (security researcher, privacy lawyer, consumer advocate) | Charter changes, complaints about OpenExposure itself |

Complaints about a report go to the advisory board, not the editor who published it.

Funding, in order of preference: volunteer time and free infrastructure, small grants from
privacy and open internet funders, individual donations, then AI lab grants under the
funding firewall. No advertising, no affiliate links, no paid placements, ever.
