# Borrower

_Borrower entity extending the core Party with credit-specific attributes_

**Schema**: `credit/borrower.schema.json`

## Borrower

_Extends_ `../core/party.schema.json#/$defs/Party`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `industry` | `string` | Yes | Primary industry classification |
| `revenue` | `Money` | No | Most recent annual revenue |
| `ebitda` | `Money` | No | Most recent EBITDA |
| `total_debt` | `Money` | No | Total outstanding debt |
| `credit_rating` | `string` | No | External or internal credit rating |
| `sponsor_id` | `string` (uuid) | No | Reference to the PE sponsor party, if sponsor-backed |
