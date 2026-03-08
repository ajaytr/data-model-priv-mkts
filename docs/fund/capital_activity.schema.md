# Capital activity

_Capital calls, distributions, and their per-investor allocations_

**Schema**: `fund/capital_activity.schema.json`

## CapitalCall

A capital call issued by the fund to its investors

_Extends_ `../core/base.schema.json#/$defs/Auditable`

**Type**: `object`

A capital call issued by the fund to its investors

## CallAllocation

A single investor's share of a capital call

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `commitment_id` | `string` (uuid) | Yes | Reference to the commitment |
| `investor_id` | `string` (uuid) | Yes | Reference to the investor (Party) |
| `called_amount` | `Money` | Yes | Amount called from this investor |
| `ownership_percentage` | `Percentage` | Yes | Investor's ownership percentage at time of call |

## Distribution

A distribution from the fund to its investors

_Extends_ `../core/base.schema.json#/$defs/Auditable`

**Type**: `object`

A distribution from the fund to its investors

## DistributionAllocation

A single investor's share of a distribution

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `commitment_id` | `string` (uuid) | Yes | Reference to the commitment |
| `investor_id` | `string` (uuid) | Yes | Reference to the investor (Party) |
| `amount` | `Money` | Yes | Amount distributed to this investor |
| `withholding_tax` | `Money` | No | Tax withheld from this distribution |
