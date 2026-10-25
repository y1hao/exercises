"""Validate the calendar, repository references and ready Brief structure."""

import argparse
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path
import re
from urllib.parse import urlparse

import yaml

from common import DOMAINS, KINDS, ROOT, STATUSES, local_path, read_yaml


def text(value):
    return isinstance(value, str) and bool(value.strip())


def iso_date(value):
    if isinstance(value, datetime):
        raise ValueError("timestamp is not a calendar date")
    if isinstance(value, date):
        return value
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise ValueError("expected YYYY-MM-DD")
    return date.fromisoformat(value)


def string_list(value, nonempty=True):
    return isinstance(value, list) and (bool(value) or not nonempty) and all(text(v) for v in value)


def ready_errors(brief):
    """Structural checks only: a passing result does not verify external facts."""
    errors = []
    for field in ("objective", "opening"):
        if not text(brief.get(field)):
            errors.append(f"ready Brief requires nonempty {field}")
    if brief.get("kind") == "micro_design":
        for field in ("initial_constraints", "evaluation_criteria", "boundaries"):
            if not string_list(brief.get(field)):
                errors.append(f"{field} must be a nonempty list of strings")
        changes = brief.get("perturbations")
        if not isinstance(changes, list) or not 1 <= len(changes) <= 2:
            errors.append("perturbations must contain 1–2 changes")
        else:
            ids = set()
            for item in changes:
                if not isinstance(item, dict) or not all(text(item.get(k)) for k in ("id", "change", "tests")):
                    errors.append("each perturbation requires id/change/tests")
                elif item["id"] in ids:
                    errors.append("duplicate perturbation ID")
                else:
                    ids.add(item["id"])
        return errors

    try:
        iso_date(brief.get("historical_as_of"))
    except (TypeError, ValueError) as exc:
        errors.append(f"invalid historical_as_of: {exc}")
    boundaries = brief.get("boundaries")
    if not isinstance(boundaries, dict) or not string_list(boundaries.get("forbidden_assumptions")):
        errors.append("boundaries.forbidden_assumptions must be a nonempty string list")
    sources = brief.get("sources")
    source_ids = set()
    if not isinstance(sources, list) or not sources:
        errors.append("historical ready Brief requires sources")
        sources = []
    for item in sources:
        if not isinstance(item, dict):
            errors.append("source must be a mapping")
            continue
        sid = item.get("id")
        if not text(sid) or sid in source_ids:
            errors.append("source IDs must be nonempty and unique")
        else:
            source_ids.add(sid)
        url = item.get("url")
        try:
            parsed = urlparse(url) if isinstance(url, str) else None
            hostname = parsed.hostname if parsed else None
        except ValueError:
            parsed, hostname = None, None
        if (
            not parsed or parsed.scheme not in {"https", "http"} or not hostname
            or any(hostname == reserved or hostname.endswith("." + reserved)
                   for reserved in ("example.org", "example.com", "example.net", "localhost"))
            or hostname.endswith((".example", ".invalid", ".test", ".localhost"))
        ):
            errors.append(f"source {sid}: requires a real HTTP(S) URL")
        if not text(item.get("publisher")) or not string_list(item.get("supports")):
            errors.append(f"source {sid}: requires publisher and supports")

    def references(value, label):
        if not string_list(value):
            errors.append(f"{label} requires nonempty source_ids")
        elif not set(value) <= source_ids:
            errors.append(f"{label} references unknown source_ids")

    evidence = brief.get("evidence_pool")
    if not isinstance(evidence, list) or not evidence:
        errors.append("historical ready Brief requires evidence_pool")
        evidence = []
    evidence_ids = set()
    for item in evidence:
        if not isinstance(item, dict):
            errors.append("evidence must be a mapping")
            continue
        eid = item.get("id")
        if not text(eid) or eid in evidence_ids:
            errors.append("evidence IDs must be nonempty and unique")
        else:
            evidence_ids.add(eid)
        if item.get("availability") not in ("initial", "on_request", "after_commitment"):
            errors.append(f"evidence {eid}: invalid availability")
        if not text(item.get("fact")) or not text(item.get("release_trigger")):
            errors.append(f"evidence {eid}: requires fact and release_trigger")
        references(item.get("source_ids"), f"evidence {eid}")
    resolution = brief.get("resolution")
    if not isinstance(resolution, dict):
        errors.append("historical ready Brief requires resolution")
    else:
        for field in ("observed", "interpretation"):
            if not text(resolution.get(field)):
                errors.append(f"resolution.{field} must be nonempty")
        if not string_list(resolution.get("unknowns"), nonempty=False):
            errors.append("resolution.unknowns must be a string list (may be empty)")
        references(resolution.get("source_ids"), "resolution")
    return errors


