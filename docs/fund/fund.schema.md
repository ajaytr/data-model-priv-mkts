# Fund

_Fund entity and fund terms for private market funds_

**Schema**: `fund/fund.schema.json`

## Fund

A private markets fund vehicle

_Extends_ `../core/base.schema.json#/$defs/Auditable`

**Type**: `object`

A private markets fund vehicle

## FundTerms

Economic and governance terms of a fund

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fund_life_years` | `integer` | No | Total fund life in years (typically 10-12) |
| `investment_period_years` | `integer` | No | Investment period in years (typically 4-6) |
| `management_fee_rate` | `Percentage` | No | Annual management fee rate |
| `carried_interest_rate` | `Percentage` | No | Carried interest rate (typically 20%) |
| `preferred_return` | `Percentage` | No | Preferred return (hurdle) rate |
| `gp_commitment_rate` | `Percentage` | No | GP commitment as a percentage of fund size |
| `hurdle_rate` | `Percentage` | No | Hurdle rate for carried interest calculation |
| `clawback` | `boolean` | No | Whether a GP clawback provision exists |
| `key_person_clause` | `boolean` | No | Whether a key person clause exists |
