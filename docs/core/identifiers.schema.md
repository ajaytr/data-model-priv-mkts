# Identifiers

_External identifier types_

**Schema**: `core/identifiers.schema.json`

## ExternalId

Reference to an identifier in an external system

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `system` | `string` | Yes | Name of the external system (e.g., LEI, CUSIP, Bloomberg) |
| `value` | `string` | Yes | The identifier value in the external system |
