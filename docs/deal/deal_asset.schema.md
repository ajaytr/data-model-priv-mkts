# Deal Asset

_References to domain-specific assets within a deal_

**Schema**: `deal/deal_asset.schema.json`

## DealAsset

A reference to an underlying asset in a deal, discriminated by asset_type

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `asset_type` | `DealAssetType` | Yes |  |
| `label` | `string` | Yes | Human-readable label (e.g., 'Senior Term Loan', 'Equity Co-Invest') |
| `facility_id` | `string` (uuid) | No | Reference to credit/Facility (when asset_type = FACILITY) |
| `investment_id` | `string` (uuid) | No | Reference to fund/Investment (when asset_type = INVESTMENT) |
| `property_id` | `string` (uuid) | No | Reference to real_estate/Property (when asset_type = PROPERTY) |
| `lp_interest_id` | `string` (uuid) | No | Reference to secondaries/LPInterest (when asset_type = LP_INTEREST) |
| `notional_amount` | `Money` | No | Notional or face value of this asset within the deal |
