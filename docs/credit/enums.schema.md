# Credit enumerations

_Enumerations specific to private credit facilities and instruments_

**Schema**: `credit/enums.schema.json`

## FacilityType

Type of credit facility

**Type**: `string`

**Values**:
- `TERM_LOAN`
- `REVOLVING_CREDIT`
- `DELAYED_DRAW`
- `BRIDGE_LOAN`
- `UNITRANCHE`
- `FIRST_LIEN`
- `SECOND_LIEN`
- `MEZZANINE`
- `PIK`

## RateType

Interest rate structure type

**Type**: `string`

**Values**:
- `FIXED`
- `FLOATING`
- `PIK`
- `FIXED_PLUS_PIK`
- `FLOATING_PLUS_PIK`

## RateIndex

Reference rate index for floating-rate instruments

**Type**: `string`

**Values**:
- `SOFR`
- `TERM_SOFR`
- `EURIBOR`
- `SONIA`
- `PRIME`
- `FED_FUNDS`

## SeniorityLevel

Position in the capital structure

**Type**: `string`

**Values**:
- `SUPER_SENIOR`
- `SENIOR_SECURED`
- `SENIOR_UNSECURED`
- `SUBORDINATED`
- `MEZZANINE`
- `JUNIOR`
- `EQUITY`
