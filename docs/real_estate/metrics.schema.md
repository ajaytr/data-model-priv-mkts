# Real estate metrics

_NOI statements and appraisal definitions for real estate properties_

**Schema**: `real_estate/metrics.schema.json`

## NOIStatement

Net operating income statement for a property over a reporting period

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `property_id` | `string` (uuid) | Yes | Reference to the Property |
| `period` | `ReportingPeriod` | Yes | Reporting period covered by this statement |
| `gross_revenue` | `Money` | Yes | Total gross rental and ancillary revenue |
| `vacancy_loss` | `Money` | Yes | Revenue lost due to vacancy |
| `effective_gross_income` | `Money` | Yes | Gross revenue minus vacancy loss |
| `operating_expenses` | `Money` | Yes | Total property operating expenses |
| `net_operating_income` | `Money` | Yes | Effective gross income minus operating expenses |
| `capital_expenditures` | `Money` | No | Capital expenditures during the period |

## Appraisal

A formal property appraisal

_Extends_ `../core/base.schema.json#/$defs/Auditable`

**Type**: `object`

A formal property appraisal
