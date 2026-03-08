# LP Interest

_LP interest positions available for secondary trading_

**Schema**: `secondaries/lp_interest.schema.json`

## LPInterest

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fund_id` | `string` (uuid) | Yes | Reference to Fund |
| `fund_name` | `string` | No | Denormalized fund name for convenience |
| `seller_id` | `string` (uuid) | Yes | Reference to Party (current LP) |
| `commitment_id` | `string` (uuid) | No | Reference to Commitment |
| `total_commitment` | `Money` | Yes |  |
| `funded_amount` | `Money` | No |  |
| `unfunded_amount` | `Money` | No |  |
| `nav` | `Money` | Yes | Most recent NAV |
| `nav_date` | `string` (date) | No |  |
| `distributions_received` | `Money` | No |  |
| `vintage_year` | `integer` | No |  |
| `fund_strategy` | `string` | No | Fund strategy (denormalized from Fund) |
| `remaining_fund_life_years` | `number` | No |  |
