# Money

_Monetary amount with currency_

**Schema**: `core/money.schema.json`

## Money

A monetary value represented as a decimal string to avoid floating-point issues

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `amount` | `string` | Yes | Decimal amount as string to preserve precision |
| `currency` | `Currency` | Yes |  |
