# Deal

_Central deal entity with participants and milestones_

**Schema**: `deal/deal.schema.json`

## DealParticipant

A party participating in a deal

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `party_id` | `string` (uuid) | Yes | Reference to Party |
| `role` | `DealRole` | Yes |  |
| `fund_id` | `string` (uuid) | No | Fund through which this party is investing (optional) |
| `commitment_amount` | `Money` | No |  |
| `ownership_percentage` | `Percentage` | No |  |

## DealMilestone

A stage in the deal lifecycle

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stage` | `DealStage` | Yes |  |
| `date` | `string` (date) | Yes |  |
| `completed` | `boolean` | No |  |
| `notes` | `string` | No |  |

## Deal

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | Yes | Deal name (e.g., 'Acme Corp LBO') |
| `description` | `string` | No |  |
| `asset_class` | `AssetClass` | Yes |  |
| `stage` | `DealStage` | Yes |  |
| `deal_size` | `Money` | No | Total deal size |
| `target_company` | `string` | No | Name of the target company or asset |
| `sector` | `string` | No |  |
| `region` | `Region` | No |  |
| `country` | `Country` | No |  |
| `sourced_date` | `string` (date) | No |  |
| `expected_close_date` | `string` (date) | No |  |
| `actual_close_date` | `string` (date) | No |  |
| `participants` | array of `DealParticipant` | No |  |
| `assets` | array of `DealAsset` | No |  |
| `milestones` | array of `DealMilestone` | No |  |
| `documents` | array of `string` (uuid) | No | References to Document entities |
