# Party

_Parties, addresses, and contact information_

**Schema**: `core/party.schema.json`

## Address

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `line1` | `string` | Yes |  |
| `line2` | `string` | No |  |
| `city` | `string` | Yes |  |
| `state_province` | `string` | No |  |
| `postal_code` | `string` | No |  |
| `country` | `Country` | Yes |  |

## ContactInfo

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | Yes |  |
| `email` | `string` (email) | Yes |  |
| `phone` | `string` | No |  |
| `title` | `string` | No | Job title |

## PartyType

**Type**: `string`

**Values**:
- `GP`
- `LP`
- `FUND_ADMIN`
- `CUSTODIAN`
- `PLACEMENT_AGENT`
- `LEGAL_COUNSEL`
- `AUDITOR`
- `BORROWER`
- `LENDER`
- `BROKER`
- `OTHER`

## Party

_Extends_ `base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | Yes | Legal name of the party |
| `short_name` | `string` | No | Short or common name |
| `party_type` | `PartyType` | Yes |  |
| `external_ids` | array of `ExternalId` | No |  |
| `address` | `Address` | No |  |
| `contacts` | array of `ContactInfo` | No |  |
