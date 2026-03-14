# Private Markets Data Model

A comprehensive, language-agnostic data model for private markets — covering PE/VC funds, private credit, real estate, secondaries, deal management, portfolio tracking, and trade lifecycle.

All models are defined as **JSON Schema 2020-12** files. No code generation lock-in — schemas serve as the single source of truth and can drive code generation for any language.

**[Interactive Schema Explorer](https://ajaytr.github.io/data-model-priv-mkts/)** — browse the full data model with drill-down navigation across Deal, Fund, and base Types.

## Domains

| Domain | Schemas | Description |
|--------|---------|-------------|
| **core** | base, money, percentage, party, identifiers, dates, enums | Shared types: Money, Party, Address, ExternalId, Auditable base |
| **fund** | fund, commitment, capital_activity, nav, waterfall, portfolio_company | PE/VC fund lifecycle — terms, capital calls, distributions, NAV, carry |
| **credit** | facility, interest, covenants, amortization, borrower | Private credit — facilities, tranches, rate definitions, covenant testing |
| **real_estate** | property, vehicle, lease, metrics | Real estate — properties, RE vehicles, leases, NOI, appraisals |
| **deal** | deal, deal_asset | Central deal entity linking participants to assets across domains |
| **secondaries** | lp_interest, trade, transaction, transfer | Secondary market — LP interests, bids/offers, GP consent, transfers |
| **portfolio** | position, portfolio, cash_flow, performance | Cross-asset portfolio — discriminated positions, unified cash flows, IRR/TVPI |
| **trade_lifecycle** | trade, settlement, documentation | Trade execution — state machine, settlement instructions, document tracking |

## Project Structure

```
schemas/          # JSON Schema 2020-12 definitions (source of truth)
examples/         # Realistic sample data validated against schemas
tools/            # Python validation and doc generation
docs/             # Generated markdown documentation
```

## Key Design Decisions

- **Money as decimal string** — `{"amount": "1500000.50", "currency": "USD"}` avoids floating-point precision loss
- **`allOf` composition** — entities inherit `id`, `created_at`, `updated_at` from `Auditable` base
- **`oneOf` + discriminator** — `Position` uses `position_type` to distinguish fund/credit/real estate positions
- **`$ref` cross-references** — schemas reference each other via relative paths; entity relationships use UUID strings
- **Deal as central entity** — links participants (with roles and fund vehicles) to assets across credit, equity, real estate, and secondaries

### Deal Model

A Deal ties together participants and assets across domains:

```
Deal: "Acme Corp LBO"
  ├── DealAsset: Senior Term Loan    → credit/Facility
  ├── DealAsset: Mezz Tranche        → credit/Facility
  ├── DealAsset: Equity Co-Invest    → fund/Investment
  ├── DealParticipant: PE Fund A (Lead, $50M)
  └── DealParticipant: Credit Fund B (Co-invest, $20M)
```

## Getting Started

### Validate examples against schemas

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install "jsonschema[format]>=4.21,<5" "referencing>=0.33,<1"
python tools/validate.py
```

### Generate documentation

```bash
python tools/generate_docs.py
# Output: docs/index.md + per-schema markdown files
```

### Use in your own project

Reference any schema via its path:

```json
{
  "$ref": "schemas/core/money.schema.json#/$defs/Money"
}
```

Or load schemas programmatically in Python, TypeScript, Go, etc. to generate types, validate API payloads, or seed test data.

## Schema Conventions

| Convention | Example |
|-----------|---------|
| Percentages as decimals | `0.08` = 8%, `0.02` = 2% |
| Basis points as integers | `450` = 4.50% |
| Dates as ISO 8601 | `"2024-06-15"`, `"2024-06-15T14:30:00Z"` |
| Entity references as UUIDs | `"fund_id": "f1a2b3c4-d5e6-7890-abcd-ef1234560001"` |
| Money amounts as strings | `"amount": "2000000000"` |

## Acknowledgments & References

This data model was not derived from a single open-source project, but its design draws on established industry standards and conventions:

- **[ILPA Reporting Standards](https://ilpa.org/reporting-template/)** — Institutional Limited Partners Association templates for LP reporting, capital call/distribution notices, and fund performance metrics. Influenced the fund domain's capital activity, NAV, and waterfall structures.
- **[ISDA CDM (Common Domain Model)](https://www.isda.org/a/z3igE/Digital-Regulatory-Reporting-ISDA-CDM-and-Beyond-December-2019.pdf)** — ISDA's standardized model for derivatives and financial products. Informed the trade lifecycle state machine, settlement patterns, and the approach to representing financial instruments as composable schemas.
- **[LSTA (Loan Syndications and Trading Association)](https://www.lsta.org/)** — Market conventions for par and distressed loan trading. Shaped the credit domain's facility/tranche structure, day-count conventions, and settlement workflows.
- **[FIX Protocol](https://www.fixtrading.org/)** — Financial Information eXchange standard for trade messaging. Influenced trade state transitions, settlement instruction fields, and party role classifications.
- **[ISO Standards](https://www.iso.org/)** — ISO 4217 (currency codes), ISO 3166-1 (country codes), ISO 8601 (date/time formats), and UUID (RFC 4122) are used throughout for interoperability.
- **[JSON Schema 2020-12 Specification](https://json-schema.org/specification)** — The schema language itself. All files conform to the 2020-12 draft, using `$ref`, `allOf` composition, `oneOf` with discriminator, and `$defs` for type definitions.

## License

Private — all rights reserved.
