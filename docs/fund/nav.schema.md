# NAV reporting

_Net asset value statements, investor NAV, and investment valuations_

**Schema**: `fund/nav.schema.json`

## NAVStatement

A fund-level net asset value statement for a reporting period

_Extends_ `../core/base.schema.json#/$defs/Auditable`

**Type**: `object`

A fund-level net asset value statement for a reporting period

## InvestorNAV

An individual investor's NAV within a fund

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `commitment_id` | `string` (uuid) | Yes | Reference to the commitment |
| `investor_id` | `string` (uuid) | Yes | Reference to the investor (Party) |
| `nav` | `Money` | Yes | Investor's NAV |
| `ownership_percentage` | `Percentage` | Yes | Investor's ownership share |
| `total_contributed` | `Money` | Yes | Total capital contributed by this investor |
| `total_distributed` | `Money` | Yes | Total distributions received by this investor |

## InvestmentValuation

Fair value of a single portfolio investment

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `investment_id` | `string` (uuid) | Yes | Reference to the investment |
| `company_name` | `string` | Yes | Name of the portfolio company |
| `fair_value` | `Money` | Yes | Current fair value |
| `cost_basis` | `Money` | Yes | Original cost basis |
| `unrealized_gain_loss` | `Money` | Yes | Unrealized gain or loss (fair_value - cost_basis) |
| `valuation_method` | enum: `MARKET_COMPARABLE`, `DCF`, `RECENT_TRANSACTION`, `THIRD_PARTY_APPRAISAL`, `COST` | Yes | Methodology used for valuation |
