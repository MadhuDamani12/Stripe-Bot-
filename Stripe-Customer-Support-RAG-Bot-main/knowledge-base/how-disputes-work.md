# How disputes work

The lifecycle of payment card disputes.

A dispute occurs when an account owner contacts their bank to contest a payment to you for a number of possible [reasons](https://docs.stripe.com/disputes/categories.md). When someone files a dispute, the process varies slightly across different *card networks* (A network that processes the transactions of a particular card brand. It might be an intermediary in front of an issuing bank as with Visa or Mastercard, or a standalone entity as with American Express), but typically follows this standard pattern:
![Dispute lifecycle diagram](https://b.stripecdn.com/docs-statics-srv/assets/lifecycle.b60ea78efb3b484b36c415a2b71887e3.png)

When an account owner disputes a charge to their payment account, Stripe:

- Notifies you of the dispute through the Stripe Dashboard, email, *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests), and the API.
- Debits the disputed amount, plus a dispute fee, from your Stripe account.
- Provides you with an explanation of the dispute and access to the account owner’s claim to their bank.
- Walks you through the process of submitting convincing evidence to counter the dispute.

Throughout this process, Stripe facilitates your case, but doesn’t have influence over the outcome, which is at the sole discretion of the account owner’s bank.

## Before the dispute 

Sometimes, Stripe alerts you to pre-dispute notifications before an actual dispute is filed. Pay attention to these notifications because:

- You might avoid a dispute entirely with proactive customer service and transaction clarification.
- Failure to respond in the pre-dispute phase can have negative implications in the formal dispute phase.

### Early fraud warnings 

Early fraud warnings (EFWs) are messages sourced from reports that *card issuers* (The entity that issued a payment card to a cardholder. This could be a bank, such as with the Visa or Mastercard network, or it could be the card network itself, such as with American Express) on the Visa, Mastercard, and JCB networks generate to flag payments they suspect might be fraudulent. These include Visa TC40 reports and Mastercard’s System to Avoid Fraud Effectively (SAFE) reports. The networks require issuers to report fraud, but that requirement doesn’t affect an issuer’s decision about whether to initiate a dispute.

As with any fraud signal, EFWs don’t require any action or response from you. You can proactively [refund the charge](https://docs.stripe.com/disputes/prevention/best-practices.md#consider-proactively-refunding-suspicious-payments) to prevent the cardholder from initiating a dispute, or you might wait and see if a fraud dispute happens. Unless the payment was covered by the [liability shift](https://docs.stripe.com/payments/3d-secure/authentication-flow.md#disputed-payments) rule, 80% of EFWs convert into a fraud dispute if you do nothing. If the payment was covered by liability shift, then you might still receive a dispute. In that case, Stripe automatically provides some evidence for you, such as data from *3D Secure* (3D Secure (3DS) provides an additional layer of authentication for credit card transactions that protects businesses from liability for fraudulent card payments).

Automatically refunding all EFWs regardless of the likelihood of escalation isn’t a good strategy. If you’re too aggressive in issuing refunds for all EFWs, you’ll inevitably refund some transactions that would never have become disputes.

All other things being equal, our analysis suggests that the optimal point for issuing a refund on early fraud warnings is on charges that are roughly less than or equal to your [dispute fee](https://docs.stripe.com/disputes/how-disputes-work.md#dispute-fees). It’s likely not worthwhile to refund EFWs on charges more than 35 percent higher than your dispute fee.

Proactively refunding a flagged payment doesn’t affect the fraud warning. The only time a refund can prevent a fraud report is when it’s processed as a reversal, which usually happens within 2 hours of the payment capture.

Although it’s called an early fraud warning, it’s possible to receive an EFW even after you receive a fraud dispute on a charge. This is generally because the systems the networks use to process EFWs are separate from the systems they use to process disputes, and the two aren’t necessarily in sync. You can listen for EFW *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) using our [API](https://docs.stripe.com/api/radar/early_fraud_warnings.md).

> #### Cases where refunding makes more sense
> 
> The main exception to the optimal refund strategy previously described is if you have reason to worry about the effect of the dispute itself on your business or account.
> 
> If any of the conditions described under the [Best practices for preventing fraud](https://docs.stripe.com/disputes/prevention/best-practices.md#consider-proactively-refunding-suspicious-payments) apply to your situation, it makes sense to more aggressively refund EFWs.

### Inquiries 

Some card networks initiate a preliminary phase before creating a formal dispute, and *chargeback* (The action taken by a cardholder's bank to debit a business's account in response to a dispute from the cardholder. The debited funds are held until the dispute is resolved). Stripe calls this preliminary phase an *inquiry* (A pre-dispute request from a card issuer, asking for information about a charge. Based on the response from the business, an inquiry might or might not escalate to a full chargeback. Inquiries are sometimes called "retrievals" or "requests for information."), though these are sometimes also called a “retrieval” or a “request for information.” American Express and Discover are the networks that most often use this phase, while Mastercard and Visa no longer use it. Mexico Domestic charges that are disputed across card brands use inquiries before creating a formal dispute. If left unanswered, some disputes might escalate to unwinnable chargebacks.

During the inquiry phase, the cardholder’s bank requests transaction clarification, often because the cardholder doesn’t recognize the transaction description. You can resolve the case without incurring a dispute fee by either:

- Providing satisfactory evidence that answers the [dispute type](https://docs.stripe.com/disputes/categories.md) for the inquiry
- Issuing a full refund.

Inquiries on partially refunded charges can still escalate to a chargeback.

> #### Unwinnable chargebacks
> 
> Failing to respond to an inquiry can signal to the issuer your implicit acceptance of the claim, resulting in an escalation to a formal, and *likely unwinnable*, chargeback. Unless you intend to accept financial liability, always respond to inquiries immediately, making every effort to amicably resolve issues with your customer during this stage.

#### Dashboard

The Dashboard payment page describes inquiries as an **inquiry** or **dispute inquiry**. In the API events summary, they’re described as a **warning** or **dispute warning** to mirror the language in the API.

#### API

In the API, the [Dispute object](https://docs.stripe.com/api/disputes/object.md#dispute_object-status) `status` relating to an inquiry is prepended with `warning`. For example:

- `needs_response`: A full chargeback that is awaiting your response to the issuer.
- `warning_needs_response`: An inquiry awaiting response.

An inquiry can have one of the following statuses.

- `warning_needs_response`: You haven’t provided evidence for this dispute yet.
- `warning_under_review`: You submitted evidence to the issuer and are awaiting their review and decision.
- `warning_closed`: The inquiry has been open for 120 days without escalation to a chargeback.

If an inquiry remains open for 120 days without escalating to a chargeback, Stripe marks it as closed in both the Dashboard and API. At this point, the card network won’t escalate it. Card networks don’t provide an explicit “win” message for inquiries.

## During the dispute 

When an account owner files a formal dispute against a payment, whether due to an escalated inquiry or for another reason, it initiates a chargeback. During this process:

- The *card network* (A network that processes the transactions of a particular card brand. It might be an intermediary in front of an issuing bank as with Visa or Mastercard, or a standalone entity as with American Express) pulls the funds for the dispute from your Stripe balance.
- These funds are held for the entire duration of the dispute.
- The disputed amount might be the full amount of the charge or a different amount.

To learn why the debited amount might differ from the original payment, see [disputed amounts](https://docs.stripe.com/disputes/how-disputes-work.md#disputed-amount).

### Receive a dispute 

The initiation of a dispute triggers several processes:

- The card network debits Stripe for your disputed payment and related dispute fees.
- Stripe in turn debits your Stripe balance for the disputed amount plus a dispute fee.
- You can’t issue a refund outside the dispute process while the dispute is open.
- Your [dispute rate](https://docs.stripe.com/disputes/measuring.md) with that card network increases.

### Dispute timing 

Card networks typically allow cardholders to initiate disputes within 120 days of the original payment, but their rules allow more time in some situations. Certain industries, such as travel or event ticketing, are prone to longer intervals between the original purchase and a dispute. Generally, when a customer pays for a future event or service (like a vacation reservation, professional services appointment, or event ticket), the dispute window starts on the event date, not the payment date.

After a chargeback is created, you have a limited time to respond to the *card issuer* (The entity that issued a payment card to a cardholder. This could be a bank, such as with the Visa or Mastercard network, or it could be the card network itself, such as with American Express): usually 7-21 days, depending on the card network.

If you submit evidence, the issuer has a limited time to evaluate it and decide the outcome: usually 60-75 days, depending on the card network.

The full dispute lifecycle, from initiation to the final decision, can take 2-3 months to complete. You can’t reliably accelerate this timeline, except by accepting the dispute in the Dashboard or API.

At the end of the dispute process, the issuer either:

- Overturns the dispute in your favor:

  - The issuer returns the debited chargeback amount to Stripe.
  - Stripe passes this amount back to you.

- Upholds the dispute in their cardholder’s favor:

  - No money moves from your perspective.
  - Stripe has already credited the issuer when they initiated the chargeback.
  - The issuer will return the funds to the cardholder at their discretion, during or after this process.

### Dispute fees 

The dispute fees for your country can be found on the Stripe [Pricing page](https://support.stripe.com/questions/june-2025-pricing-updates-for-disputes#fee-details). The fee for receiving a dispute is deducted from your account balance when a cardholder initiates a dispute. Dispute fees vary based on your business location:

- For businesses outside Mexico, the fee for receiving a dispute is non-refundable.
- For businesses in Mexico, the fee for receiving a dispute might be returned if you win or the cardholder withdraws.
- Businesses in the Single Euro Payments Area (SEPA) incur no fee for receiving a dispute on a card payment processed on the [Cartes Bancaires network](https://docs.stripe.com/payments/cartes-bancaires.md).

If you counter a dispute, a [dispute countered fee](https://support.stripe.com/questions/june-2025-pricing-updates-for-disputes#fee-details) applies, in addition to the dispute received fee. The cardholder’s bank reviews it and decides the dispute outcome. This can take up to 3 months. When Stripe receives the decision, you receive an email from us.

Stripe returns the dispute countered fee if you win the dispute. Unless otherwise stated in your Stripe contract, we never return the dispute received fee.

> The dispute countered fee doesn’t apply to businesses in Mexico and Japan.

### Respond to a dispute 

In most cases, you have the ability to challenge a disputed payment, as long as you submit strong evidence to the card issuer that invalidates the dispute claim before the deadline.

As soon as a dispute is active, the only way to overturn it’s by *submitting evidence in a response*. Even in cases where your customer claims to have [withdrawn the dispute](https://docs.stripe.com/disputes/withdrawing.md), you must respond with evidence for the dispute to be closed in your favor. Submitting evidence is what signals to the issuer that you don’t accept the dispute and want to have the funds returned to you.

See [Respond to disputes](https://docs.stripe.com/disputes/responding.md) for information on how to:

- Review the cardholder’s claim.
- Evaluate whether to accept or challenge the dispute.
- Gather appropriate evidence to respond to the dispute.
- Use the Dashboard or API to submit your response.

### Unchallengeable disputes 

You can’t challenge some types of disputes under the rules of the card network they were processed on or due to local regulations. In general, Stripe immediately closes them as lost as soon as we notify you about them, and you have no opportunity to present evidence to the issuer.

#### Dashboard

The Dashboard payment page and timeline describes these disputes as those where the card issuer doesn’t allow you to submit evidence.

#### API

The API doesn’t distinguish these from other disputes, other than by closing them as lost immediately when opened.

- [Inquiries](https://docs.stripe.com/disputes/how-disputes-work.md#inquiries) for Discover cards can turn into unchallengeable disputes if you don’t submit evidence for the inquiry.

- The Cartes Bancaires network requires a higher standard of evidence from the cardholder before allowing them to initiate a dispute, but then prohibits you from challenging the dispute. This affects only businesses in the [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) processing payments on the Cartes Bancaires network, and not businesses elsewhere charging cards *issued* by Cartes Bancaires. Learn more at [Cartes Bancaires](https://docs.stripe.com/payments/cartes-bancaires.md).

- Due to local regulations, you can’t challenge disputes submitted for Nigerian payment methods.

### Receive multiple disputes 

In extremely rare cases, you might receive more than one dispute per payment. This can happen when a customer files a new dispute with a different reason code, for a new line item in the original transaction, on multi-capture payments or simply because the issuer acquired new information about the payment allowing them to refile a dispute.

Handle each dispute the same way as any other dispute; each dispute requires you to either accept or counter the dispute. Pay special attention to the outlined amount, currency, category, and claim details before managing the dispute.

### Disputed amount 

A disputed amount might be lower or higher than the amount of the original charge. The following table outlines some of the most common reasons for this difference:

| Scenario                   | Description                                                                                                                                                                                                                                                                                                                          | Example                                                                                                                                                                                                                                                                                                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Currency conversion        | If the currency of the payment requires conversion (for example, when the currency of the seller differs from that of the buyer), the conversion rate at the time of the purchase is likely different from the rate at dispute initiation, which causes the converted dispute amount to differ from the original transaction amount. | In January, a purchase from a business based in Ireland for 100 EUR by a customer in the United States converts to a payment on the customer’s USD account of 113.74 USD. In April, the customer disputes the 113.74 USD payment, but the exchange rate has changed, so the 113.74 USD chargeback is now 107.86 EUR to the business instead of the original 100 EUR. |
| Recurring payments         | Sometimes, when an account owner disputes multiple payments within a recurring subscription plan, their bank creates a single dispute for the total amount against one of the charges. This can also happen with non-recurring payments, but is rare.                                                                                | An account owner disputes three 50 USD recurring charges, but the bank issues a dispute of 150 USD against one of the three payments.                                                                                                                                                                                                                                |
| Partial disputes           | An account owner disputes only a portion of the total transaction amount.                                                                                                                                                                                                                                                            | A purchase of multiple products contains a single damaged item, so the account owner files a dispute to be reimbursed for only that item.                                                                                                                                                                                                                            |
| Partially refunded charges | A business partially refunded a payment, but the account owner disputes the entire payment. See our [Disputes on partially refunded payments best practice](https://docs.stripe.com/disputes/best-practices.md#partial-refund-bp) for more information about submitting evidence to counter this kind of dispute.                    | An account owner contacts a business directly and the business refunds a portion of the original purchase because one of several items in the purchase is damaged. The account owner then disputes the entire purchase amount.                                                                                                                                       |

## After the decision 

After you submit your evidence, the next notification from the card issuer to both Stripe and you is the final decision. As soon as the issuer makes its decision, Stripe updates the status of the dispute to `won` or `lost`, notifying you through the Dashboard, email, and any other communication channels you configured.

This outcome is final for all parties. Neither you nor your customer can overturn a lost dispute. However, a customer can [withdraw a dispute](https://docs.stripe.com/disputes/withdrawing.md), even after a loss.

Stripe doesn’t support the arbitration phase for disputes, which means that you can’t escalate disputes to arbitrators through our platform.

> #### Late-win disputes
> 
> Although the outcome of a dispute is normally final, in rare cases the status can change from `lost` to `won`. When this occurs, Stripe labels the dispute as a `late win` and returns the funds to your balance. These late-win results happen when issuers credit or debit Stripe for a dispute outside of the regular dispute lifecycle. They might do this to handle money movement or to correct amounts or decisions. Because late wins are driven by the issuer, Stripe can’t predict when or why they happen.

## Local payment method disputes 

This dispute process applies primarily to card payments. Local payment methods (LPMs), such as Klarna and PayPal, have their own dispute processes that differ in key ways.

Each LPM defines its own rules for the following:

- **Decision-maker**: The LPM provider, such as Klarna or PayPal, decides the dispute instead of a card issuer.
- **Dispute window**: LPMs typically allow customers up to 180 days to file a dispute, compared to the 120-day window common for card payments.
- **Fee**: Fee structures vary by LPM. Some charge a single fee only when you lose a dispute, while others charge no additional fee beyond the standard Stripe dispute fee.
- **Evidence submission**: Deadlines and evidence requirements vary by LPM provider. Some LPMs include an inquiry phase where you can resolve the issue before it escalates to a formal dispute.

For details about how a specific LPM handles disputes, see the following pages:

- [Klarna disputes](https://docs.stripe.com/payments/klarna/disputes.md)
- [PayPal disputed payments](https://docs.stripe.com/payments/paypal/disputed-payments.md)
