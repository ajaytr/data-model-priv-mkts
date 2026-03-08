# Commitment

_LP commitments to a fund and associated side letter terms_

**Schema**: `fund/commitment.schema.json`

## Commitment

An LP's capital commitment to a fund

_Extends_ `../core/base.schema.json#/$defs/Auditable`

**Type**: `object`

An LP's capital commitment to a fund

## SideLetterTerms

Terms negotiated in a side letter agreement

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `fee_discount` | `Percentage` | No | Discount on management fee rate |
| `co_investment_rights` | `boolean` | No | Whether the investor has co-investment rights |
| `most_favored_nation` | `boolean` | No | Whether MFN rights apply |
| `excuse_rights` | array of `string` | No | Sectors or investment types the investor may opt out of |
| `reporting_requirements` | array of `string` | No | Additional reporting obligations |
