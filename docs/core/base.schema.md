# Base definitions

_Auditable base type for all domain entities_

**Schema**: `core/base.schema.json`

## Auditable

Common fields for all persistent entities

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `id` | `string` (uuid) | Yes | Unique identifier |
| `created_at` | `string` (date-time) | Yes | Timestamp when the record was created |
| `updated_at` | `string` (date-time) | No | Timestamp when the record was last updated |
