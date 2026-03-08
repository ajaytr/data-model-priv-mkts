# Portfolio

_A portfolio containing positions across asset types_

**Schema**: `portfolio/portfolio.schema.json`

## Portfolio

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `name` | `string` | Yes |  |
| `owner_id` | `string` (uuid) | Yes | Reference to Party that owns this portfolio |
| `as_of_date` | `string` (date) | Yes |  |
| `positions` | array of `Position` | No |  |
| `total_nav` | `Money` | No |  |
| `total_commitments` | `Money` | No |  |
| `total_unfunded` | `Money` | No |  |
