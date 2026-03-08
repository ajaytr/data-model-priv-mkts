# Transaction

_Secondary transaction lifecycle_

**Schema**: `secondaries/transaction.schema.json`

## TransactionMilestone

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `stage` | `TransactionStage` | Yes |  |
| `date` | `string` (date) | Yes |  |
| `completed` | `boolean` | No |  |
| `notes` | `string` | No |  |

## Transaction

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `trade_id` | `string` (uuid) | Yes | Reference to SecondaryTrade |
| `stage` | `TransactionStage` | Yes |  |
| `milestones` | array of `TransactionMilestone` | No |  |
| `gp_consent_required` | `boolean` | No |  |
| `gp_consent_received` | `boolean` | No |  |
| `gp_consent_date` | `string` (date) | No |  |
| `transfer_agent` | `string` (uuid) | No | Reference to Party handling the transfer |
| `legal_counsel_buyer` | `string` (uuid) | No |  |
| `legal_counsel_seller` | `string` (uuid) | No |  |
| `documents` | array of `string` (uuid) | No | References to Document entities |
| `closing_date` | `string` (date) | No |  |
| `effective_date` | `string` (date) | No | Date the transfer becomes effective on the fund's books |
