#!/usr/bin/env python3
"""Validate OpenExposure reports.

Checks every reports/<slug>/report.json against the JSON Schema, then applies the
evidence and publication rules from METHODOLOGY.md and CHARTER.md that a schema alone
cannot express.

Usage:
    python tools/validate.py              # all reports
    python tools/validate.py reports/foo  # one report folder

Exit code 0 when every report passes, 1 otherwise.
"""
from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "exposure-report.schema.json"
REPORTS_DIR = ROOT / "reports"

# Characterizations the charter bans in published text. Facts only.
BANNED_WORDS = ["spyware", "malware", "malicious", "steal", "steals", "stealing", "scam", "keylogger"]

# Evidence type each level requires (E0 needs an archived claim instead).
LEVEL_NEEDS = {
    "E1": {"code-reference"},
    "E2": {"traffic-capture"},
    "E3": {"developer-statement"},
}
REPLY_WINDOW_DAYS = 14
ADVANCED_STATUSES = {"right-of-reply", "published", "corrected", "outdated"}
PUBLIC_STATUSES = {"published", "corrected", "outdated"}


def rule_errors(report: dict, folder: Path) -> list[str]:
    errors: list[str] = []

    if report["slug"] != folder.name and not folder.name.startswith("_"):
        errors.append(f"slug '{report['slug']}' does not match folder '{folder.name}'")

    claims = {c["id"]: c for c in report["claims"]}
    evidence = {e["id"]: e for e in report["evidence"]}

    for kind, items in (("claim", report["claims"]), ("evidence", report["evidence"]), ("data flow", report["data_flows"])):
        ids = [i["id"] for i in items]
        dupes = {i for i in ids if ids.count(i) > 1}
        if dupes:
            errors.append(f"duplicate {kind} ids: {sorted(dupes)}")

    for claim in report["claims"]:
        path = claim.get("archive_path")
        if path and not (folder / path).is_file():
            errors.append(f"{claim['id']}: archive_path '{path}' not found")

    for ev in report["evidence"]:
        path = ev.get("path")
        if path and not (folder / path).is_file():
            errors.append(f"{ev['id']}: evidence file '{path}' not found")
        if ev["type"] == "code-reference" and "code" not in ev:
            errors.append(f"{ev['id']}: code-reference needs a code block (file, line, excerpt)")
        if ev["type"] == "traffic-capture":
            if not path:
                errors.append(f"{ev['id']}: traffic-capture needs a redacted capture file in path")
            if ev.get("runs", 0) < 2:
                errors.append(f"{ev['id']}: traffic-capture must be reproduced on 2+ runs (runs={ev.get('runs', 0)})")

    for flow in report["data_flows"]:
        fid, level = flow["id"], flow["evidence_level"]
        for ref in flow["evidence_refs"]:
            if ref not in evidence:
                errors.append(f"{fid}: evidence ref {ref} does not exist")
        for ref in flow.get("claim_refs", []):
            if ref not in claims:
                errors.append(f"{fid}: claim ref {ref} does not exist")

        types = {evidence[r]["type"] for r in flow["evidence_refs"] if r in evidence}
        needed = LEVEL_NEEDS.get(level)
        if needed and not (types & needed):
            errors.append(f"{fid}: {level} requires evidence of type {sorted(needed)}, found {sorted(types) or 'none'}")
        if level == "E0" and not flow.get("claim_refs"):
            errors.append(f"{fid}: E0 flow must cite the claim it rests on (claim_refs)")

        if flow["matches_claims"] in {"no", "yes"} and not flow.get("claim_refs"):
            errors.append(f"{fid}: matches_claims='{flow['matches_claims']}' must cite claim_refs")
        if flow["matches_claims"] == "no" and level == "E0":
            errors.append(f"{fid}: a mismatch needs E1 or higher evidence, not E0")

    texts = [report["summary"]] + [f["description"] for f in report["data_flows"]]
    for text in texts:
        for word in BANNED_WORDS:
            if re.search(rf"\b{word}\b", text, re.IGNORECASE):
                errors.append(f"banned characterization '{word}' in: {text[:60]}...")

    response = report["developer_response"]
    status = report["status"]
    if status in ADVANCED_STATUSES and not response["sent_on"]:
        errors.append(f"status '{status}' requires developer_response.sent_on")
    if status in PUBLIC_STATUSES:
        if report.get("fictional"):
            errors.append("fictional reports can never be published")
        if len(report["method"]["reviewers"]) < 2:
            errors.append("published reports need at least 2 human reviewers")
        if response["sent_on"]:
            sent = dt.date.fromisoformat(response["sent_on"])
            published = [dt.date.fromisoformat(c["date"]) for c in report["changelog"] if "publish" in c["change"].lower()]
            if published and min(published) < sent + dt.timedelta(days=REPLY_WINDOW_DAYS):
                errors.append(f"published before the {REPLY_WINDOW_DAYS}-day reply window ended")

    return errors


def validate_folder(folder: Path, validator: Draft202012Validator) -> list[str]:
    report_path = folder / "report.json"
    if not report_path.is_file():
        return [f"missing {report_path.relative_to(ROOT)}"]
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"invalid JSON: {exc}"]

    schema_errors = [
        f"schema: {'/'.join(str(p) for p in err.absolute_path) or '<root>'}: {err.message}"
        for err in sorted(validator.iter_errors(report), key=lambda e: list(e.absolute_path))
    ]
    if schema_errors:
        return schema_errors
    return rule_errors(report, folder)


def mismatch_count(folder: Path) -> int:
    report = json.loads((folder / "report.json").read_text(encoding="utf-8"))
    return sum(1 for f in report["data_flows"] if f["matches_claims"] in {"no", "undisclosed"})


def main(argv: list[str]) -> int:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    folders = [Path(a).resolve() for a in argv] or sorted(p for p in REPORTS_DIR.iterdir() if p.is_dir())
    failed = 0
    for folder in folders:
        errors = validate_folder(folder, validator)
        name = folder.relative_to(ROOT)
        if errors:
            failed += 1
            print(f"FAIL {name}")
            for err in errors:
                print(f"  - {err}")
        else:
            print(f"ok   {name} ({mismatch_count(folder)} mismatch or undisclosed flows)")

    print(f"\n{len(folders) - failed}/{len(folders)} reports valid")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
