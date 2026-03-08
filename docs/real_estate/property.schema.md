# Property

_Real estate property and valuation definitions_

**Schema**: `real_estate/property.schema.json`

## PropertyValuation

A point-in-time valuation of a property

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `valuation_date` | `string` (date) | Yes | Date of the valuation |
| `appraised_value` | `Money` | Yes | Appraised market value |
| `cap_rate` | `Percentage` | No | Capitalization rate |
| `price_per_sqft` | `Money` | No | Price per square foot |
| `valuation_method` | enum: `APPRAISAL`, `COMPARABLE_SALES`, `DCF`, `REPLACEMENT_COST` | Yes | Methodology used for the valuation |
| `appraiser` | `string` | No | Name of the appraiser or appraisal firm |

## Property

A real estate property asset

_Extends_ `../core/base.schema.json#/$defs/Auditable`

**Type**: `object`

A real estate property asset
