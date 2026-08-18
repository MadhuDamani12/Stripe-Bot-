# Pending updates

Learn how to handle payment failures when updating subscriptions.

Updating a *subscription* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) generates a new *invoice* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) when:

- The subscription requires payment for the first time, such as the end of a trial period.
- The billing period changes.
- Changing the subscription causes a proration and `proration_behavior=always_invoice`.

Many subscription updates don’t generate new invoices or trigger pending updates, including:

- Configuration changes (payment methods, tax settings, retry settings)
- Billing threshold adjustments
- Setting `cancel_at_period_end` to `true`
- Adding one-time charges with `add_invoice_items`



These updates apply immediately without payment implications. For a complete list, see [What doesn’t trigger prorations](https://docs.stripe.com/billing/subscriptions/prorations.md#no-prorations).

By default, Stripe applies updates regardless of whether payment on the new invoice succeeds. If payment fails, rolling back the updates is a manual process. You need to create a new invoice, prorate items on the invoice, and then initiate payment again. However, with the pending updates feature, you can make changes to subscriptions only if payment succeeds on the new invoice.

## Before you begin

You can use pending updates if the subscription’s [collection_method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-collection_method) is `charge_automatically` and the payment method is one of the following:

- [Card](https://docs.stripe.com/payments/cards.md)
- [Link](https://docs.stripe.com/payments/link.md)
- [Alipay](https://docs.stripe.com/payments/alipay.md)
- [Amazon Pay](https://docs.stripe.com/payments/amazon-pay.md)
- [Afterpay/Clearpay](https://docs.stripe.com/payments/afterpay-clearpay.md)
- [Apple Pay](https://docs.stripe.com/apple-pay.md)
- [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay.md)
- [EPS](https://docs.stripe.com/payments/eps.md)
- [GoPay](https://docs.stripe.com/payments/gopay.md)
- [Google Pay](https://docs.stripe.com/google-pay.md)
- [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment.md)
- [Klarna](https://docs.stripe.com/payments/klarna.md)
- [KR Card](https://docs.stripe.com/payments/kr-card/accept-a-payment.md)
- [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment.md)
- [NG Card](https://docs.stripe.com/payments/ng-card/accept-a-payment.md)
- [PayPal](https://docs.stripe.com/payments/paypal.md)
- [PayTo](https://docs.stripe.com/payments/payto.md)
- [Pix](https://docs.stripe.com/payments/pix.md)
- [PromptPay](https://docs.stripe.com/payments/promptpay.md)
- [Revolut Pay](https://docs.stripe.com/payments/revolut-pay.md)
- [Satispay](https://docs.stripe.com/payments/satispay.md)
- [Stablecoins and crypto](https://docs.stripe.com/payments/stablecoin-payments.md)
- [Swish](https://docs.stripe.com/payments/swish.md)
- [TWINT](https://docs.stripe.com/payments/twint.md)
- [UPI](https://docs.stripe.com/payments/upi.md)
- [WeChat Pay](https://docs.stripe.com/payments/wechat-pay.md)

## Update the subscription [Server-side]

You can use pending updates with the [update subscription](https://docs.stripe.com/api/subscriptions/update.md), [create subscription item](https://docs.stripe.com/api/subscription_items/create.md), and [update subscription item](https://docs.stripe.com/api/subscription_items/update.md) calls. When you make the update, set `payment_behavior=pending_if_incomplete`. The example below adds a new price to a subscription. Because `proration_behavior=always_invoice`, an invoice is created and payment is attempted when the update is made.

#### curl

```bash
curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
  -u <<YOUR_SECRET_KEY>>: \
  -d "payment_behavior"="pending_if_incomplete" \
  -d "proration_behavior"="always_invoice" \
  -d "items[0][id]"="si_09IkI4u3ZypJUk5onGUZpe8O" \
  -d "items[0][price]"="price_CBb6IXqvTLXp3f"
```

If payment succeeds, the subscription is updated. If payment fails, the `Subscription` object that’s returned contains a `pending_update` hash with the changes:

```json
{
  "id": "sub_49ty4767H20z6a",
  "object": "subscription",
  "application_fee_percent": null,
  "pending_update": {
    "expires_at": 1571194285,
    "subscription_items": [
      {
        "id": "si_09IkI4u3ZypJUk5onGUZpe8O",
        "price": "price_CBb6IXqvTLXp3f"
      }
    ]
  }
}
```

## Handle failed payments [Client-side]

After making the update, check the `pending_update` hash on the subscription or listen for the `customer.subscription.updated` event in your *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests). A populated `pending_update` hash means the payment failed and your subscription update isn’t applied.

Build logic to handle payment failures due to card declines and customer authentication requests:

- For card declines, [attach a new payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method) to the customer. Then use the [pay](https://docs.stripe.com/api/invoices/pay.md) endpoint to pay the invoice that the update generates.
- For customer authentication, follow the [requires action](https://docs.stripe.com/billing/subscriptions/overview.md#requires-action) flow.

A successful payment immediately applies the changes in the `pending_update` hash and updates the invoice to `paid`.

If payment fails again, the `pending_update` hash remains on the subscription with the original [expiry date](https://docs.stripe.com/billing/subscriptions/pending-updates.md#expiration) and no changes are applied.

## Optional: Cancel or change pending updates [Server-side]

To cancel a pending update, you need to void the invoice the update created. Check the [latest invoice](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-latest_invoice) attribute on the subscription to find the invoice ID. Then use the ID to [void](https://docs.stripe.com/api/invoices/void.md) the invoice.

You can [update a subscription](https://docs.stripe.com/billing/subscriptions/pending-updates.md#update-subscription) with new values for a pending update. This updates values in the `pending_update` hash, voids the invoice associated with the previous pending update, and creates a new invoice to reflect the updated values. Successful payment of this new invoice applies the most recent updates to the subscription. Payment failure generates a new pending update with a new [expiry date](https://docs.stripe.com/billing/subscriptions/pending-updates.md#expiration) to replace the existing one.

## Supported attributes for pending updates 

Pending updates only support attributes that control proration behavior or generate new invoices.

The [update subscription](https://docs.stripe.com/api/subscriptions/update.md) endpoint supports the following attributes:

- `expand`
- `payment_behavior`
- `proration_behavior`
- `proration_date`
- `billing_cycle_anchor`
- `items`
  - `price`
  - `quantity`
- `trial_end`
- `trial_from_plan`
- `metadata`
- `discounts`
- `coupon`
- `promotion_code`
- `add_invoice_items`
- 

The [create subscription item](https://docs.stripe.com/api/subscription_items/create.md) and [update subscription item](https://docs.stripe.com/api/subscription_items/update.md) endpoints support the following attributes:

- `expand`
- `payment_behavior`
- `proration_behavior`
- `proration_date`
- `price`
- `quantity`

## Expired updates 

If you don’t take any action after an update fails, Stripe voids the invoice and discards the update after it expires.

A pending update’s `expired_at` time matches the first occurrence of either the [trial end](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-trial_end) or the earliest [items.current period end](https://docs.stripe.com/api/subscriptions/object.md##subscription_object-items-data-current_period_end). This applies if either time is within 23 hours of the update request. Otherwise, the expiration is 23 hours from the update request.

Stripe also automatically voids the invoice and removes the pending update if any of the following occurs:

- The subscription reaches a billing threshold.
- A subscription schedule linked to the subscription transitions to a new phase.

## Pending updates events 

Use [webhooks](https://docs.stripe.com/webhooks.md) to listen for the following events related to pending updates. The events are the same whether you use `Customer` objects or customer-configured `Account` objects.

| Event                                          | Purpose                                                                                                                                                                                                                 |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `customer.subscription.updated`                | Receive notifications for subscriptions, checking for the `pending_updates` hash and [resolving payment failures](https://docs.stripe.com/billing/subscriptions/pending-updates.md#handling-failed-payments) if needed. |
| `customer.subscription.pending_update_applied` | Receive notifications when pending updates are applied so that you can take further actions like upgrading, downgrading, provisioning, or deprovisioning services.                                                      |
| `customer.subscription.pending_update_expired` | Receive notifications when pending updates expire or are automatically voided, and if needed, try the update request again.                                                                                             |

## Pending updates and subscription schedules 

You can use both pending updates and [subscription schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md) to manage subscriptions. A schedule phase change discards a pending update and voids the associated invoice. Retry the update request after the phase transition if needed.

## Metered items

If a subscription includes metered items, Stripe bills any outstanding usage on the pending update invoice. However, if the pending update expires before payment, Stripe discards this usage, which prevents any subsequent invoices from billing for them.

If the pending update removes a metered price, Stripe disregards any usage reported between the pending update’s creation and the resulting invoice payment. You can’t bill for that usage. However, if `billing_mode=flexible` is on the subscription, Stripe bills for usage when removing a metered price.
