# Payout Trace IDs

Track late or missing payouts with your bank.

The Trace ID is a unique identifier for a payout that our banking partners create to help you track [missing or delayed payouts](https://support.stripe.com/questions/where-is-my-payout-faq-for-late-and-missing-payouts). If you don’t see an expected payout in your bank account after 10 business days, contact your bank for an update and provide the Trace ID. You can find the Trace ID in the [Stripe Dashboard](https://dashboard.stripe.com/test/payouts), using the [API](https://docs.stripe.com/api/payouts/retrieve.md), with [Sigma](https://docs.stripe.com/data.md), or in the [Payout Reconciliation Report](https://docs.stripe.com/reports/payout-reconciliation.md).

For Connect users, you can provide your connected accounts their payout Trace IDs by accessing them using the [Stripe API](https://docs.stripe.com/api/payouts/retrieve.md). Connected accounts can then self-service their late or missing payouts.

> #### Trace ID format
> 
> Each bank determines the format of its own Trace IDs, so they can vary between payouts.

## Availability

Trace IDs are retrieved from the partner bank up to 10 days after a payout has been marked as paid. A Trace ID might not be available within this timeframe, in which case the Trace ID status is marked as pending. If a Trace ID can’t be retrieved after 10 days, the Trace ID is marked as unsupported.

## Retrieve a Trace ID

You can access a payout’s Trace ID by looking at the payout in your Dashboard or using the API.

#### Dashboard

To access the Trace ID in the Dashboard, go to your [payouts](https://dashboard.stripe.com/test/payouts) and click the payout that you want to investigate. The Trace ID appears in the **Details** section. If the Trace ID isn’t available, it displays **Unsupported**.

#### API

The `Payout` object’s [trace_id](https://docs.stripe.com/api/payouts/object.md#payout_object-trace_id) hash contains both a `value` string and a `status`. The `status` can have one of the following values:

| Status        | Description                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------- |
| `pending`     | The payout is marked as paid, but Stripe hasn’t yet received the Trace ID. The Trace ID `value` is null.        |
| `supported`   | The banking partner has provided the Trace ID, which is stored in `value`.                                      |
| `unsupported` | Either the payout country doesn’t support Trace IDs, or Stripe couldn’t obtain the Trace ID for another reason. |

This example shows how to retrieve the Trace ID using the Payouts API:

```curl
curl https://api.stripe.com/v1/payouts/po_xxx \
  -u "<<YOUR_SECRET_KEY>>:"
```

Example response:

```json
{
  "object": "list",
  "data": [
    {
      "id": "po_xxx",
      "trace_id": {
        "status": "supported",
        "value": "7UF6L35ME6bh3bk3cj51L7o93ky79X5Pb58i5LO1e"
      }
      ...
    }
  ]
}
```

## Sigma

You can also access the Trace ID using Sigma. The following example query uses the transfers table to retrieve Trace ID information for the three most recent payouts:

#### SQL

```sql
select
  date_format(created, '%m/%d/%Y') as day,
  id,
  trace_id_status,
  trace_id
from transfers
order by day desc
limit 3
```

| `day`    | `id`                        | `trace_id_status` | `trace_id`                |
| -------- | --------------------------- | ----------------- | ------------------------- |
| 9/9/2024 | po_orWziM4j7CiRL8J4vQmXgW2w | pending           | null                      |
| 9/8/2024 | po_orWziM4j7CiRL8J4vQmXgW2w | supported         | orWziM4j7CiRL8J4vQmXgW2w5 |
| 9/6/2024 | po_orWziM4j7CiRL8J4vQmXgW2w | unsupported       | null                      |

## Support

Trace IDs are available in all Stripe-supported countries except the following payout destinations:

- Argentina
- Bolivia
- Chile
- Colombia
- Egypt
- Japan
- Philippines
- UK (Instant Payouts)
