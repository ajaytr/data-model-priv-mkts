# Performance Metrics

_Performance analytics for positions and funds_

**Schema**: `portfolio/performance.schema.json`

## PerformanceMetrics

Common performance metrics for any private markets position

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `as_of_date` | `string` (date) | Yes |  |
| `irr_net` | `number` | No | Net IRR (decimal, e.g., 0.15 = 15%) |
| `irr_gross` | `number` | No | Gross IRR |
| `tvpi` | `number` | No | Total Value to Paid-In multiple |
| `dpi` | `number` | No | Distributions to Paid-In multiple |
| `rvpi` | `number` | No | Residual Value to Paid-In multiple |
| `moic` | `number` | No | Multiple on Invested Capital |
| `pme` | `number` | No | Public Market Equivalent (Kaplan-Schoar) |

## FundPerformance

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fund_id` | `string` (uuid) | Yes |  |
| `reporting_period` | `ReportingPeriod` | Yes |  |
| `metrics` | `PerformanceMetrics` | Yes |  |
| `total_committed` | `Money` | No |  |
| `total_called` | `Money` | No |  |
| `total_distributed` | `Money` | No |  |
| `total_nav` | `Money` | No |  |
| `num_investments` | `integer` | No |  |
| `num_realized` | `integer` | No |  |
| `num_unrealized` | `integer` | No |  |
