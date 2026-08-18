# Pause subscriptions

Learn how to pause subscriptions, halting both service delivery and invoice generation.

Pausing a subscription lets you temporarily suspend both service delivery and invoice generation. The ability to pause a subscription helps you support customer scenarios such as vacations, temporary non‑usage, or goodwill pauses to prevent churn.

## Pause subscription versus pause payment collection

Pausing a subscription stops both service and billing. The subscription moves to `paused` status, Stripe stops generating invoices, and your customer loses access to the subscription’s service for the duration of the pause.

If you want to keep your customer’s access to the service active but temporarily stop collecting payment, use [pause payment collection](https://docs.stripe.com/billing/subscriptions/pause-payment.md) instead.

|                              | Servicing is paused (customer loses service access) | Invoicing is paused | Payment collection is paused |
| ---------------------------- | --------------------------------------------------- | ------------------- | ---------------------------- |
| **Pause subscription**       | Yes                                                 | Yes                 | Yes                          |
| **Pause payment collection** | No                                                  | No                  | Yes                          |

To pause a subscription, it must use [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md).

The ability to pause subscriptions is useful for:

- Merchant teams that want API control over subscription lifecycle without canceling subscriptions.
- Backend engineers building retention flows or support tooling that needs a true pause state.
- Developers validating billing, entitlement revocation, and webhook handling for paused windows.

> A subscription can also move to `paused` status when a trial ends without a payment method on file. Stripe triggers this automatically and doesn’t use the Pause subscription endpoint. See [Trial end without a payment method](https://docs.stripe.com/billing/subscriptions/trials/free-trials.md#create-free-trials-without-payment).

## Pause subscriptions

You can pause subscriptions with the [API](https://docs.stripe.com/api/subscriptions/pause.md?api-version=preview) or in the [Dashboard](https://dashboard.stripe.com/subscriptions). The pause takes effect immediately. After a subscription is paused:

- The subscription status updates to `paused`.
- You get notified about the status change via the [customer.subscription.paused](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.paused), [customer.subscription.updated](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.updated), and [entitlements.active_entitlement_summary.updated](https://docs.stripe.com/api/events/types.md#event_types-entitlements.active_entitlement_summary.updated) webhooks, enabling you to de-provision service delivery accordingly.
- Invoice generation is paused for the entire pause duration, though existing subscription invoices advance without affecting the paused status.
- The [current_period_end](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-items-data-current_period_end) updates to the time when you paused the subscription.
- You can use the [bill_for](https://docs.stripe.com/api/subscriptions/pause.md?api-version=preview#pause_subscription-bill_for) parameter to control billing behavior at pause time, including creating credit prorations for unused licensed time and creating debits for metered usage in the current period. You can invoice immediately or create pending invoice items.

You can’t pause a subscription if it:

- Uses [send_invoice](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-collection_method) collection
- Uses billing mode [classic](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-billing_mode-type)
- Is in a trial period, or has an active trial offer
- Has `paused`, `incomplete`, `incomplete_expired`, or `canceled` status
- Has an attached [schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md)
- Has an attached [cadence](https://docs.stripe.com/api/v2/billing-cadences.md?api-version=preview)

Similarly, you can’t attach a schedule or cadence to a paused subscription.

If you pause a subscription that uses a coupon, the coupon retains its original validity and the pause doesn’t extend its duration.

#### Dashboard

To pause a subscription in the Dashboard:

1. On the [Subscriptions](https://dashboard.stripe.com/subscriptions) page, find the applicable subscription, click the overflow menu (⋯), and select **Pause subscription**.
2. Configure billing behavior for unused time and outstanding usage.
3. After finalizing all settings, click **Pause subscription**.

#### API

This example demonstrates how to immediately pause an active subscription:

```curl
curl https://api.stripe.com/v1/subscriptions/sub_1234567890/pause \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: preview" \
  -d type=subscription \
  -d "bill_for[unused_time_from][type]=now" \
  -d "bill_for[outstanding_usage_through][type]=now" \
  -d invoicing_behavior=pending_invoice_item
```

### Preview the invoice before pausing

Use [Create a preview invoice](https://docs.stripe.com/api/invoices/create_preview.md?api-version=preview) to see the debits or credits that would be created by pausing.

Two conditions must be true for Stripe to return a preview invoice:

- `invoicing_behavior` must be `invoice`. The default value (`pending_invoice_item`) doesn’t generate an invoice, so the endpoint returns a 404.
- The `bill_for` parameters must produce billable amounts such as unused licensed time or outstanding metered usage. If pausing would not create debits or credits, no invoice exists to preview and the endpoint returns a 404.

Stripe returns a preview invoice only. Call [Pause a subscription](https://docs.stripe.com/api/subscriptions/pause.md?api-version=preview) when you’re ready to pause.

Include `expand: ["parent.subscription_details.subscription"]` to see the projected subscription state after pausing: `status` is `paused`, `status_details` is populated, each item’s `current_period_end` is truncated to the pause time, and any pending updates are cleared. These changes don’t persist.

This example requests a preview invoice for a pause that bills unused time and metered usage at pause time:

```curl
curl https://api.stripe.com/v1/invoices/create_preview \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: preview" \
  -d subscription=sub_1234567890 \
  -d "subscription_details[pause][invoicing_behavior]=invoice" \
  -d "subscription_details[pause][bill_for][unused_time_from][type]=now" \
  -d "subscription_details[pause][bill_for][outstanding_usage_through][type]=now" \
  -d "expand[]=parent.subscription_details.subscription"
```

The customer portal reflects that a subscription is paused, but your subscribers can’t use it to pause subscriptions themselves.

### Subscription response

When you pause a subscription, the response includes a `status_details` object that provides context about the pause:

```json
{
  "id": "sub_1SrpWtRnJ89Z4rKknfSwXkBc",
  "object": "subscription",
  "status": "paused",
  "status_details": {
    "paused": {
      "subscription": {
        "type": "pause_requested"
      },
      "transitioned_at": 1749081600,
      "type": "subscription"
    }
  }
}
```

- `status_details.paused.transitioned_at`: Unix timestamp of when the subscription transitioned to `paused` status.

- `status_details.paused.subscription.type` indicates the reason the subscription paused:

| Value                              | Meaning                                           |
| ---------------------------------- | ------------------------------------------------- |
| `pause_requested`                  | You paused the subscription via the API.          |
| `trial_end_without_payment_method` | The trial ended without a payment method on file. |
| `system`                           | Stripe paused the subscription automatically.     |

## Resume subscriptions

Resume is only available on subscriptions that use [charge_automatically](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-collection_method) collection.

If resuming doesn’t generate an invoice, the subscription status updates to `active` immediately.

If Stripe generates a resumption invoice:

- Stripe finalizes the resumption invoice immediately.
- The subscription becomes `active` once the invoice is paid or marked uncollectible.
- If you void the resumption invoice, the subscription stays `paused`.

Use the optional [payment_behavior](https://docs.stripe.com/api/subscriptions/resume.md?api-version=preview#resume_subscription-payment_behavior) parameter to control how Stripe handles payment when resuming. It accepts two values: `resume_on_payment_success` (recommended) and `resume_on_payment_attempt` (default).

### Payment behavior

| Criterion                                      | `resume_on_payment_success` (Recommended)                                                                                            | `resume_on_payment_attempt` (Default)                                                             |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| Resume request attempts payment                | Yes, when the customer has a default payment method or their cash balance covers the amount due. Otherwise, Stripe returns an error. | No. Collect payment with the [Pay invoice](https://docs.stripe.com/api/invoices/pay.md) endpoint. |
| Subscription status if a payment attempt fails | `paused`                                                                                                                             | `past_due`. The subscription doesn’t automatically revert to `paused`.                            |
| Invoice payment retries after payment failure  | Yes, unless your retry settings disable it                                                                                           | No                                                                                                |
| Pending update expiration time                 | 1 year after the resume request                                                                                                      | 23 hours after the resume request                                                                 |

`resume_on_payment_success` is only available for subscriptions that use [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md).

After a subscription’s status updates to `active`:

- Invoicing resumes.
- The billing cycle anchor is optionally reset.
- You get notified about the status change via the [customer.subscription.resumed](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.resumed), [customer.subscription.updated](https://docs.stripe.com/api/events/types.md#event_types-customer.subscription.updated), and [entitlements.active_entitlement_summary.updated](https://docs.stripe.com/api/events/types.md#event_types-entitlements.active_entitlement_summary.updated) webhooks, enabling you to re-provision service delivery accordingly.

#### Dashboard

To resume a paused subscription in the Dashboard:

1. On the [Subscriptions](https://dashboard.stripe.com/subscriptions) page, find the paused subscription, click the overflow menu (⋯), and select **Resume subscription**.
2. Configure proration and billing cycle anchor settings.
3. Click **Resume subscription**.

#### API

This example demonstrates how to immediately resume a paused subscription:

```curl
curl https://api.stripe.com/v1/subscriptions/sub_1234567890/resume \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: preview" \
  -d billing_cycle_anchor=unchanged \
  -d proration_behavior=create_prorations
```

### Preview the invoice before resuming

Use [Create a preview invoice](https://docs.stripe.com/api/invoices/create_preview.md?api-version=preview) to see the resumption invoice before calling [Resume a subscription](https://docs.stripe.com/api/subscriptions/resume.md?api-version=preview). Set `subscription_details.resume_at` to `now`. Stripe returns a preview invoice only. No subscription state is modified by calling this endpoint.

This example previews a resumption invoice using the same `billing_cycle_anchor` and `proration_behavior` values you intend to pass to the resume call:

```curl
curl https://api.stripe.com/v1/invoices/create_preview \
  -u "<<YOUR_SECRET_KEY>>:" \
  -H "Stripe-Version: preview" \
  -d subscription=sub_1234567890 \
  -d "subscription_details[resume_at]=now" \
  -d "subscription_details[billing_cycle_anchor]=now" \
  -d "subscription_details[proration_behavior]=create_prorations"
```

## Identify pause and resume events

Stripe sends the following events for paused and resumed subscriptions.

| Event                                                                                                                                                                          | Description                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| [customer.subscription.paused](https://docs.stripe.com/api/events/types.md?api-version=preview#event_types-customer.subscription.paused)                                       | Emitted when a subscription pauses.                        |
| [customer.subscription.resumed](https://docs.stripe.com/api/events/types.md?api-version=preview#event_types-customer.subscription.resumed)                                     | Emitted when a subscription resumes.                       |
| [customer.subscription.updated](https://docs.stripe.com/api/events/types.md?api-version=preview#event_types-customer.subscription.updated)                                     | Emitted when a subscription pauses or resumes.             |
| [entitlements.active_entitlement_summary.updated](https://docs.stripe.com/api/events/types.md?api-version=preview#event_types-entitlements.active_entitlement_summary.updated) | Emitted when entitlements change due to a pause or resume. |

Example webhook payload for `customer.subscription.paused` (key fields shown):

```json
{
  "id": "evt_1SrpXjRnJ89Z4rKkFxe9waAz",
  "object": "event",
  ...
  "data": {
    "object": {
      "id": "sub_1SrpWtRnJ89Z4rKknfSwXkBc",
      "object": "subscription",
      ...
      "latest_invoice": "in_1SrpWtRnJ89Z4rKkzYBCF1MY",
      ...
      "status": "paused",
      ...
    }
  },
  ...
  "type": "customer.subscription.paused"
}
```

## Query paused subscriptions in Sigma

The `subscriptions` table in [Sigma](https://dashboard.stripe.com/sigma/queries) includes a `status` column and a `status_details` JSON column that you can use to identify and analyze paused subscriptions.

Use the following query to find all currently paused subscriptions along with the pause reason and when the pause occurred:

```sql
select
  id,
  customer_id,
  status,
  json_extract_scalar(status_details, '$.paused.subscription.type') as pause_reason,
  from_unixtime(cast(json_extract_scalar(status_details, '$.paused.transitioned_at') as double)) as paused_at
from subscriptions
where status = 'paused'
order by paused_at desc
```
