#!/usr/bin/env python3
"""Validate example JSON files against their corresponding JSON Schemas.

Usage:
    python tools/validate.py                    # validate all examples
    python tools/validate.py examples/fund/     # validate specific directory
    python tools/validate.py examples/fund/sample_fund.json  # validate single file
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = PROJECT_ROOT / "schemas"
EXAMPLES_DIR = PROJECT_ROOT / "examples"

# Mapping: example file -> (schema file, definition name or None for top-level)
EXAMPLE_SCHEMA_MAP: dict[str, tuple[str, str | None]] = {
    "core/sample_party.json": ("core/party.schema.json", "Party"),
    "fund/sample_fund.json": ("fund/fund.schema.json", "Fund"),
    "fund/sample_capital_call.json": ("fund/capital_activity.schema.json", "CapitalCall"),
    "credit/sample_facility.json": ("credit/facility.schema.json", "Facility"),
    "real_estate/sample_property.json": ("real_estate/property.schema.json", "Property"),
    "deal/sample_lbo_deal.json": ("deal/deal.schema.json", "Deal"),
    "secondaries/sample_secondary_trade.json": ("secondaries/trade.schema.json", "SecondaryTrade"),
    "portfolio/sample_portfolio.json": ("portfolio/portfolio.schema.json", "Portfolio"),
}


def build_registry() -> Registry:
    """Build a referencing.Registry with all schema files loaded."""
    resources: list[tuple[str, Resource]] = []
    for schema_path in SCHEMAS_DIR.rglob("*.schema.json"):
        with open(schema_path) as f:
            schema = json.load(f)
        # Use the relative path from schemas/ as the URI
        rel = schema_path.relative_to(SCHEMAS_DIR)
        uri = str(rel)
        resource = Resource.from_contents(schema, default_specification=DRAFT202012)
        resources.append((uri, resource))
    registry = Registry().with_resources(resources)
    return registry


def resolve_schema_for_def(
    schema_path: str, def_name: str | None, registry: Registry
) -> dict:
    """Get the schema dict for validation, optionally extracting a $defs entry."""
    with open(SCHEMAS_DIR / schema_path) as f:
        schema = json.load(f)

    if def_name is None:
        return schema

    # Build a schema that $refs the definition
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$ref": f"{schema_path}#/$defs/{def_name}",
    }


def validate_example(
    example_rel: str, registry: Registry
) -> list[str]:
    """Validate a single example file. Returns list of error messages (empty = pass)."""
    if example_rel not in EXAMPLE_SCHEMA_MAP:
        return [f"No schema mapping for {example_rel}"]

    schema_path, def_name = EXAMPLE_SCHEMA_MAP[example_rel]
    example_path = EXAMPLES_DIR / example_rel

    if not example_path.exists():
        return [f"Example file not found: {example_path}"]

    with open(example_path) as f:
        data = json.load(f)

    schema = resolve_schema_for_def(schema_path, def_name, registry)
    validator = Draft202012Validator(schema, registry=registry)

    errors: list[str] = []

    # Handle arrays (e.g., sample_party.json is a list of parties)
    items = data if isinstance(data, list) else [data]
    for i, item in enumerate(items):
        for err in validator.iter_errors(item):
            prefix = f"[{i}] " if isinstance(data, list) else ""
            errors.append(f"{prefix}{err.json_path}: {err.message}")

    return errors


def main() -> int:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    registry = build_registry()

    # Determine which examples to validate
    if target and target.is_file():
        examples = [str(target.relative_to(EXAMPLES_DIR))]
    elif target and target.is_dir():
        examples = [
            str(p.relative_to(EXAMPLES_DIR))
            for p in target.rglob("*.json")
        ]
    else:
        examples = list(EXAMPLE_SCHEMA_MAP.keys())

    total = 0
    failed = 0
    for example_rel in sorted(examples):
        total += 1
        errors = validate_example(example_rel, registry)
        if errors:
            failed += 1
            print(f"FAIL  {example_rel}")
            for e in errors:
                print(f"      {e}")
        else:
            print(f"OK    {example_rel}")

    print(f"\n{total} examples, {total - failed} passed, {failed} failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
