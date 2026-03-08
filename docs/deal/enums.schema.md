# Deal enumerations

_Enumerations for deal management_

**Schema**: `deal/enums.schema.json`

## DealStage

**Type**: `string`

**Values**:
- `SOURCING`
- `SCREENING`
- `DUE_DILIGENCE`
- `IC_REVIEW`
- `TERM_SHEET`
- `DOCUMENTATION`
- `CLOSING`
- `ACTIVE`
- `MONITORING`
- `EXIT`
- `CLOSED`
- `PASSED`

## DealRole

**Type**: `string`

**Values**:
- `LEAD`
- `CO_LEAD`
- `CO_INVESTOR`
- `SYNDICATE_MEMBER`
- `ADVISOR`
- `ARRANGER`
- `AGENT`

## AssetClass

**Type**: `string`

**Values**:
- `PRIVATE_EQUITY`
- `VENTURE_CAPITAL`
- `PRIVATE_CREDIT`
- `REAL_ESTATE`
- `INFRASTRUCTURE`
- `NATURAL_RESOURCES`
- `SECONDARIES`

## DealAssetType

Discriminator for DealAsset to indicate the referenced domain entity

**Type**: `string`

**Values**:
- `FACILITY`
- `INVESTMENT`
- `PROPERTY`
- `LP_INTEREST`
