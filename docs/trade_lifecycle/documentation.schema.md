# Documentation

_Document tracking for trade lifecycle and deal management_

**Schema**: `trade_lifecycle/documentation.schema.json`

## Document

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `document_type` | `DocumentType` | Yes |  |
| `title` | `string` | Yes |  |
| `description` | `string` | No |  |
| `file_name` | `string` | No |  |
| `mime_type` | `string` | No |  |
| `file_size_bytes` | `integer` | No |  |
| `storage_url` | `string` (uri) | No | URL or path to the stored document |
| `version` | `integer` | No |  |
| `uploaded_by` | `string` | No |  |
| `entity_id` | `string` (uuid) | No | UUID of the related entity (deal, trade, fund, etc.) |
| `entity_type` | `string` | No | Type of the related entity |
| `execution_date` | `string` (date) | No | Date the document was executed/signed |
| `expiry_date` | `string` (date) | No |  |

## DocumentRequirement

A required document for a deal or trade

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `document_type` | `DocumentType` | Yes |  |
| `description` | `string` | No |  |
| `required` | `boolean` | No |  |
| `received` | `boolean` | No |  |
| `document_id` | `string` (uuid) | No | Reference to the received Document, if any |
| `due_date` | `string` (date) | No |  |
