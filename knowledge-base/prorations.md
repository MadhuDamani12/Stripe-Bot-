# Prorations

Manage prorations for modified subscriptions.

The most complex aspect of changing existing subscriptions are prorations, where the customer is charged a percentage of a subscription’s cost to reflect partial use. This page explains how prorations work with subscriptions and how to manage prorations for your customers.

## How prorations work

For example, [upgrading or downgrading](https://docs.stripe.com/billing/subscriptions/change-price.md) a subscription can result in prorated charges. If a customer upgrades from a 10 USD monthly plan to a 20 USD option, they’re charged prorated amounts for the time spent on each option. Assuming the change occurred halfway through the billing period, the customer is billed an additional 5 USD: -5 USD for unused time on the initial price, and 10 USD for the remaining time on the new price.

Proration ensures that customers are billed accurately, but a proration can result in different payment amounts than you might expect. Negative prorations aren’t automatically refunded and positive prorations aren’t immediately billed, although you can do both manually.

You can [preview a proration](https://docs.stripe.com/billing/subscriptions/prorations.md#preview-proration) to view the amount before applying the changes. To learn more about [how credit prorations work](https://docs.stripe.com/billing/subscriptions/prorations.md#credit-prorations), read our guide.

### Prorations and discounts

All [invoice items](https://docs.stripe.com/api/invoiceitems/object.md#invoiceitem_object) that are prorations (`prorations=true`) are set to `discountable=false`. Discounts applied to an invoice containing prorations are only applied to [invoice items](https://docs.stripe.com/api/invoiceitems/object.md#invoiceitem_object-discounts) and [invoice line items](https://docs.stripe.com/api/invoice-line-item/object.md#invoice_line_item_object-discounts) that aren’t prorations. Any discounts previously applied to the subscription and affecting the amount of the proration are reflected in the proration invoice item’s amount.

Non-prorations show discount adjustments in [discount_amounts](https://docs.stripe.com/api/invoice-line-item/object.md#invoice_line_item_object-discount_amounts).

#### Discount changes and prorations 

Updating subscription-level promotion codes, coupons, or discounts by themselves doesn’t create proration invoice items. Only changes that affect billable amounts for the current billing cycle create prorations, such as:

- Changing a subscription item’s `price` or `quantity`
- Adding or removing subscription items
- Changing billing cycle anchors or proration behavior

When you make a change that creates a proration, Stripe computes the proration amounts using the subscription’s current pricing and discounting state at the time the proration is calculated. If you modify discounts as part of the same API call that also triggers prorations (for example, changing an item quantity and modifying a discount in a single update), the proration debit or credit is calculated using the modified discounts.

For example:

- **Updating only a subscription item’s metadata or applying or removing a discount:** No proration invoice items are created, and no immediate proration charges or credits appear on the upcoming invoice.
- **Updating a subscription item’s quantity and removing a discount in the same call:** Proration invoice items are created for the quantity change, and the proration amounts reflect prices after the discount change—the modified discount is used in the proration calculation.

For more information about how discounts work on subscriptions, including how `duration=once` coupons are consumed and removed from `subscription.discounts`, see [Coupons and promotion codes](https://docs.stripe.com/billing/subscriptions/coupons.md#coupon-duration).

### What triggers prorations

By default, the following scenarios result in a proration:

| Update                                                                                                                                                                                                              | Description                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Changing [items](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items)                                                                                                                     | Adding a new item or removing an existing item                   |
| Changing [price](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items-price)                                                                                                               | Changing to a price with a different base cost or billing period |
| Changing [quantity](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items-quantity)                                                                                                         | Increasing or decreasing the quantity on a subscription item     |
| Adding [trial_end](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-trial_end) or [trial_from_plan](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-trial_from_plan) | Adding a trial period to an active subscription                  |
| Changing [billing_cycle_anchor](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-billing_cycle_anchor)                                                                                       | Resetting the billing period to a new date                       |
| Setting [cancel_at](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-cancel_at)                                                                                                              | Canceling a subscription mid-period (not at period end)          |

### What doesn’t trigger prorations 

Many subscription updates don’t affect billing or generate prorations. Make these updates at any time without creating *proration* invoice items:

| Parameter                                                                                                                                                                                                                                         | Description                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Configuration and settings updates**                                                                                                                                                                                                            |                                                                                            |
| [automatic_tax](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-automatic_tax)                                                                                                                                            | Enable or disable automatic tax calculation                                                |
| [default_payment_method](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-default_payment_method)                                                                                                                          | Change the default payment method                                                          |
| [default_source](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-default_source)                                                                                                                                          | Change the default payment source                                                          |
| [payment_behavior](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-payment_behavior)                                                                                                                                      | Control payment attempt behavior                                                           |
| [collection_method](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-collection_method)                                                                                                                                    | Change between charge automatically and send invoice                                       |
| [days_until_due](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-days_until_due)                                                                                                                                          | Update payment due date for send invoice subscriptions                                     |
| [tax_filing_currency](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-tax_filing_currency)                                                                                                                                | Change the tax filing currency                                                             |
| [retry_settings](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-retry_settings)                                                                                                                                          | Modify retry behavior for failed payments                                                  |
| [trial_settings](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-trial_settings)                                                                                                                                          | Update trial end behavior settings                                                         |
| [pay_immediately](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-pay_immediately)                                                                                                                                        | Control immediate payment behavior                                                         |
| [pending_invoice_item_interval](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-pending_invoice_item_interval)                                                                                                            | Change how often pending items are invoiced                                                |
| [pause_collection](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-pause_collection)                                                                                                                                      | Pause or resume payment collection                                                         |
| [proration_date](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-proration_date)                                                                                                                                          | Set a specific proration date (doesn’t create prorations by itself)                        |
| **Metadata and descriptive fields**                                                                                                                                                                                                               |                                                                                            |
| [metadata](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-metadata) and [items.metadata](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items-metadata)                                         | Update metadata on the subscription/subscription items                                     |
| [cancellation_details](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-cancellation_details)                                                                                                                              | Add cancellation feedback and comments                                                     |
| **Updates that act as settings for future non-proration billing changes**                                                                                                                                                                         |                                                                                            |
| [discounts](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-discounts) and [items.discounts](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items-discounts)                                     | Add or update subscription-level coupons or promotion codes that apply to future invoices. |
| [billing_thresholds](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-billing_thresholds) and [items.billing_thresholds](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-items-billing_thresholds) | Update billing thresholds on subscription/subscription items                               |
| [cancel_at_period_end](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-cancel_at_period_end)                                                                                                                              | Cancel at the current period end without proration                                         |
| [add_invoice_items](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-add_invoice_items)                                                                                                                                    | Add one-time charges to the next invoice                                                   |

> These updates don’t generate proration invoice items with `proration_behavior=create_prorations` or generate invoices with proration invoice items with `proration_behavior=always_invoice` because they don’t change the billing amount for the current period.

### Manually creating your own prorations

To calculate your own prorations outside of Stripe and add them to the subscription, pass [add_invoice_items](https://docs.stripe.com/api/subscription_schedules/create.md#create_subscription_schedule-add_invoice_items) with a negative `unit_amount` (equal to the calculated proration amount) to these endpoints:

- [CreateSubscription](https://docs.stripe.com/api/subscriptions/create.md)
- [UpdateSubscription](https://docs.stripe.com/api/subscriptions/update.md)
- [CreateSubscriptionSchedule](https://docs.stripe.com/api/subscription_schedules/create.md)
- [UpdateSubscriptionSchedule](https://docs.stripe.com/api/subscription_schedules/update.md)

### When prorations are applied

Prorations only apply to charges that occur ahead of the billing period. [Usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based.md) isn’t subject to proration.

The prorated amount is calculated as soon as the API updates the subscription. The current billing period’s start and end times are used to calculate the cost of the subscription before and after the change.

### Prorations and unpaid invoices

Stripe calculates prorations based on the subscription’s status at the time of an update, assuming that any previous invoices for the subscription will eventually be paid. If a customer changes their subscription while having an unpaid invoice for the current period, they might receive a credit for unused time on the higher-priced plan, even if they haven’t paid for that time yet.

To avoid crediting for unpaid time, you can disable prorations when the subscription’s latest invoice is unpaid. When updating the subscription, set [proration_behavior](https://docs.stripe.com/api/subscriptions/update.md?update_subscription-proration_behavior=#update_subscription-proration_behavior) to `none`. Select one of the following approaches:

1. **To keep the original billing period:** Manually [create a one-off invoice](https://docs.stripe.com/api/invoices/create.md) for any new charges.
2. **To charge immediately for the new plan and reset the billing period:** Set `billing_cycle_anchor` to `now`. For more details, see [Reset the billing period to the current time](https://docs.stripe.com/billing/subscriptions/billing-cycle.md#reset-the-billing-period-to-the-current-time).

Either of these approaches can lead to double payment if the customer eventually pays the old invoice. To avoid this, [void the unpaid invoice](https://docs.stripe.com/api/invoices/void.md).

### Taxes and prorations

For information about how taxes work with prorations, see [Collect taxes for recurring payments](https://docs.stripe.com/billing/taxes/collect-taxes.md).

## Credit prorations 

Credit prorations are issued when customers downgrade their subscriptions or cancel subscription items before the end of their billing period. Stripe offers two approaches for calculating credit prorations, depending on whether you set your subscription’s [billing_mode](https://docs.stripe.com/billing/subscriptions/billing-mode/compare.md) to `classic` or `flexible`.

### Relating credit prorations to debited items 

For prorations created from subscriptions with `billing_mode=flexible`, credit proration [invoice items](https://docs.stripe.com/api/invoiceitems/object.md#invoiceitem_object) include a [proration_details](https://docs.stripe.com/api/invoiceitems/object.md#invoiceitem_object-proration_details) object. When the invoice item is a credit proration, [proration_details.credited_items](https://docs.stripe.com/api/invoiceitems/object.md#invoiceitem_object-proration_details-credited_items) identifies the debit that the credit applies to, so you can reconcile credits against the original charges.

The `credited_items` object has a `type` field:

- If `type` is `invoice_item`, the debit is still a pending invoice item. The `invoice_item` field is the ID of that debited invoice item.
- If `type` is `invoice_line_items`, the debit is one or more [invoice line items](https://docs.stripe.com/api/invoice-line-item/object.md#invoice_line_item_object) on an existing invoice. The `invoice_line_item_details` object includes the invoice ID and an `invoice_line_items` array of debited line item IDs.

A single credit can reference multiple debited invoice line items—for example, when tiered unit pricing results in several debit line items on the invoice. [Invoice items](https://docs.stripe.com/api/invoiceitems/object.md#invoiceitem_object) can represent tiered usage in a more aggregated way than the line items on a finalized invoice, so the array reflects the debits as they appear on the invoice.

### Calculation logic with no prorations

In the following scenario, you upgrade a 10 USD monthly subscription to 20 USD with the `proration_behavior` set to `none` for 10 days. There’s no previous debit to base it on. Later, you downgrade the subscription to 10 USD per month with the `proration_behavior` set to `always_invoice`.

To set up this scenario, first you [create a subscription](https://docs.stripe.com/api/subscriptions/create.md) for 10 USD per month on April 1:

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "items[0][price]=price_10_monthly"
```

The response includes the invoice that’s created for this subscription:

```json
{
  "id": "sub_123",
  "latest_invoice": {
    "id": "in_123",
    "total": 1000,
    "currency": "usd"
  }
}
```

Then, on April 11, you [upgrade the subscription](https://docs.stripe.com/billing/subscriptions/change-price.md#changing) to 20 USD per month without creating prorations:

```curl
curl https://api.stripe.com/v1/subscriptions/sub_123 \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "items[0][id]=sub_item_1" \
  -d "items[0][price]=price_20_monthly" \
  -d proration_behavior=none
```

The latest invoice remains unchanged because `proration_behavior` is `none`:

```json
{
  "id": "sub_123",
  "latest_invoice": {
    "id": "in_123"
  }
}
```

Finally, on April 21, you [downgrade the subscription](https://docs.stripe.com/billing/subscriptions/change-price.md#changing) to 10 USD per month and create prorations:

```curl
curl https://api.stripe.com/v1/subscriptions/sub_123 \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "items[0][id]=sub_item_1" \
  -d "items[0][price]=price_10_monthly" \
  -d proration_behavior=always_invoice
```

| **Classic**                                                                                                                                                                                                                                                                                                                                                                         | **Flexible**                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The `billing_mode=classic` proration calculation logic creates a credit proration based on the current price, even though the customer never paid the 20 USD monthly rate. The latest invoice credits a third of the month for 20 USD (-6.67 USD), even though the customer never paid for the `price_20_monthly` price. It also debits a third of the month for 10 USD (3.33 USD). | The calculation logic enabled with `billing_mode=flexible` creates a credit proration based on the last price billed for the subscription item. In this case, the latest invoice credits a third of a month for the 10 USD monthly price billed on April 1 (3.33 USD) and debits a third of the month for the 10 USD price (3.33 USD). The credit and debit cancel out so the invoice total is 0 USD. |
| ```json
    # billing_mode = classic
    {
      "id": "sub_123",
      "latest_invoice": {
        "id": "in_456",
        "total": -334,
        "currency": "usd"
      }
    }
  ```                                                                                                                                                                                            | ```json
    # billing_mode = flexible
    {
      "id": "sub_123",
      "latest_invoice": {
        "id": "in_456",
        "total": 0,
        "currency": "usd"
      }
    }
  ```                                                                                                                                                                                                                |

### Calculation logic for coupons applied to multiple subscription items

Stripe weights the `amount_off` coupon on the credit proration to prevent over-billing.

In the following scenario, a 5 USD coupon is unevenly allocated to a 25 USD monthly subscription for a 10 USD item and 20 USD item.

To set up this scenario, you create a subscription with multiple items and a coupon on February 1:

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "items[0][price]=price_10_monthly" \
  -d "items[1][price]=price_20_monthly" \
  -d "discounts[0][coupon]=five_dollars_off"
```

Which returns this response:

```json
{
  "id": "sub_123",
  "latest_invoice": {
    "id": "in_123",
    "total": 2500,
    "currency": "usd",
    "lines": {
      "data": [
      {
        "id": "ili_1",
        "amount": 1000,
        "price": "price_10_monthly",
        "discount_amounts": [{
          "discount": "di_a",
          "amount": 166
        }]
      },
      {
        "id": "ili_2",
        "amount": 2000,
        "price": "price_20_monthly",
        "discount_amounts": [{
          "discount": "di_a",
          "amount": 334
        }]
      }
    ]}
  }
}

```

To cancel the 10 USD monthly subscription item:

```curl
curl https://api.stripe.com/v1/subscription_items/si_10_monthly \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d proration_behavior=create_prorations
```

When a subscription item is deleted, the `billing_mode` associated with that subscription affects how the proration is calculated as follows:

| **Classic**                                                                                                                                                                                                                                            | **Flexible**                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The default behavior distributes a 5 USD coupon to each item (2.5 USD each), canceling the cheaper item (5 USD) and resulting in a refund of 2.5 USD. Stripe calculates the total with the formula `-0.5 x (10 USD price - 5 USD coupon) = -2.50 USD`. | The flexible behavior reflects the proportional discount applied to the canceled item, rather than potentially applying the full discount amount to the proration calculation. Stripe calculates the total using the formula `-0.5 x (10 USD price - 1.66 USD discount amount) = -4.17 USD`. |
| ```json
    # billing_mode = classic
    {
      "id": "sub_123",
      "latest_invoice": {
        "id": "in_456",
        "total": -250,
        "currency": "usd"
      }
    }
  ```                                                               | ```json
    # billing_mode = flexible
    {
      "id": "sub_123",
      "latest_invoice": {
        "id": "in_789",
        "total": -417,
        "currency": "usd"
      }
    }
  ```                                                                                                    |

## Preview a proration 

You can [create a preview invoice](https://docs.stripe.com/api/invoices/create_preview.md) to preview changes to a subscription. This API call doesn’t modify the subscription. Instead, it returns the upcoming *invoice* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) based only on the parameters that you pass. Changing the `price` or `quantity` both result in a proration. This example changes the `price` and sets a date for the proration.

#### Accounts v2

#### Ruby

```ruby

# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
# Find your keys at https://dashboard.stripe.com/apikeys.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')

# Set proration date to this moment:
proration_date = Time.now.to_i

subscription = client.v1.subscriptions.retrieve('sub_49ty4767H20z6a')

# See what the next invoice would look like with a price switch
# and proration set:
items = [{
  id: subscription.items.data[0].id,
  price: 'price_CBb6IXqvTLXp3f', # Switch to new price
}]

invoice = client.v1.invoices.create_preview({
  customer_account: 'acct_4fdAW5ftNQow1a',
  subscription: 'sub_49ty4767H20z6a',
  subscription_details: {
    items: items,
    proration_date: proration_date,
  }
})
```

#### Customers v1

#### Ruby

```ruby

# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
# Find your keys at https://dashboard.stripe.com/apikeys.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')

# Set proration date to this moment:
proration_date = Time.now.to_i

subscription = client.v1.subscriptions.retrieve('sub_49ty4767H20z6a')

# See what the next invoice would look like with a price switch
# and proration set:
items = [{
  id: subscription.items.data[0].id,
  price: 'price_CBb6IXqvTLXp3f', # Switch to new price
}]

invoice = client.v1.invoices.create_preview({
  customer: 'cus_4fdAW5ftNQow1a',
  subscription: 'sub_49ty4767H20z6a',
  subscription_details: {
    items: items,
    proration_date: proration_date,
  }
})
```

You can expand the example response below to see:

- The credit for unused time at the previous price on lines 36-38.
- The cost for time spent at the new price on lines 107-109.
- The new subtotal and total for the invoice on lines 276-279.

```json
{
  "id": "upcoming_in_1OujwkClCIKljWvsq5v2ICAN",
  "account_country": "US",
  "account_name": "Test account",
  "amount_due": 3627,
  "amount_paid": 0,
  "amount_remaining": 3627,
  "application_fee_amount": null,
  "attempt_count": 0,
  "attempted": false,
  "billing_reason": "upcoming",
  "charge": null,
  "collection_method": "charge_automatically",
  "created": 1599427688,
  "currency": "usd",
  "custom_fields": null,
  "customer": "cus_DGEhAXrZWrzdYs",
  "customer_address": null,
  "customer_email": "jenny.rosen@example.com",
  "customer_name": null,
  "customer_phone": null,
  "customer_shipping": null,
  "customer_tax_exempt": "none",
  "customer_tax_ids": [],
  "default_payment_method": null,
  "default_source": null,
  "default_tax_rates": [],
  "description": null,
  "discount": null,
  "discounts": [],
  "due_date": null,
  "ending_balance": 0,
  "footer": null,
  "lines": {
    "data": [
      {"amount": -166,
        "currency": "usd",
        "description": "Unused time on Silver plan after 01 Sep 2020",
        "discount_amounts": [],
        "discountable": false,
        "discounts": [],
        "id": "il_tmp1HMdV2AJVYItwOKqQi4H",
        "invoice_item": "ii_1HMdV2AJVYItwUH1Qi4H",
        "livemode": false,
        "metadata": {},
        "object": "line_item",
        "period": {
          "end": 1599427688,
          "start": 1598982148
        },
        "plan": {
          "active": true,
          "amount": 1000,
          "amount_decimal": "1000",
          "billing_scheme": "per_unit",
          "created": 1585856460,
          "currency": "usd",
          "id": "price_H1c8v1lifcd",
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "object": "plan",
          "product": "prod_c7exjJHbC4",
          "tiers": null,
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1585856460,
          "currency": "usd",
          "id": "price_c8v1liEvrf",
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "object": "price",
          "product": "prod_c7exjJHbC4",
          "recurring": {
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount": 1000,
          "unit_amount_decimal": "1000"
        },
        "proration": true,
        "quantity": 1,
        "subscription": "sub_H38lqYjDO0DSzl",
        "subscription_item": "si_H38lIMagWoFx0W",
        "tax_amounts": [],
        "tax_rates": [],
        "type": "invoiceitem"
      },
      {"amount": 541,
        "currency": "usd",
        "description": "Remaining time on Gold plan after 01 Sep 2020",
        "discount_amounts": [],
        "discountable": false,
        "discounts": [],
        "id": "il_tmp1HMdV2AJVYItwOKqDcgkmpzz",
        "invoice_item": "ii_1HMdV2AJVYItwOKqDcgkmpzz",
        "livemode": false,
        "metadata": {},
        "object": "line_item",
        "period": {
          "end": 1599427688,
          "start": 1598982148
        },
        "plan": {
          "active": true,
          "amount": 3252,
          "amount_decimal": "3252",
          "billing_scheme": "per_unit",
          "created": 1598473039,
          "currency": "usd",
          "id": "price_KV3bAJVYItwOKq16frkr",
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "object": "plan",
          "product": "prod_JfJiw2l6ke",
          "tiers": null,
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1598473039,
          "currency": "usd",
          "id": "price_KV3bAJVYItwOKq16frkr",
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "object": "price",
          "product": "prod_JfJiw2l6ke",
          "recurring": {
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount": 3252,
          "unit_amount_decimal": "3252"
        },
        "proration": true,
        "quantity": 1,
        "subscription": "sub_H38lqYjDO0DSzl",
        "subscription_item": "si_H38lIMagWoFx0W",
        "tax_amounts": [],
        "tax_rates": [],
        "type": "invoiceitem"
      },
      {
        "amount": 3252,
        "currency": "usd",
        "description": "1 \u00d7 Gold product (at $32.52 / month)",
        "discount_amounts": [],
        "discountable": true,
        "discounts": [],
        "id": "il_tmp_7fc9ba9b6aa9aa",
        "livemode": false,
        "metadata": {},
        "object": "line_item",
        "period": {
          "end": 1602019688,
          "start": 1599427688
        },
        "plan": {
          "active": true,
          "amount": 3252,
          "amount_decimal": "3252",
          "billing_scheme": "per_unit",
          "created": 1598473039,
          "currency": "usd",
          "id": "price_KV3bAJVYItwOKq16frkr",
          "interval": "month",
          "interval_count": 1,
          "livemode": false,
          "metadata": {},
          "nickname": null,
          "object": "plan",
          "product": "prod_JfJiw2l6ke",
          "tiers": null,
          "tiers_mode": null,
          "transform_usage": null,
          "trial_period_days": null,
          "usage_type": "licensed"
        },
        "price": {
          "active": true,
          "billing_scheme": "per_unit",
          "created": 1598473039,
          "currency": "usd",
          "id": "price_KV3bAJVYItwOKq16frkr",
          "livemode": false,
          "lookup_key": null,
          "metadata": {},
          "nickname": null,
          "object": "price",
          "product": "prod_JfJiw2l6ke",
          "recurring": {
            "interval": "month",
            "interval_count": 1,
            "trial_period_days": null,
            "usage_type": "licensed"
          },
          "tiers_mode": null,
          "transform_quantity": null,
          "type": "recurring",
          "unit_amount": 3252,
          "unit_amount_decimal": "3252"
        },
        "proration": false,
        "quantity": 1,
        "subscription": "sub_H38lqYjDO0DSzl",
        "subscription_item": "si_H38lIMagWoFx0W",
        "tax_amounts": [],
        "tax_rates": [],
        "type": "subscription"
      }
    ],
    "has_more": false,
    "object": "list",
    "total_count": 3,
    "url": "/v1/invoices/upcoming_in_1OujwkClCIKljWvsq5v2ICAN/lines"
  },
  "livemode": false,
  "metadata": {},
  "next_payment_attempt": 1599431288,
  "number": null,
  "object": "invoice",
  "paid": false,
  "payment_intent": null,
  "period_end": 1599427688,
  "period_start": 1596749288,
  "post_payment_credit_notes_amount": 0,
  "pre_payment_credit_notes_amount": 0,
  "receipt_number": null,
  "starting_balance": 0,
  "statement_descriptor": null,
  "status": "draft",
  "status_transitions": {
    "finalized_at": null,
    "marked_uncollectible_at": null,
    "paid_at": null,
    "voided_at": null
  },
  "subscription": "sub_8lqYjDO0DS",
  "subscription_details": {
    "proration_date": 1598982148
  },"subtotal": 3627,
  "tax": null,
  "tax_percent": null,
  "total": 3627,
  "total_discount_amounts": [],
  "total_tax_amounts": [],
  "transfer_data": null,
  "webhooks_delivered_at": null
}
```

Use this information to confirm the changes with the customer before modifying the subscription. Because Stripe prorates to the second, prorated amounts might change between the time they’re previewed and the time the update is made. To avoid this, pass in a `subscription_details.proration_date` value when creating a preview. When you update the subscription, pass the same date using the `proration_date` parameter on a subscription so that the proration is calculated at the same time.

#### Ruby

```ruby

# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
# Find your keys at https://dashboard.stripe.com/apikeys.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')

subscription = client.v1.subscriptions.update(
  'sub_49ty4767H20z6a',
  {
    items: [
      {
        id: subscription.items.data[0].id,
        price: 'price_CBb6IXqvTLXp3f',
      },
    ],
    proration_date: proration_date,
  }
)
```

## Control proration behavior

Prorating is controlled by the [proration_behavior](https://docs.stripe.com/api/subscriptions/update.md#update_subscription-proration_behavior) parameter, which has three possible parameter options: `create_prorations`, `always_invoice`, and `none`.

### Default behavior

The default parameter for `proration_behavior` is `create_prorations`, which creates proration invoice items when applicable. These proration items are only invoiced immediately under [certain conditions](https://docs.stripe.com/billing/subscriptions/change-price.md#immediate-payment).

### Create immediate prorations

To bill a customer immediately for a change to a subscription on the same billing period, set `proration_behavior` to `always_invoice` when you modify the subscription. This calculates the proration, then immediately generates an invoice.

### Disable prorations 

To disable prorations on a per-request basis, set the `proration_behavior` parameter to `none`. No parameter turns off all future prorations for a subscription. To disable prorations indefinitely, set `proration_behavior` to `none` for every request that generates prorations.

> When canceling a subscription, you can only disable the proration if the `cancel_at` date is within the current billing period. If you cancel the subscription for a date outside the current period, you can’t disable the proration.

#### curl

```bash
curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \
  -u <<YOUR_SECRET_KEY>>: \
  -d "items[0][id]"="si_1AkFf6LlRB0eXbMtRFjYiJ0J" \
  -d "items[0][price]"="price_CBb6IXqvTLXp3f" \
  -d "proration_behavior"="none"
```

When prorations are disabled, customers are billed the full amount at the new price when the next invoice is generated.
