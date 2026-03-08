# Settlement

_Settlement instructions for trade execution_

**Schema**: `trade_lifecycle/settlement.schema.json`

## SettlementInstruction

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `trade_id` | `string` (uuid) | Yes | Reference to Trade |
| `payment_amount` | `Money` | Yes |  |
| `settlement_date` | `string` (date) | Yes |  |
| `payer_id` | `string` (uuid) | Yes | Reference to Party |
| `payee_id` | `string` (uuid) | Yes | Reference to Party |
| `payment_method` | enum: `WIRE`, `ACH`, `CHECK`, `DTC`, `IN_KIND` | No |  |
| `bank_name` | `string` | No |  |
| `account_number` | `string` | No |  |
| `routing_number` | `string` | No |  |
| `swift_code` | `string` | No |  |
| `reference` | `string` | No |  |
| `status` | enum: `PENDING`, `INSTRUCTED`, `CONFIRMED`, `SETTLED`, `FAILED`, `CANCELLED` | Yes |  |
| `settled_at` | `string` (date-time) | No |  |
