# Lease

_Lease, tenant, lease options, and rent roll definitions_

**Schema**: `real_estate/lease.schema.json`

## Tenant

A tenant occupying leased space

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `tenant_id` | `string` (uuid) | Yes | Unique identifier for the tenant |
| `name` | `string` | Yes | Legal name of the tenant |
| `industry` | `string` | No | Industry classification of the tenant |
| `credit_rating` | `string` | No | Credit rating of the tenant (e.g., AAA, BB+) |

## LeaseOption

An option embedded within a lease agreement

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `option_type` | enum: `RENEWAL`, `EXPANSION`, `TERMINATION`, `RIGHT_OF_FIRST_REFUSAL`, `PURCHASE` | Yes | Type of lease option |
| `exercise_date` | `string` (date) | Yes | Date by which the option must be exercised |
| `terms` | `string` | No | Free-text description of option terms |

## Lease

A lease agreement for space within a property

_Extends_ `../core/base.schema.json#/$defs/Auditable`

**Type**: `object`

A lease agreement for space within a property

## RentRoll

A point-in-time snapshot of all leases for a property

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `property_id` | `string` (uuid) | Yes | Reference to the Property |
| `as_of_date` | `string` (date) | Yes | Date of the rent roll snapshot |
| `leases` | array of `string` (uuid) | Yes | References to active Lease entities |
| `total_monthly_rent` | `Money` | Yes | Sum of all monthly base rents |
| `occupied_sqft` | `number` | Yes | Total occupied square footage |
| `total_sqft` | `number` | Yes | Total leasable square footage |
| `occupancy_rate` | `Percentage` | Yes | Occupancy rate (occupied_sqft / total_sqft) |
