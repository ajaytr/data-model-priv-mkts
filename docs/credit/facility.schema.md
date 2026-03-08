# Facility

_Credit facility and tranche definitions_

**Schema**: `credit/facility.schema.json`

## Tranche

A sub-division of a facility with its own commitment and rate terms

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tranche_id` | `string` (uuid) | Yes | Unique identifier for this tranche |
| `tranche_name` | `string` | Yes | Descriptive name (e.g., Term Loan A, Revolver) |
| `commitment_amount` | `Money` | Yes |  |
| `funded_amount` | `Money` | No |  |
| `rate_definition` | `RateDefinition` | Yes |  |
| `seniority` | `SeniorityLevel` | Yes |  |

## Facility

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | Yes | Facility name |
| `borrower_id` | `string` (uuid) | Yes | Reference to the borrower party |
| `facility_type` | `FacilityType` | Yes |  |
| `total_commitment` | `Money` | Yes |  |
| `funded_amount` | `Money` | No |  |
| `unfunded_amount` | `Money` | No |  |
| `currency` | `Currency` | Yes |  |
| `seniority` | `SeniorityLevel` | Yes |  |
| `closing_date` | `string` (date) | Yes |  |
| `maturity_date` | `string` (date) | Yes |  |
| `tranches` | array of `Tranche` | No |  |
| `status` | enum: `ACTIVE`, `DRAWN`, `FULLY_REPAID`, `DEFAULTED`, `RESTRUCTURED` | Yes | Current status of the facility |
| `external_ids` | array of `ExternalId` | No |  |