def validate(root=ROOT, index_path=None):
    root = Path(root).resolve()
    index_path = Path(index_path) if index_path is not None else root / "curriculum/2027.yaml"
    errors = []

    def load(path, label):
        try:
            data = read_yaml(path)
            if not isinstance(data, dict):
                raise ValueError("expected a YAML mapping")
            return data
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{label}: {exc}")
            return None

    data = load(index_path, "curriculum")
    if data is None:
        return errors
    if type(data.get("year")) is not int or data["year"] != 2027:
        errors.append("year must be integer 2027")
    if data.get("timezone") != "Pacific/Auckland":
        errors.append("timezone must be Pacific/Auckland")
    entries = data.get("entries")
    if not isinstance(entries, list):
        return errors + ["entries must be an array"]
    if len(entries) != 365:
        errors.append(f"expected 365 entries, found {len(entries)}")
    runner = None
    try:
        runner = local_path(root, "protocols/runner.md")
    except ValueError as exc:
        errors.append(f"runner: {exc}")
    dates, ids = [], []
    for number, entry in enumerate(entries, 1):
        if not isinstance(entry, dict):
            errors.append(f"entry {number}: expected a mapping")
            continue
        label = f"entry {number} ({entry.get('id', '?')})"
        kind, domain, status = (entry.get(k) for k in ("kind", "domain", "status"))
        # Tuple membership also rejects malformed list/dict values without crashing.
        for field, value, allowed in (
            ("kind", kind, tuple(KINDS)), ("domain", domain, tuple(DOMAINS)),
            ("status", status, tuple(STATUSES)),
        ):
            if value not in allowed:
                errors.append(f"{label}: invalid {field}: {value!r}")
        identifier = entry.get("id")
        if not isinstance(identifier, str) or not re.fullmatch(r"(?:ENG|PRO|INV|DES)-\d{3}", identifier):
            errors.append(f"{label}: invalid ID")
        else:
            ids.append(identifier)
            prefix = "DES" if kind == "micro_design" else {
                "engineering": "ENG", "product": "PRO", "investing": "INV"
            }.get(domain if isinstance(domain, str) else "")
            if identifier.split("-")[0] != prefix:
                errors.append(f"{label}: ID prefix does not match kind/domain")
        for field in ("subdomain", "focus"):
            if not text(entry.get(field)):
                errors.append(f"{label}: requires {field}")
        if "review_status" in entry and entry["review_status"] not in ("accepted", "revise", "replace"):
            errors.append(f"{label}: invalid review_status")
        try:
            day = iso_date(entry.get("date"))
            dates.append(day)
            if day.year != 2027:
                errors.append(f"{label}: date outside 2027")
            weekday = day.weekday()
            if weekday == 6:
                ok = kind == "micro_design"
            else:
                expected_domain = "investing" if weekday == 5 else "product" if weekday in {1, 3} else "engineering"
                ok = kind == "historical" and domain == expected_domain
            if not ok:
                errors.append(f"{label}: weekday allocation mismatch")
        except (ValueError, TypeError) as exc:
            errors.append(f"{label}: invalid date: {exc}")
        paths = {}
        for field in ("brief_path", "protocol_path"):
            try:
                paths[field] = local_path(root, entry.get(field))
            except (ValueError, OSError) as exc:
                errors.append(f"{label}: {field}: {exc}")
        expected_protocol = "protocols/micro-design.md" if kind == "micro_design" else "protocols/historical.md"
        if entry.get("protocol_path") != expected_protocol:
            errors.append(f"{label}: protocol_path must be {expected_protocol}")
        expected_brief = f"designs/{identifier}.yaml" if kind == "micro_design" else f"cases/{domain}/{identifier}.yaml"
        if entry.get("brief_path") != expected_brief:
            errors.append(f"{label}: brief_path must be {expected_brief}")
        if "brief_path" not in paths:
            continue
        brief = load(paths["brief_path"], label)
        if brief is None:
            continue
        for field in ("id", "kind", "domain", "status"):
            if brief.get(field) != entry.get(field):
                errors.append(f"{label}: Brief/index {field} mismatch")
        if status == "ready":
            errors.extend(f"{label}: {issue}" for issue in ready_errors(brief))
            for path in (runner, paths.get("protocol_path")):
                if path is not None:
                    protocol = path.read_text(encoding="utf-8")
                    if not protocol.strip() or "status: draft" in protocol:
                        errors.append(f"{label}: ready entry uses empty/draft protocol {path.name}")
    for name, values in (("date", dates), ("ID", ids)):
        duplicates = [str(k) for k, count in Counter(values).items() if count > 1]
        if duplicates:
            errors.append(f"duplicate {name}: {', '.join(duplicates)}")
    expected = {date(2027, 1, 1) + timedelta(days=i) for i in range(365)}
    missing = sorted(expected - set(dates))
    if missing:
        errors.append("missing dates: " + ", ".join(map(str, missing)))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--index", type=Path, help="Optional alternative index file")
    args = parser.parse_args()
    errors = validate(args.root, args.index)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print("PASS: 365 dates, weekday allocation, IDs, fields, references and status structure.")
    print("Structural validation only; sources, spoiler safety and training quality require review.")


if __name__ == "__main__":
    main()
