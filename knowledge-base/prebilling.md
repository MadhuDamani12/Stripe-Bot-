# Bill customers in advance

Use prebilling to collect payment now for multiple future service periods.

## Start here: Install agent skills

Stripe recommends using official skills to integrate with the API using best practices. Follow the instructions below to learn how.

**Tip: Use curl instead of Fetch tools.** Skills are detailed 10–20 KB markdown files. Fetch tools summarize them. `curl -sL` guarantees the full content.

**Using `npx skills`**: Check if `npx` is installed on the system. If `npx` is available, run `npx skills add https://docs.stripe.com --list` to list available skills, then run `npx skills add https://docs.stripe.com --yes --skill <skill-name> <--skill other-skills>` to install individual skills.

**If `npx skills` isn’t available**: You can use curl to fetch the index of available skills, what they do, and their files from `https://docs.stripe.com/.well-known/skills/index.json`. To download a skill and its related files, use curl to download them from `https://docs.stripe.com/.well-known/skills/<filepath>`.

For this article, we recommend using these skills: `stripe-best-practices`

With prebilling, you can bill customers in advance for multiple service periods. You can enable prebilling when you create a subscription or add it to an existing one.

> #### Flexible billing mode required
> 
> Prebilling requires subscriptions with [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md) enabled. If you haven’t enabled flexible billing mode yet, see [Flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md) to get started.

## Use cases

With prebilling, you can collect payment upfront for future service periods. Common use cases include:

| Use case                              | Description                                                                                                                                                               |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Prepay multiple months at signup**  | Charge a monthly subscriber upfront for 3 months when they sign up, then resume normal monthly billing from that point.                                                   |
| **Early renewal billing**             | When a renewal is 7 days away, generate and send the customer the renewal invoice now instead of waiting for the end of the billing cycle.                                |
| **Annual payment on a monthly price** | Let a customer pay for 12 months of a monthly plan in one upfront invoice, without changing the underlying price to an annual interval.                                   |
| **Item-level prebilling**             | Prebill for a specific add-on item while billing other items on the same subscription at their normal monthly cadence.                                                    |
| **Early cancellation fee**            | Charge a customer for the remaining term of a committed contract when they cancel early by prebilling through the end of the commitment, then canceling the subscription. |

### Limitations 

Prebilling has the following limitations:

