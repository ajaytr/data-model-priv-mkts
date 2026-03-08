# Fund enumerations

_Enumerations specific to the fund domain_

**Schema**: `fund/enums.schema.json`

## FundStrategy

Investment strategy of the fund

**Type**: `string`

**Values**:
- `BUYOUT`
- `GROWTH_EQUITY`
- `VENTURE_CAPITAL`
- `DISTRESSED`
- `MEZZANINE`
- `INFRASTRUCTURE`
- `REAL_ASSETS`
- `FUND_OF_FUNDS`
- `SECONDARIES`
- `CO_INVESTMENT`
- `SPECIAL_SITUATIONS`

## FundStatus

Current lifecycle status of the fund

**Type**: `string`

**Values**:
- `FUNDRAISING`
- `FIRST_CLOSE`
- `FINAL_CLOSE`
- `INVESTING`
- `HARVESTING`
- `FULLY_REALIZED`
- `LIQUIDATED`

## FundStructure

Legal structure of the fund

**Type**: `string`

**Values**:
- `LIMITED_PARTNERSHIP`
- `LLC`
- `OFFSHORE_FEEDER`
- `PARALLEL_FUND`
- `CO_INVESTMENT_VEHICLE`
- `SMA`

## FeeType

Type of fee charged by the fund

**Type**: `string`

**Values**:
- `MANAGEMENT_FEE`
- `CARRIED_INTEREST`
- `ORGANIZATIONAL_EXPENSE`
- `TRANSACTION_FEE`
- `MONITORING_FEE`
