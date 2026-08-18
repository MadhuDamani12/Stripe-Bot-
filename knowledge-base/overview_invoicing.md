# How invoicing works

Learn about the stages of the invoice lifecycle.

Invoices provide an itemized list of goods and services rendered, which includes the cost, quantity, and taxes. You can send invoices to customers to collect payment or you can create an invoice and automatically charge a customer’s saved payment method.

*Subscriptions* (A Subscription represents the product details associated with the plan that your customer subscribes to. Allows you to charge the customer on a recurring basis) automatically generate invoices for each billing cycle. Learn more about the [invoice lifecycle for subscriptions](https://docs.stripe.com/billing/invoices/subscription.md#sub-invoice-lifecycle).

When you create an invoice, you can select an existing [customer](https://docs.stripe.com/invoicing/customer.md) and [product](https://docs.stripe.com/invoicing/products-prices.md) or create and save new ones. You can also create one-time products that only exist on the current invoice.

You can use both the [Dashboard](https://docs.stripe.com/invoicing/dashboard.md) and the [API](https://docs.stripe.com/api/invoices.md) to create, edit, and manage invoices.

## Invoice lifecycle 

After they’re created manually or as part of a subscription, invoices move through a series of statuses as they’re created and processed. Stripe calls this the automatic collection workflow.

The basic lifecycle for invoices looks like this:

1. A newly created invoice has `draft` status.
2. Stripe [finalizes an invoice](https://docs.stripe.com/invoicing/integration/workflow-transitions.md#finalized) when it’s ready to be paid by changing its status to `open`. You can no longer change most details of a finalized invoice.
3. Stripe can wait for the customer to pay the invoice or automatically attempt to pay it using the customer’s default payment method.
   - If payment succeeds, Stripe updates the invoice status to `paid`.
   - If payment fails or the invoice isn’t fully paid, the invoice remains `open`.
4. Optionally, you can change the status of an unpaid invoice to `void` or `uncollectible`.
5. You can also change the status of a paid invoice back to open by [unapplying payments](https://docs.stripe.com/invoicing/apply-payments.md) from it.

You can [configure Stripe to send customer emails](https://docs.stripe.com/invoicing/send-email.md) at different stages of the invoice lifecycle, such as when it finalizes an invoice or when automatic payment fails.

## Invoice statuses 

Invoices can have one of the following statuses. The actions you can take on an invoice depend on its status.

| Status                                                                       | Description                                                                                                 | Possible actions                                                                                                                                                                                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [draft](https://docs.stripe.com/invoicing/overview.md#draft)                 | The invoice isn’t ready to use. All invoices start in `draft` status.                                       | - Edit any part of the invoice.
  - When the invoice is ready to use, finalize it by changing its status to `open`.
  - If the invoice isn’t associated with a subscription, [delete](https://docs.stripe.com/invoicing/overview.md#deleted) it.                                                                                                                                  |
| [open](https://docs.stripe.com/invoicing/overview.md#open)                   | The invoice is finalized and awaiting payment.                                                              | - Send the invoice to a customer for payment.
  - Change [only some elements of the invoice](https://docs.stripe.com/invoicing/invoice-edits.md). To make more substantive changes, create a new invoice and void the old one.
  - Change the invoice’s status to `paid`, `void`, or `uncollectible`.
  - [Edit](https://docs.stripe.com/invoicing/invoice-edits.md) the invoice. |
| [paid](https://docs.stripe.com/invoicing/overview.md#paid)                   | This invoice is paid.                                                                                       | - Change the invoice status to `open`.
  - Detach payments from invoice.                                                                                                                                                                                                                                                                                                          |
| [void](https://docs.stripe.com/invoicing/overview.md#void)                   | This invoice is canceled.                                                                                   | - No further actions.                                                                                                                                                                                                                                                                                                                                                             |
| [uncollectible](https://docs.stripe.com/invoicing/overview.md#uncollectible) | The customer is unlikely to pay the invoice. Normally, you treat it as bad debt in your accounting process. | - Change the invoice’s status to `void` or `paid`.                                                                                                                                                                                                                                                                                                                                |

### Draft invoices 

You can update almost any details of a `draft` invoice. You can also delete it, unless it’s associated with a subscription. When a `draft` invoice is ready to send for payment, you finalize it by changing its status to `open`.

You can delete a `draft` invoice. You can’t recover a deleted invoice. 

#### Dashboard

1. Go to the [Invoices page](https://dashboard.stripe.com/test/invoices).

2. Click the overflow menu (⋯) next to the invoice.

3. Click **Delete draft**.

#### API

If you delete an invoice using the API and have configured [webhook](https://docs.stripe.com/webhooks.md) endpoints, Stripe sends an `invoice.deleted` event.

```curl
curl -X DELETE https://api.stripe.com/v1/invoices/id \
  -u "<<YOUR_SECRET_KEY>>:"
```

### Open invoices 

The invoice has been finalized and still has a remaining balance. If the amount due is less than the [minimum chargeable amount](https://docs.stripe.com/currencies.md#minimum-and-maximum-charge-amounts), the invoice automatically transitions to `paid` status and Stripe debits the amount from the [customer’s credit balance](https://docs.stripe.com/billing/customer/balance.md).

In the Dashboard, invoices in `open` status can display a different badge, such as `Past due` or `Retrying`. In some scenarios, you can hover over the badge to view an explanatory tooltip.

If an open non-subscription invoice is waiting for a payment that’s initiated but still pending, it shows the `Pending` badge in the list of invoices. However, its details page shows the `Open` badge.

You can update only a few elements of an open invoice, such as the memo or metadata. To make more substantive changes, you must [revise the invoice](https://docs.stripe.com/invoicing/invoice-edits.md) by replacing it with a new one.

You can’t delete a finalized invoice. To cancel it, change its status to `void`.

### Paid invoices 

The customer has paid the invoice. This status is terminal, which means that the invoice’s status can never change.

#### Dashboard

To attempt a payment through the Dashboard, open the [Invoice details page](https://docs.stripe.com/invoicing/dashboard/manage-invoices.md#invoice-details-page) and click **Charge customer**.

#### API

The following example shows how to transition an invoice into a `paid` state by using the [Pay](https://docs.stripe.com/api/invoices/pay.md) endpoint. If you’ve configured [webhook](https://docs.stripe.com/webhooks.md) endpoints, you’ll receive an `invoice.payment_failed` or `invoice.paid` event, depending on the outcome of the payment attempt.

```curl
curl -X POST https://api.stripe.com/v1/invoices/id/pay \
  -u "<<YOUR_SECRET_KEY>>:"
```

You receive the `invoice.payment_succeeded` event only when an invoice-related PaymentIntent is created and completes successfully. Stripe sends the `invoice.paid` event when an invoice transitions to `paid`. An invoice can transition to `paid` without an associated PaymentIntent succeeding if:

- It relates to a trial or free subscription
- It has an `amount_due` covered by a [customer’s credit balance](https://docs.stripe.com/billing/customer/balance.md) or below the [minimum charge amount](https://docs.stripe.com/currencies.md#minimum-and-maximum-charge-amounts)
- It’s marked as [paid_out_of_band](https://docs.stripe.com/api/invoices/pay.md#pay_invoice-paid_out_of_band)

In these cases, you receive the `invoice.paid` event, but no `invoice.payment_succeeded` event.

#### Out of band invoices

If a customer pays an invoice out of band (outside of Stripe), you can manually change the [status](https://docs.stripe.com/invoicing/overview.md#invoice-statuses) to `paid` through the Dashboard or API.

#### Dashboard

You can manually mark an open invoice as paid in the Dashboard. On the invoice details page, click the overflow menu (⋯) and select **Change invoice status**. In the **Change invoice status** dialog, select **Paid**.

#### API

To manually mark an open invoice as paid in the API, use the [paid_out_of_band](https://docs.stripe.com/api/invoices/pay.md#pay_invoice-paid_out_of_band) parameter when you submit a request to the [Pay](https://docs.stripe.com/api/invoices/pay.md) endpoint.

### Void invoices 

Voiding an invoice is conceptually similar to deleting or canceling it. However, voiding an invoice maintains a paper trail, which allows you to look up the invoice by number. Voided invoices are treated as zero-value for reporting purposes, and aren’t payable. This status is terminal, which means that the invoice’s status can never change.

After you void an invoice, the [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page.md) is still accessible, and displays a message indicating that the invoice has been voided. You can only void an invoice in `open` or `uncollectible` status.

> Consult with local regulations to determine whether and how an invoice might be amended, canceled, or voided in the jurisdiction you’re doing business in. You might need to [issue another invoice](https://docs.stripe.com/invoicing/integration.md#create-invoice-code) or [credit note](https://docs.stripe.com/invoicing/integration/programmatic-credit-notes.md) instead. Stripe recommends that you consult with your legal counsel for advice specific to your business.

#### Dashboard

To void an invoice from the Dashboard:

1. Go to the **Invoice details** page.

2. Click the overflow menu (⋯) and select **Change invoice status**.

3. In the resulting dialog, select **Void**.

#### API

To void an invoice through the API:

```curl
curl -X POST https://api.stripe.com/v1/invoices/id/void \
  -u "<<YOUR_SECRET_KEY>>:"
```

If you’ve configured [webhook](https://docs.stripe.com/webhooks.md) endpoints, you’ll receive an `invoice.voided` event when an invoice moves into the `void` status.

### Uncollectible invoices 

Sometimes your customers can’t pay their outstanding bills. For example, assume that you provide 1,000 USD worth of services to your customer, but they’ve since declared bankruptcy and have no assets to pay the invoice.

As a result, you decide to write off the invoice as unlikely to be paid. In this case, you can update the status of the invoice to be `uncollectible`. This allows you to track the amount owed for reporting purposes as part of your bad debt accounting process.

#### Dashboard

You can mark an open invoice as uncollectible in the Dashboard. On the invoice details page, click the overflow menu (⋯) and select **Change invoice status**. In the **Change invoice status** dialog, select **Uncollectible**.

#### API

To mark an open invoice as uncollectible using the API, use the [Mark uncollectible](https://docs.stripe.com/api/invoices/mark_uncollectible.md) endpoint as shown in the following example:

```curl
curl -X POST https://api.stripe.com/v1/invoices/id/mark_uncollectible \
  -u "<<YOUR_SECRET_KEY>>:"
```

If you’ve configured [webhook](https://docs.stripe.com/webhooks.md) endpoints, you’ll receive a `invoice.marked_uncollectible` event when an invoice moves into the `uncollectible` status.

## See also

- [Use the Dashboard](https://docs.stripe.com/invoicing/dashboard.md)
- [Integrate with the API](https://docs.stripe.com/invoicing/integration.md)
- [Status transitions and finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions.md)
