# Subscription invoices

Learn how to manage subscription invoices.

*Invoices* (Invoices are statements of amounts owed by a customer. They track the status of payments from draft through paid or otherwise finalized. Subscriptions automatically generate invoices, or you can manually create a one-off invoice) are core resources in Stripe, representing the amount a customer owes. Stripe generates an invoice for every subscription billing period. You can also manually generate invoices through the Dashboard or API for off-cycle or one-time payments. Learn more about the lifecycle for [standalone invoices](https://docs.stripe.com/invoicing/overview.md#invoice-lifecycle) and [subscription-generated invoices](https://docs.stripe.com/billing/invoices/subscription.md#sub-invoice-lifecycle).

## Subscription invoice lifecycle 

The following sections describe how Stripe handles an invoice throughout a subscription lifecycle.

### New subscription invoices 

When you create a subscription for a customer, Stripe:

- Creates an invoice.
- [Finalizes](https://docs.stripe.com/invoicing/integration/workflow-transitions.md#finalized) the invoice immediately when [collection_method](https://docs.stripe.com/api/subscriptions/create.md#create_subscription-collection_method) is set to `charge_automatically`, or [one hour](https://docs.stripe.com/billing/subscriptions/webhooks.md#successful-invoice-finalization) later when it’s set to `send_invoice`.

If the payment succeeds on a subscription’s first invoice or the invoice doesn’t require payment, the invoice transitions to [status=paid](https://docs.stripe.com/api/invoices/object.md#invoice_object-status), and the subscription becomes active.

Until the payment succeeds, the invoice [status](https://docs.stripe.com/api/invoices/object.md#invoice_object-status) remains `open` and [auto_advance](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection.md#toggle-auto-advance) remains `false`. The subscription [status](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-status) remains `incomplete`. Learn how to resolve payment failures for new subscription invoices that [require a payment method](https://docs.stripe.com/billing/subscriptions/overview.md#requires-payment-method).

In some cases, upgrading or downgrading the subscription also creates a new invoice. We turn off [auto_advance](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection.md#toggle-auto-advance) for these invoices from the outset.

> Stripe doesn’t generate an invoice when you create a `billing_mode=flexible` subscription that contains only metered items. The subscription becomes active immediately. Stripe generates an invoice at creation only if the subscription is backdated with previously accrued usage or if pending invoice items exist.

With a finalized invoice, you can’t add invoice items or make other modifications that affect the amount due. However, you can still add invoice items to the customer. The added items apply to the next invoice.

### Subscription renewal invoices 

When subscriptions renew, Stripe:

- Creates an invoice.

- Leaves the invoice in a `draft` status for about an hour.

- Attempts to finalize and pay the invoice with the default payment method.

- Changes the invoice status to `paid` if payment succeeds.

When Stripe creates an invoice, you receive an `invoice.created` event at your configured [webhook endpoint](https://docs.stripe.com/billing/subscriptions/webhooks.md). In this case, the attribute of the invoice [status](https://docs.stripe.com/api/invoices/object.md#invoice_object-status) is `draft`, which means that its invoice items are open for modification.

### Collect payment

When an invoice is due, Stripe tries to collect payment by either [automatically charging](https://docs.stripe.com/invoicing/automatic-charging.md) the [payment method](https://docs.stripe.com/payments/payment-methods/integration-options.md) on file, or [emailing the invoice](https://docs.stripe.com/invoicing/integration.md#accept-invoice-payment) to customers.

When trying to collect payment on an invoice, Stripe uses the first available payment method in this list, in this order:

| Priority | Payment method                           | API attribute                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1        | Invoice default payment method           | [invoice.default_payment_method](https://docs.stripe.com/api/invoices/object.md#invoice_object-default_payment_method)                                                                                                                                                                                                                                                                                                      |
| 2        | Subscription default payment method      | [subscription.default_payment_method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-default_payment_method)                                                                                                                                                                                                                                                                                       |
| 3        | Customer default payment method          | [customer.invoice_settings.default_payment_method](https://docs.stripe.com/api/customers/object.md#customer_object-invoice_settings-default_payment_method) (for `Customer` objects) or [configuration.customer.billing.default_payment_method](https://docs.stripe.com/api/v2/core/accounts/object.md#v2_account_object-configuration-customer-billing-default_payment_method) (for customer-configured `Account` objects) |
| 4        | (Legacy) Customer default payment source | [customer.default_source](https://docs.stripe.com/api/customers/object.md#customer_object-default_source)                                                                                                                                                                                                                                                                                                                   |

#### Retry payments

Stripe offers several options for dealing with [failed payments](https://docs.stripe.com/invoicing/automatic-collection.md), including machine-learning powered [Smart Retries](https://docs.stripe.com/invoicing/automatic-collection.md#smart-retries).

## Manage subscription invoices 

#### Dashboard

The following sections describe how to perform [basic actions on invoices](https://docs.stripe.com/invoicing/dashboard/manage-invoices.md) in the Dashboard.

### Create an invoice

Stripe automatically creates an [invoice](https://docs.stripe.com/invoicing/dashboard.md#create-invoice) for subscriptions at the end of each billing cycle. We finalize and send the invoice in one hour. Before the invoice is finalized, you can edit it. Read more about making changes in the [Invoice details page](https://docs.stripe.com/invoicing/dashboard/manage-invoices.md#invoice-details-page).

### Preview upcoming invoices 

The [Retrieve an invoice](https://docs.stripe.com/api.md#retrieve_invoice) API provides a mechanism for viewing an existing invoice. Stripe also provides an endpoint for [creating a preview invoice](https://docs.stripe.com/api/invoices/create_preview.md). This preview reflects the base price, pending invoice items, discounts, and any existing customer credit balance.

When fetching the preview, you can also model what the invoice would look like if you changed the subscription in one of these ways:

- Swapping the underlying price
- Altering the quantity
- Applying a trial period
- Adding a coupon

### Retrieve the full subscription from the invoice

By default, retrieving an invoice returns only the Subscription ID. To retrieve the full Subscription object, use the [expand](https://docs.stripe.com/api/expanding_objects.md) parameter:

- **API version 2025-03-31.basil or later**: Expand [parent.subscription_details.subscription](https://docs.stripe.com/api/invoices/object.md#invoice_object-parent-subscription_details-subscription)

  ```curl
  curl -G https://api.stripe.com/v1/invoices/in_xxxxxxx \
    -u "<<YOUR_SECRET_KEY>>:" \
    -d "expand[]=parent.subscription_details.subscription"
  ```

- **API versions before 2025-03-31.basil**: Expand [subscription](https://docs.stripe.com/api/invoices/object.md?api-version=2025-02-24.acacia#invoice_object-subscription)

  ```curl
  curl -G https://api.stripe.com/v1/invoices/in_xxxxxxx \
    -u "<<YOUR_SECRET_KEY>>:" \
    -d "expand[]=subscription"
  ```

#### API

To invoice a customer for a one-time charge such as a setup fee, create an [invoice item](https://docs.stripe.com/api.md#invoiceitems) by passing the customer ID, currency, and price:

```curl
curl https://api.stripe.com/v1/invoiceitems \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}" \
  -d "pricing[price]={{PRICE_ID}}"
```

You can now create an invoice for your customer and it adds the invoice item automatically:

```curl
curl https://api.stripe.com/v1/invoices \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "customer={{CUSTOMER_ID}}"
```

## Update the first invoice of a subscription 

How you edit the first invoice of a subscription depends on the setting for the customer’s payment method for the subscription. If unsure, you can check the payment method setting using the API or the Dashboard.

To check a subscription’s payment method using the API, check the value of [collection_method](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-collection_method) on the `Subscriptions` object for the customer. A value of `send_invoice` means Stripe emails the customer their invoice. A value of `charge_automatically` means Stripe charges the customer on your behalf using their default payment method.

To check a subscription’s payment method in the Dashboard, open the [Subscriptions page](https://dashboard.stripe.com/subscriptions). Then, click the subscription you want to check to open its detailed view. In the **Subscription details** section, the **Billing method** field value defines the payment method: **Charge default payment method** or **Send invoice**.

#### Send invoice

For customers that receive invoices, you have a one hour period after creation before Stripe finalizes the subscription. Within this timeframe you can make necessary changes to the subscription, like changing amount or line items, adding a description or metadata, and so on.

After the initial hour, you can no longer make updates. Stripe emails the invoice to the customer to collect subscription payment.

#### Charge default payment method

Stripe immediately finalizes the initial invoice and charges the customer. Consequently, there isn’t a one hour period in which you can update the initial invoice before finalization.

There are a few options available to make changes to the initial invoice:

- Create the subscription with `trial_end` set several seconds into the future. The subscription first generates a 0.00 USD invoice, and after the trial is over Stripe creates a non-zero invoice with a one hour draft period. The initial status of this subscription is `trialing` and transitions to either `active` or `past_due`, depending on the payment outcome.
- Create the subscription through a [subscription schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules.md#start-subscription-future). When the schedule starts, Stripe creates the first invoice with a one hour draft period. The initial status of this subscription is `active` and either stays `active` or transitions to `past_due`, depending on the payment outcome.

## Customize invoices 

You can customize invoices in several ways, including:

- [Add extra items to a future invoice](https://docs.stripe.com/billing/invoices/subscription.md#adding-upcoming-invoice-items)
- [Increase the frequency of invoices](https://docs.stripe.com/billing/invoices/subscription.md#pending-items-frequently)
- [Add items to a customer’s first invoice](https://docs.stripe.com/billing/invoices/subscription.md#first-invoice-extra)
- [Add items to a draft subscription invoice](https://docs.stripe.com/billing/invoices/subscription.md#adding-draft-invoice-items)
- [Generate an invoice outside of the subscription service period](https://docs.stripe.com/billing/invoices/subscription.md#generating-invoices)
- [Pause a subscription invoice for review](https://docs.stripe.com/billing/invoices/subscription.md#holding-review)
- [Issue a subscription invoice with configurable item prices](https://docs.stripe.com/billing/invoices/subscription.md#invoice-item-prices)

### Add extra invoice items to a future invoice 

You can add up to 250 invoice items to an invoice. To [add extra invoice items](https://docs.stripe.com/api/invoiceitems/create.md) to the next invoice in the cycle:

```curl
curl https://api.stripe.com/v1/invoiceitems \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d "pricing[price]=price_CBb6IXqvTLXp3f" \
  -d customer=cus_4fdAW5ftNQow1a
```

These one-off items are added to the next invoice created for this customer. To make sure this is added to a specific subscription, use the optional `subscription` parameter to apply it to that subscription.

#### Invoice pending items more frequently 

Other than [changing the billing period](https://docs.stripe.com/billing/subscriptions/billing-cycle.md), there are a few ways to invoice these items without adjusting the normal subscription service period:

- Create a [one-off invoice](https://docs.stripe.com/invoicing/dashboard.md) for the customer.

- Charge a subscription whenever the amount due reaches a [threshold](https://docs.stripe.com/billing/subscriptions/usage-based/thresholds.md).

- Use [pending_invoice_item_interval](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-pending_invoice_item_interval) to specify an interval for how often to bill for any pending invoice items. This is equivalent to having Stripe create a [one-off invoice](https://docs.stripe.com/invoicing/dashboard.md) for the subscription on a recurring basis.

### Add an extra charge on a subscription’s first invoice 

Include a one-time charge to the first subscription invoice using `add_invoice_items`:

```curl
curl https://api.stripe.com/v1/subscriptions \
  -u "<<YOUR_SECRET_KEY>>:" \
  -d customer={{CUSTOMER_ID}} \
  -d "items[0][price]={{RECURRING_PRICE_ID}}" \
  -d "add_invoice_items[0][price]={{PRICE_ID}}" \
  -d payment_behavior=default_incomplete
```

> If you’re using [Checkout](https://docs.stripe.com/payments/checkout.md) to create subscriptions, add extra charges by specifying [line_items](https://docs.stripe.com/api/checkout/sessions/create.md#create_checkout_session-line_items) with the [client and server integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md).

### Add invoice items to a draft subscription invoice 

When a subscription renews and creates an invoice, Stripe sends the `invoice.created` *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) event. Stripe [waits approximately one hour](https://docs.stripe.com/billing/subscriptions/webhooks.md#understand) before finalizing the invoice and attempting payment, or sending an email.

During that delay, the invoice is a [draft](https://docs.stripe.com/api/invoices/object.md#invoice_object-status) and is editable. You can [create invoice items](https://docs.stripe.com/api/invoiceitems/create.md) on that invoice. Make sure to provide the [invoice](https://docs.stripe.com/api/invoiceitems/create.md#create_invoiceitem-invoice) parameter when you create these invoice items. Otherwise, they’re added as pending items and are included in the next subscription period.

These invoice items behave slightly differently than invoice items automatically generated by Stripe:

- Pending invoice items are always charged when the billing period ends for any canceled subscription. Canceling a customer’s subscription prevents them from being billed again *if no invoice items exist*.

- Pending invoice items aren’t prorated when a customer’s subscription changes.

If pending invoice items remain after a subscription cancels, Stripe generates an invoice and attempts to bill the customer for them at the end of the next billing period. These invoice items are (similarly) not prorated when a subscription changes.

#### Manage pending invoice items 

You can see a customer’s pending invoice items by navigating to the [Customers page](https://dashboard.stripe.com/customers), and clicking on their name. If the customer has a pending invoice item, it appears under **Pending invoice items**. An invoice item appears as pending if it’s not attached to any invoice.

Under **Pending invoice items**, you can also choose to create a new invoice item, or instantly invoice everything listed. When you click **Invoice now**, a dialog appears that lets you select whether to charge the default source or email the invoice to the customer. Additionally, the dialog gives you the option to calculate tax automatically.

### Generate an invoice for subscription items outside the billing period 

You can invoice pending invoice items outside of the regular billing period by [generating a one-off invoice](https://docs.stripe.com/invoicing/dashboard.md). Generating a one-off invoice pulls in any pending invoice items that would have been added to the regularly scheduled invoice.

> When you manually generate an invoice, Stripe doesn’t apply the [tax rates](https://docs.stripe.com/tax/tax-rates.md) you might have established on the subscription. If taxes apply, you must explicitly [add the tax rates](https://docs.stripe.com/invoicing/taxes/tax-rates.md) to the invoice.

### Pause a subscription invoice for review 

Rather than automatically attempting payment at the end of a billing period, you can pause the invoice for review or corrections. To pause an invoice:

1. Pause automatic collection within one hour of receiving the `invoice.created` event. You can do this by setting `auto_advance=false` in the API, or by going to [Subscriptions and emails](https://dashboard.stripe.com/settings/billing/automatic) in the Dashboard. Locate the pause payment section, and click **Set up** to make changes. This feature prevents Stripe from automatically attempting payment from your customer for the invoice amount, and from emailing the invoice.

2. Review the invoice.

3. After you’re ready to charge the customer, resume automatic collection. You can this by either setting [auto_advance=true](https://docs.stripe.com/api/invoices/update.md#update_invoice-auto_advance), or by updating the pause payment options in the Dashboard.

### Issue a subscription invoice with configurable item prices 

You can issue invoices with line item prices that exclude inclusive tax. Tax-exclusive prices are only shown in the invoice PDF. That means, when using inclusive tax, the Hosted Invoice Page and invoice emails show tax-inclusive prices. You can define the settings for net prices in the Dashboard or API.

- **Include inclusive tax**—The invoice PDF displays line item prices including the inclusive tax. (This is the default.)
- **Exclude tax**—The invoice PDF displays line item prices excluding tax.

> #### Order precedence
> 
> If you set a default for line item prices at the customer level, it takes precedence over account-level settings.

## Void an invoice generated by a subscription 

### Void the first invoice of a subscription

When you void the first invoice of a subscription, Stripe applies the following logic based on the subscription status:

- If the subscription is `incomplete`, the subscription status changes to `incomplete_expired`.
- If the subscription is `past_due`, the subscription status changes to `active`.
- If the subscription is `active`, the subscription status doesn’t change.

### Void the most recent invoice of a subscription

When you void the most recent invoice for an active subscription, and the invoice isn’t the first one, Stripe applies the following logic to each invoice, starting from the most recent to the oldest, until it meets one of these conditions:

- If the invoice is in a `paid` or `uncollectible` status, the subscription status changes to `active`.
- If the [collection_method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method) is set to `charge_automatically` on the invoice and Stripe stopped dunning on the invoice because of retry limits, the subscription status changes to `canceled`, `unpaid`, or `past_due` based on your [automatic collection settings](https://dashboard.stripe.com/settings/billing/automatic).
- If the [collection_method](https://docs.stripe.com/api/invoices/object.md#invoice_object-collection_method) is set to `send_invoice`, and the invoice is past its due date, the status of the subscription changes to `past_due`.
- If the invoice isn’t in one of these statuses, the same steps execute on the next most recent invoice.

If no invoices match any of these criteria, the subscription status changes to `active`.

## Subscription metadata 

After a subscription creates an invoice, it includes the subscription’s `metadata` in the following ways:

- The invoice’s [subscription_details.metadata](https://docs.stripe.com/api/invoices/object.md#invoice_object-subscription_details-metadata) attribute always contains the subscription’s `metadata` at the time of invoice creation, even if the subscription `metadata` is later modified.
- The [metadata](https://docs.stripe.com/api/invoice/line_item.md#invoice_line_item_object-metadata) attribute of [invoice line items](https://docs.stripe.com/api/invoice-line-item/object.md) with [parent.type=“subscription_item_details”](https://docs.stripe.com/api/invoices/object.md#invoice_object-lines-data-parent-type) reflects the most recent subscription `metadata` at the time of retrieving the invoice, meaning it might differ from the `metadata` at the time of invoice creation.
- Invoice line items with [parent.type=“invoice_item_details”](https://docs.stripe.com/api/invoices/object.md#invoice_object-lines-data-parent-type) don’t contain the subscription’s `metadata`.

When you modify a subscription invoice line item’s `metadata` directly, either with the [invoice line update](https://docs.stripe.com/api/invoice-line-item/update.md) or the [bulk invoice line update](https://docs.stripe.com/invoicing/bulk-update-line-item.md) endpoint, the update request declares the invoice line item `metadata`. Any “inherited” Subscription `metadata` isn’t preserved implicitly.

[Subscription item metadata](https://docs.stripe.com/api/subscriptions/object.md#subscription_object-items-data-metadata) isn’t automatically propagated to any other Stripe objects.
