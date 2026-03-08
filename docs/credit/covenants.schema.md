# Covenants

_Financial and operational covenants attached to credit facilities_

**Schema**: `credit/covenants.schema.json`

## CovenantType

Category of financial or operational covenant

**Type**: `string`

**Values**:
- `LEVERAGE_RATIO`
- `INTEREST_COVERAGE`
- `FIXED_CHARGE_COVERAGE`
- `DEBT_TO_EBITDA`
- `MINIMUM_LIQUIDITY`
- `MINIMUM_REVENUE`
- `CAPEX_LIMIT`
- `INCURRENCE`
- `SPRINGING`
- `OTHER`

## Covenant

A covenant condition attached to a credit facility

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `facility_id` | `string` (uuid) | Yes | Reference to the parent facility |
| `covenant_type` | `CovenantType` | Yes |  |
| `description` | `string` | Yes | Human-readable description of the covenant |
| `threshold_value` | `number` | Yes | Numeric threshold for compliance testing |
| `threshold_operator` | enum: `LTE`, `GTE`, `LT`, `GT`, `EQ` | Yes | Comparison operator applied to actual vs threshold |
| `testing_frequency` | enum: `MONTHLY`, `QUARTERLY`, `SEMI_ANNUAL`, `ANNUAL` | Yes | How often the covenant is tested |
| `cure_period_days` | `integer` | No | Days allowed to cure a breach |
| `springing_trigger` | `string` | No | Condition that activates a springing covenant |

## CovenantTest

Result of a single covenant compliance test

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `covenant_id` | `string` (uuid) | Yes | Reference to the covenant being tested |
| `test_date` | `string` (date) | Yes |  |
| `actual_value` | `number` | Yes | Measured value at the test date |
| `threshold_value` | `number` | Yes | Threshold in effect at the test date |
| `in_compliance` | `boolean` | Yes | Whether the borrower is in compliance |
| `notes` | `string` | No | Additional context or commentary |
