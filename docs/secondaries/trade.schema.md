# Secondary Trade

_Secondary market trade with bids and offers_

**Schema**: `secondaries/trade.schema.json`

## Bid

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `bid_id` | `string` (uuid) | Yes |  |
| `bidder_id` | `string` (uuid) | Yes | Reference to Party |
| `bid_date` | `string` (date) | Yes |  |
| `bid_price_pct_nav` | `Percentage` | Yes | Bid as percentage of NAV (e.g., 0.92 = 92% of NAV) |
| `bid_amount` | `Money` | No | Absolute bid amount |
| `assumes_unfunded` | `boolean` | No | Whether the buyer assumes unfunded commitments |
| `conditions` | `string` | No |  |
| `status` | enum: `SUBMITTED`, `ACCEPTED`, `REJECTED`, `EXPIRED`, `WITHDRAWN` | Yes |  |

## Offer

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `offer_id` | `string` (uuid) | Yes |  |
| `seller_id` | `string` (uuid) | Yes | Reference to Party |
| `offer_date` | `string` (date) | Yes |  |
| `asking_price_pct_nav` | `Percentage` | Yes | Asking price as percentage of NAV |
| `asking_amount` | `Money` | No |  |
| `includes_unfunded` | `boolean` | No |  |
| `status` | enum: `ACTIVE`, `ACCEPTED`, `EXPIRED`, `WITHDRAWN` | Yes |  |

## SecondaryTrade

_Extends_ `../core/base.schema.json#/$defs/Auditable`

| Property | Type | Required | Description |
|----------|------|----------|-------------|
| `trade_type` | `SecondaryTradeType` | Yes |  |
| `lp_interest_id` | `string` (uuid) | Yes | Reference to LPInterest |
| `direction` | `TradeDirection` | No |  |
| `buyer_id` | `string` (uuid) | Yes | Reference to Party |
| `seller_id` | `string` (uuid) | Yes | Reference to Party |
| `broker_id` | `string` (uuid) | No | Reference to Party (intermediary) |
| `agreed_price_pct_nav` | `Percentage` | No |  |
| `agreed_amount` | `Money` | No |  |
| `unfunded_assumed` | `Money` | No | Amount of unfunded commitments assumed by buyer |
| `trade_date` | `string` (date) | Yes |  |
| `expected_close_date` | `string` (date) | No |  |
| `bids` | array of `Bid` | No |  |
| `offers` | array of `Offer` | No |  |
