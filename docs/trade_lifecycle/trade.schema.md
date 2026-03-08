# Trade

_Trade entity and state transitions for the trade lifecycle_

**Schema**: `trade_lifecycle/trade.schema.json`

## TradeStatus

**Type**: `string`

**Values**:
- `INDICATIVE`
- `NEGOTIATING`
- `AGREED`
- `PENDING_DOCUMENTATION`
- `PENDING_SETTLEMENT`
- `SETTLED`
- `CANCELLED`
- `FAILED`

## Trade

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `trade_date` | `string` (date) | Yes |  |
| `settlement_date` | `string` (date) | No |  |
| `buyer_id` | `string` (uuid) | Yes | Reference to Party |
| `seller_id` | `string` (uuid) | Yes | Reference to Party |
| `broker_id` | `string` (uuid) | No | Reference to Party (optional broker/intermediary) |
| `asset_description` | `string` | No | Human-readable description of the traded asset |
| `asset_reference_id` | `string` (uuid) | No | UUID reference to the underlying asset (fund position, facility, etc.) |
| `price` | `Money` | Yes |  |
| `notional_amount` | `Money` | No |  |
| `status` | `TradeStatus` | Yes |  |
| `transitions` | array of `TradeStateTransition` | No |  |
| `documents` | array of `string` (uuid) | No | References to Document entities |

## TradeStateTransition

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `from_status` | `TradeStatus` | Yes |  |
| `to_status` | `TradeStatus` | Yes |  |
| `transition_date` | `string` (date-time) | Yes |  |
| `transitioned_by` | `string` | No | User or system that triggered the transition |
| `notes` | `string` | No |  |
