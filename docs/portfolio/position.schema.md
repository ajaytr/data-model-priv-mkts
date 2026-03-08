# Position

_Portfolio positions across asset types, using discriminated union_

**Schema**: `portfolio/position.schema.json`

## PositionType

**Type**: `string`

**Values**:
- `FUND`
- `CREDIT`
- `REAL_ESTATE`

## FundPosition

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `position_type` | `"FUND"` | Yes |  |
| `fund_id` | `string` (uuid) | Yes |  |
| `commitment_id` | `string` (uuid) | No |  |
| `commitment_amount` | `Money` | Yes |  |
| `funded_amount` | `Money` | No |  |
| `unfunded_amount` | `Money` | No |  |
| `distributions_received` | `Money` | No |  |
| `current_nav` | `Money` | Yes |  |
| `nav_date` | `string` (date) | No |  |
| `dpi` | `number` | No | Distributions to Paid-In |
| `tvpi` | `number` | No | Total Value to Paid-In |
| `irr` | `Percentage` | No | Net IRR |

## CreditPosition

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `position_type` | `"CREDIT"` | Yes |  |
| `facility_id` | `string` (uuid) | Yes |  |
| `tranche_id` | `string` (uuid) | No |  |
| `par_amount` | `Money` | Yes |  |
| `market_value` | `Money` | Yes |  |
| `accrued_interest` | `Money` | No |  |
| `current_rate` | `Percentage` | No |  |
| `maturity_date` | `string` (date) | No |  |
| `price` | `number` | No | Current price as percentage of par (e.g., 98.5) |

## RealEstatePosition

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `position_type` | `"REAL_ESTATE"` | Yes |  |
| `property_id` | `string` (uuid) | Yes |  |
| `vehicle_id` | `string` (uuid) | No | Reference to REVehicle |
| `ownership_percentage` | `Percentage` | No |  |
| `cost_basis` | `Money` | Yes |  |
| `current_valuation` | `Money` | Yes |  |
| `valuation_date` | `string` (date) | No |  |
| `noi_annual` | `Money` | No |  |
| `cap_rate` | `Percentage` | No |  |

## Position

