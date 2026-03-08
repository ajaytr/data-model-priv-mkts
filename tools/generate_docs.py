#!/usr/bin/env python3
"""Generate Markdown documentation from JSON Schema files.

Usage:
    python tools/generate_docs.py              # generate all docs
    python tools/generate_docs.py schemas/fund # generate for one domain
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = PROJECT_ROOT / "schemas"
DOCS_DIR = PROJECT_ROOT / "docs"


def schema_to_markdown(schema_path: Path) -> str:
    """Convert a single schema file to Markdown documentation."""
    with open(schema_path) as f:
        schema = json.load(f)

    rel = schema_path.relative_to(SCHEMAS_DIR)
    lines: list[str] = []
    lines.append(f"# {schema.get('title', rel.stem)}")
    lines.append("")
    if desc := schema.get("description"):
        lines.append(f"_{desc}_")
        lines.append("")
    lines.append(f"**Schema**: `{rel}`")
    lines.append("")

    defs = schema.get("$defs", {})
    if not defs:
        return "\n".join(lines)

    for def_name, def_schema in defs.items():
        lines.append(f"## {def_name}")
        lines.append("")
        if d := def_schema.get("description"):
            lines.append(d)
            lines.append("")

        # Handle allOf: merge properties from all sub-schemas
        properties = {}
        required = set()
        if "allOf" in def_schema:
            for sub in def_schema["allOf"]:
                if "$ref" in sub:
                    ref = sub["$ref"]
                    lines.append(f"_Extends_ `{ref}`")
                    lines.append("")
                if "properties" in sub:
                    properties.update(sub["properties"])
                if "required" in sub:
                    required.update(sub["required"])
        else:
            properties = def_schema.get("properties", {})
            required = set(def_schema.get("required", []))

        # Handle enum types
        if "enum" in def_schema:
            lines.append(f"**Type**: `{def_schema.get('type', 'string')}`")
            lines.append("")
            lines.append("**Values**:")
            for val in def_schema["enum"]:
                lines.append(f"- `{val}`")
            lines.append("")
            continue

        if not properties:
            # Simple type (e.g., Percentage)
            if "type" in def_schema:
                lines.append(f"**Type**: `{def_schema['type']}`")
                constraints = []
                if "minimum" in def_schema:
                    constraints.append(f"min: {def_schema['minimum']}")
                if "maximum" in def_schema:
                    constraints.append(f"max: {def_schema['maximum']}")
                if constraints:
                    lines.append(f"**Constraints**: {', '.join(constraints)}")
                if d := def_schema.get("description"):
                    lines.append(f"\n{d}")
            lines.append("")
            continue

        # Property table
        lines.append("| Property | Type | Required | Description |")
        lines.append("|----------|------|----------|-------------|")
        for prop_name, prop_schema in properties.items():
            req = "Yes" if prop_name in required else "No"
            ptype = _get_type_str(prop_schema)
            pdesc = prop_schema.get("description", "")
            lines.append(f"| `{prop_name}` | {ptype} | {req} | {pdesc} |")
        lines.append("")

    return "\n".join(lines)


def _get_type_str(prop: dict) -> str:
    """Get a human-readable type string for a property."""
    if "$ref" in prop:
        ref = prop["$ref"]
        # Extract just the definition name
        if "#/$defs/" in ref:
            return f"`{ref.split('#/$defs/')[-1]}`"
        return f"`{ref}`"
    if "const" in prop:
        return f'`"{prop["const"]}"`'
    if "enum" in prop:
        return "enum: " + ", ".join(f"`{v}`" for v in prop["enum"])
    t = prop.get("type", "any")
    fmt = prop.get("format")
    if t == "array":
        items = prop.get("items", {})
        item_type = _get_type_str(items)
        return f"array of {item_type}"
    if fmt:
        return f"`{t}` ({fmt})"
    return f"`{t}`"


def main() -> None:
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else None
    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    if target and target.is_file():
        schema_files = [target]
    elif target and target.is_dir():
        schema_files = sorted(target.rglob("*.schema.json"))
    else:
        schema_files = sorted(SCHEMAS_DIR.rglob("*.schema.json"))

    index_lines: list[str] = ["# Private Markets Data Model — Schema Documentation", ""]

    current_domain = None
    for schema_path in schema_files:
        rel = schema_path.relative_to(SCHEMAS_DIR)
        domain = rel.parts[0]
        doc_path = DOCS_DIR / rel.with_suffix(".md")
        doc_path.parent.mkdir(parents=True, exist_ok=True)

        md = schema_to_markdown(schema_path)
        doc_path.write_text(md)

        if domain != current_domain:
            current_domain = domain
            index_lines.append(f"## {domain.replace('_', ' ').title()}")
            index_lines.append("")

        doc_rel = doc_path.relative_to(DOCS_DIR)
        title = json.loads(schema_path.read_text()).get("title", rel.stem)
        index_lines.append(f"- [{title}]({doc_rel})")

    index_lines.append("")
    (DOCS_DIR / "index.md").write_text("\n".join(index_lines))

    print(f"Generated docs for {len(schema_files)} schemas in {DOCS_DIR}/")


if __name__ == "__main__":
    main()
