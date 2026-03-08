# Interest

_Rate definitions and interest period calculations for credit facilities_

**Schema**: `credit/interest.schema.json`

## RateDefinition

Defines the interest rate structure for a facility or tranche

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `rate_type` | `RateType` | Yes |  |
| `fixed_rate` | `Percentage` | No | Fixed interest rate component |
| `spread` | `BasisPoints` | No | Spread over the reference index in basis points |
| `index` | `RateIndex` | No |  |
| `floor` | `Percentage` | No | Minimum rate floor |
| `cap` | `Percentage` | No | Maximum rate cap |
| `day_count` | `DayCount` | Yes |  |
| `pik_rate` | `Percentage` | No | Payment-in-kind interest rate component |

## InterestPeriod

A single interest accrual period with calculated amounts

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `facility_id` | `string` (uuid) | Yes | Reference to the parent facility |
| `tranche_id` | `string` (uuid) | No | Reference to a specific tranche, if applicable |
| `period_start` | `string` (date) | Yes |  |
| `period_end` | `string` (date) | Yes |  |
| `principal_balance` | `Money` | Yes |  |
| `applicable_rate` | `Percentage` | Yes | All-in rate applied for this period |
| `interest_amount` | `Money` | Yes |  |
| `pik_amount` | `Money` | No | Payment-in-kind interest capitalized to principal |
| `paid` | `boolean` | Yes | Whether the cash interest for this period has been paid |
