# Amortization

_Amortization schedules and scheduled payments for credit facilities_

**Schema**: `credit/amortization.schema.json`

## ScheduledPayment

A single scheduled principal and/or interest payment

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `payment_date` | `string` (date) | Yes |  |
| `principal_amount` | `Money` | Yes |  |
| `interest_amount` | `Money` | No | Estimated or actual interest component |
| `total_amount` | `Money` | Yes |  |
| `status` | enum: `SCHEDULED`, `PAID`, `OVERDUE`, `WAIVED` | Yes | Current status of this payment |

## AmortizationSchedule

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `facility_id` | `string` (uuid) | Yes | Reference to the parent facility |
| `schedule_type` | enum: `BULLET`, `AMORTIZING`, `CUSTOM`, `INTEREST_ONLY` | Yes | Repayment structure type |
| `payments` | array of `ScheduledPayment` | Yes |  |
