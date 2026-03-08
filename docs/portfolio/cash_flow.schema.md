# Cash Flow

_Unified cash flow representation across asset types_

**Schema**: `portfolio/cash_flow.schema.json`

## CashFlowType

**Type**: `string`

**Values**:
- `CAPITAL_CALL`
- `DISTRIBUTION`
- `INTEREST_PAYMENT`
- `PRINCIPAL_PAYMENT`
- `FEE`
- `DIVIDEND`
- `RENT`
- `PURCHASE`
- `SALE`
- `OTHER`

## CashFlow

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `portfolio_id` | `string` (uuid) | No |  |
| `position_id` | `string` (uuid) | No | Reference to the Position that generated this cash flow |
| `cash_flow_type` | `CashFlowType` | Yes |  |
| `direction` | enum: `INFLOW`, `OUTFLOW` | Yes |  |
| `amount` | `Money` | Yes |  |
| `cash_flow_date` | `string` (date) | Yes |  |
| `description` | `string` | No |  |
| `source_entity_id` | `string` (uuid) | No | UUID of the originating entity (CapitalCall, Distribution, InterestPeriod, etc.) |
| `source_entity_type` | `string` | No |  |
