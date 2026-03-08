# Transfer Record

_Record of completed LP interest transfers_

**Schema**: `secondaries/transfer.schema.json`

## TransferRecord

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `transaction_id` | `string` (uuid) | Yes | Reference to Transaction |
| `fund_id` | `string` (uuid) | Yes |  |
| `from_investor_id` | `string` (uuid) | Yes | Selling LP (Party) |
| `to_investor_id` | `string` (uuid) | Yes | Buying LP (Party) |
| `old_commitment_id` | `string` (uuid) | No | Reference to original Commitment being transferred |
| `new_commitment_id` | `string` (uuid) | No | Reference to newly created Commitment for the buyer |
| `transferred_commitment` | `Money` | Yes |  |
| `transferred_unfunded` | `Money` | No |  |
| `purchase_price` | `Money` | Yes |  |
| `effective_date` | `string` (date) | Yes |  |
| `settlement_date` | `string` (date) | No |  |
| `transfer_fee` | `Money` | No | Fee charged by the GP for processing the transfer |
