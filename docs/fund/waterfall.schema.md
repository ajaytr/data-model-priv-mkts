# Waterfall

_Distribution waterfall structures and carried interest allocations_

**Schema**: `fund/waterfall.schema.json`

## WaterfallStructure

The distribution waterfall model for a fund

_Extends_ `../core/base.schema.json#/$defs/Auditable`

**Type**: `object`

The distribution waterfall model for a fund

## WaterfallTier

A single tier in the distribution waterfall

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tier_name` | `string` | Yes | Human-readable name of the tier |
| `tier_order` | `integer` | Yes | Order of this tier in the waterfall (1 = first) |
| `threshold_type` | enum: `PREFERRED_RETURN`, `CATCH_UP`, `CARRIED_INTEREST`, `RETURN_OF_CAPITAL` | Yes | Type of threshold for this tier |
| `threshold_rate` | `Percentage` | No | Rate threshold, if applicable |
| `gp_split` | `Percentage` | Yes | GP share of distributions in this tier |
| `lp_split` | `Percentage` | Yes | LP share of distributions in this tier |

## CarryAllocation

Carried interest allocation for a distribution period

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `waterfall_id` | `string` (uuid) | Yes | Reference to the waterfall structure |
| `distribution_id` | `string` (uuid) | Yes | Reference to the distribution |
| `period` | `ReportingPeriod` | Yes | Reporting period for this allocation |
| `gross_proceeds` | `Money` | Yes | Total gross proceeds being distributed |
| `lp_share` | `Money` | Yes | LP share of the distribution |
| `gp_carry` | `Money` | Yes | GP carried interest amount |
| `clawback_reserve` | `Money` | No | Amount reserved for potential clawback |
