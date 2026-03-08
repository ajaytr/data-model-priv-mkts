# Date types

_Quarter, reporting period, and date range types_

**Schema**: `core/dates.schema.json`

## Quarter

A fiscal quarter

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `year` | `integer` | Yes |  |
| `quarter` | `integer` | Yes |  |

## ReportingPeriod

A reporting period with start/end dates and optional quarter

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `start_date` | `string` (date) | Yes |  |
| `end_date` | `string` (date) | Yes |  |
| `quarter` | `Quarter` | No |  |

## DateRange

An arbitrary date range

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `start_date` | `string` (date) | Yes |  |
| `end_date` | `string` (date) | Yes |  |