- You can’t use prebilling with [subscription schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md) or subscriptions backed by a subscription schedule.
- You can only use coupons with [percent_off](https://docs.stripe.com/api/coupons/object.md#coupon_object-percent_off) and a [duration](https://docs.stripe.com/api/coupons/object.md#coupon_object-duration) of `once` or `forever` with prebilling.
- You can’t enable prebilling if all the subscription items have usage-based prices. Prebilling doesn’t apply to any usage-based prices in a subscription. You can’t set [applies_to[price]](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_schedules-applies_to) if the price has [usage_type=metered](https://docs.stripe.com/api/prices/object.md#price_object-recurring-usage_type).
- If a subscription is scheduled for cancellation, you can’t set the prebilling end date past the scheduled cancellation date.

## How prebilling works 

Prebilling uses [billing_schedules](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-billing_schedules) on a subscription to define which items to bill upfront and for how long. When you configure `billing_schedules`, Stripe generates an advance invoice that covers all specified future service periods at the time the subscription is created or updated, rather than waiting for each billing cycle to occur.

Prebilling applies at the [item](https://docs.stripe.com/api/subscription_items.md) level: you can prebill specific items by passing the `applies_to` parameter with the price IDs to target, or omit `applies_to` entirely to prebill all applicable licensed-price items on the subscription. Usage-based prices are never included in prebilling, regardless of the `applies_to` configuration.

The [bill_until](https://docs.stripe.com/api/subscriptions/update.md?api-version=preview#update_subscription-billing_schedules-bill_until) parameter controls the end date of the prebilled period. You can express this as a `duration` (for example, 2 months from the current date) or as a `timestamp` (a specific Unix timestamp).

## Create a subscription with prebilling 

To configure prebilling when creating a subscription, use [billing_schedules](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-billing_schedules) to specify which items to prebill and how long to prebill for.

- Use `applies_to` to specify which items to prebill by price ID. Omit this parameter to prebill all applicable items.
- Use `bill_until` to set the end date for prebilling as a duration or timestamp.
- Use `proration_behavior` to control when the prebilling invoice is generated.

When you set the end date for prebilling:

- The end date must fall on or after the end of the first billing period. For example, for a monthly subscription, the end date must be at least one month from the start of the billing period.
- The total prebilled cycles across all items can’t exceed 50. For example, with two items you could prebill each for up to 25 months.
- The end date can’t be more than 5 years from now.

#### Dashboard

To create a subscription with prebilling in the Dashboard:

1. Go to the [Subscriptions page](https://dashboard.stripe.com/subscriptions?status=active).
2. Click **+ Create subscription**.
3. In the **Subscription settings** section, enable **Bill upfront**.
4. Select the end date for prebilling. All items in the subscription are prebilled until the date you select.
5. In the **Advanced settings** section, set **Billing mode** to **Flexible**.
6. Click **Create subscription**.

To update an existing subscription:

> The subscription must already be in `billing_mode=flexible` to enable prebilling. See [Limitations](https://docs.stripe.com/billing/subscriptions/prebilling.md#limitations) for more details.

1. Go to the [Subscriptions page](https://dashboard.stripe.com/subscriptions?status=active).
2. Click the subscription to update, then select **Actions** > **Update subscription**.
3. In the **Subscription settings** section, enable **Bill upfront**.
4. Select the end date for prebilling. All items in the subscription are prebilled until the date you select.
5. Click **Update subscription**.

#### API

### Prebill a specific item 

To prebill for a specific price on a subscription, pass an `applies_to` array with the price ID you want to prebill:

#### Accounts v2

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  --data-urlencode "items[1][price]={{PRICE_1, PRICE_2}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][applies_to][0][type]=price" \
  -d "billing_schedules[0][applies_to][0][price]={{PRICE_ID}}" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

#### Customer v1

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][applies_to][0][type]=price" \
  -d "billing_schedules[0][applies_to][0][price]={{PRICE_ID}}" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

### Prebill multiple items 

To prebill for multiple items, add multiple objects to the `applies_to` array:

#### Accounts v2

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][applies_to][0][type]=price" \
  -d "billing_schedules[0][applies_to][0][price]={{PRICE_ID}}" \
  -d "billing_schedules[0][applies_to][1][type]=price" \
  -d "billing_schedules[0][applies_to][1][price]={{PRICE_ID}}" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

#### Customer v1

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][applies_to][0][type]=price" \
  -d "billing_schedules[0][applies_to][0][price]={{PRICE_ID}}" \
  -d "billing_schedules[0][applies_to][1][type]=price" \
  -d "billing_schedules[0][applies_to][1][price]={{PRICE_ID}}" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

### Prebill all items 

To prebill for all applicable items, omit the `applies_to` array. Prebilling applies to all items on the subscription with a licensed price that cycle at least once before the prebilling end date.

#### Accounts v2

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

#### Customer v1

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

### Prebill for a duration 

To prebill for a specified duration from the current date, set `type` to `duration` and set `interval` and `interval_count`. For example, to prebill for 2 months, set `interval` to `month` and `interval_count` to `2`.

#### Accounts v2

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

#### Customer v1

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

### Prebill until a timestamp 

To prebill up to a specific date, set `type` to `timestamp` and set `timestamp` to the Unix timestamp when prebilling should end.

#### Accounts v2

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][bill_until][type]=timestamp" \
  -d "billing_schedules[0][bill_until][timestamp]=1679609767"
```

#### Customer v1

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d "billing_schedules[0][bill_until][type]=timestamp" \
  -d "billing_schedules[0][bill_until][timestamp]=1679609767"
```

### Generate the invoice immediately 

To generate the prebilling invoice immediately when you create or update the subscription, set `proration_behavior` to `always_invoice`:

#### Accounts v2

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d proration_behavior=always_invoice \
  -d "billing_schedules[0][bill_until][type]=timestamp" \
  -d "billing_schedules[0][bill_until][timestamp]=1679609767"
```

#### Customer v1

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d proration_behavior=always_invoice \
  -d "billing_schedules[0][bill_until][type]=timestamp" \
  -d "billing_schedules[0][bill_until][timestamp]=1679609767"
```

### Generate the invoice at the next billing cycle 

To generate the prebilling invoice at the next natural billing cycle date, set `proration_behavior` to `create_prorations`:

#### Accounts v2

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer_account={{CUSTOMERACCOUNT_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d proration_behavior=create_prorations \
  -d "billing_schedules[0][bill_until][type]=timestamp" \
  -d "billing_schedules[0][bill_until][timestamp]=1679609767"
```

#### Customer v1

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "items[0][price]={{PRICE_ID}}" \
  -d "items[1][price]={{PRICE_ID}}" \
  -d "billing_mode[type]=flexible" \
  -d proration_behavior=create_prorations \
  -d "billing_schedules[0][bill_until][type]=timestamp" \
  -d "billing_schedules[0][bill_until][timestamp]=1679609767"
```

## Update an existing subscription with prebilling 

To add prebilling to an existing subscription, update the subscription with the `billing_schedules` parameter. The subscription must already be in `billing_mode=flexible`.

```curl
curl https://api.stripe.com/v1/subscriptions/{{SUBSCRIPTION_ID}} \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "billing_schedules[0][bill_until][type]=duration" \
  -d "billing_schedules[0][bill_until][duration][interval]=month" \
  -d "billing_schedules[0][bill_until][duration][interval_count]=2"
```

## Early cancellation fees 

Use prebilling to charge customers for the remaining term of a committed contract when they cancel early. This is common for fixed-term subscriptions that bill on a recurring (for example, monthly) cadence.

For example, a customer signs up on January 1 for a 1-year monthly plan at 10 USD/month. They cancel on September 10. To collect the remaining commitment, prebill the subscription through December on the final invoice, then cancel the subscription with no proration.

1. [Update the subscription](https://docs.stripe.com/api/subscriptions/update.md) to set `billing_schedules.bill_until` to the end of the committed term (December 31).
2. [Cancel the subscription](https://docs.stripe.com/api/subscriptions/cancel.md) with `proration_behavior` set to `none`.

The customer’s final invoice includes charges for October, November, and December, which covers the remainder of their commitment as an early cancellation fee.

This pattern also works for longer committed contracts (for example, a 2-year contract where the customer cancels at month 18) and for early renewal scenarios where customers upgrade mid-term and prepay the remaining period at the new price.

## Additional considerations 

### Invoice generation timing 

The prebilling invoice is generated when you create or update a subscription with `billing_schedules` configured. The exact timing depends on your `proration_behavior` setting:

- `always_invoice`: Generates and finalizes the prebilling invoice immediately when the subscription is created or updated.
- `create_prorations`: Generates the prebilling invoice at the next natural billing cycle date.

Use `always_invoice` if you want the customer to receive the advance invoice right away. Use `create_prorations` if you want the invoice to appear alongside the customer’s regular invoice at their next billing date.

### Webhooks and events 

Prebilling generates invoices outside the normal billing cycle. Make sure your integration handles the relevant events. For example, you might want to send the customer a receipt when the prebilling invoice is paid, or handle payment failure with a retry flow.

| Event                           | Description                                                                         | Use case                                                                           |
| ------------------------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `invoice.created`               | Sent when Stripe generates the prebilling invoice.                                  | Record the advance charge in your system.                                          |
| `invoice.finalized`             | Sent when the invoice is finalized and ready for payment.                           | Trigger customer notification workflows.                                           |
| `invoice.payment_succeeded`     | Sent when payment on the prebilling invoice succeeds.                               | Grant the customer access to the prepaid service periods.                          |
| `invoice.payment_failed`        | Sent when payment on the prebilling invoice fails.                                  | Handle payment failure: retry logic, customer notification, or subscription pause. |
| `customer.subscription.updated` | Sent when the subscription is updated with a new `billing_schedules` configuration. | Sync the updated subscription state to your system.                                |

### Preview the prebilling invoice 

You can preview a customer’s invoice before you create or update a subscription to use prebilling. Use the API to [create a preview invoice](https://docs.stripe.com/api/invoices/create_preview.md) and include [billing_schedules](https://docs.stripe.com/api/invoices/create_preview.md#create_create_preview-subscription_details-billing_schedules) in the `subscription_details` parameter. This shows you the invoice generated for prebilling.

### Interaction with coupons 

Only coupons with `percent_off` and a `duration` of `once` or `forever` are compatible with prebilling. `amount_off` coupons and coupons with `duration=repeating` return an error when used with a subscription that has `billing_schedules` configured.

## See also

- [Flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode.md)
- [Prorations](https://docs.stripe.com/billing/subscriptions/prorations.md)
- [Preview invoices](https://docs.stripe.com/api/invoices/create_preview.md)
- [Subscription billing cycle](https://docs.stripe.com/billing/subscriptions/billing-cycle.md)
