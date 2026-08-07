# Dispute evidence best practices

Learn how to format the most convincing evidence to challenge a dispute.

You can manage disputes using the [Dashboard](https://docs.stripe.com/disputes/responding.md) or the [API](https://docs.stripe.com/disputes/api.md).

When an account owner disputes a payment with their bank, they must provide evidence to support their claim. In many cases, the bank’s goal is to protect their customer from having to pay for something they didn’t authorize or feel was misrepresented or damaged.

As the seller, you have the right to counter the account owner’s claim and provide evidence that supports your case. While Stripe doesn’t influence the ultimate outcome of the bank’s decision, our goal is to help you defend the dispute. We base the best practices that we provide here on our deep exposure to dispute resolution.

## Organize the evidence 

Before you submit evidence to counter a dispute, abide by the following guidelines:

- **Present chronologically:** Organize evidence in the order events occurred to create a clear timeline of the transaction and subsequent communications.

- **Group by type:** Separate receipts, communications, policies, and system logs into distinct sections for easier reference.

- **Include summaries:** Provide brief explanations of what each piece of evidence demonstrates to guide the reviewer.

- **Maintain clarity:** Ensure all of the text is readable and that images are clear, with sufficient contrast and resolution.

## Likelihood of winning disputes

Your chances of overturning a dispute vary significantly based on several factors, including:

- The type of dispute and whether it qualifies for [Visa CE 3.0](https://docs.stripe.com/disputes/best-practices.md#visa-ce-30) evidence.
- The strength of the evidence you submit.
- The type of payment (debit, credit, digital wallet, and so on).
- The type of purchase (online, in-person, physical product, service, and so on).

Stripe’s [Radar for Fraud Teams](https://stripe.com/radar/fraud-teams) uses Radar’s AI models to estimate your chances of winning a dispute. It gives you a prediction score in the dispute details page of your Dashboard, so you can prioritize disputes.

If you’re enrolled in Radar, but don’t see a win likelihood prediction next to a dispute, it’s likely one of the following reasons:

- The payment wasn’t made with a credit card.
- The payment has only received an [inquiry](https://docs.stripe.com/disputes/how-disputes-work.md#inquiries), not an actual dispute.
- An error prevented us from generating a prediction (this is rare).

The prediction score ranks your likelihood of winning a dispute that you’ve submitted relevant evidence for from lowest (one dot) to highest (five dots). The following table shows the expected win percentage for each ranking. Even in the most favorable cases, it’s very difficult to overturn a disputed payment.

| Dispute Win Likelihood Ranking | Chance of Winning the Dispute |
| ------------------------------ | ----------------------------- |
| 5 dots                         | 60%                           |
| 4 dots                         | 40%                           |
| 3 dots                         | 25%                           |
| 2 dots                         | 15%                           |
| 1 dot                          | 5%                            |

## Keep your evidence relevant to the dispute reason and to the point

Card issuers review thousands of dispute responses every day. Writing a long explanation to them isn’t going to make your responses more convincing. Similarly, providing evidence about your clearly stated return policy isn’t relevant for a dispute claiming that the customer never received the product. Instead, describe clearly and concisely why the claim is unreasonable and how your evidence proves that, using a neutral and professional tone. For example:

> Jenny Rosen purchased [product] from our company on [date] using a Visa credit card. We shipped the product on [date] to the address provided by the customer, and it was delivered on [date], as shown in the tracking file provided, so the claim that the product wasn’t received isn’t true.

You can investigate the dispute while collecting evidence. For example, you can review Google Maps and Street View to see where your delivery took place, or check social media to help establish the customer as the legitimate cardholder.

Many businesses also include email correspondence or texts with their customer, but be aware that these exchanges don’t verify identity. If you include them, only include the relevant excerpts. For example, if you include a long email thread, redact any duplicated copy in the chain.

Keep your evidence factual, professional, and concise. Providing too little evidence is a problem, but overwhelming the card issuer with unnecessary content can obscure your argument.

## Limit evidence file length 

Card issuers manually review thousands of dispute responses daily and won’t comb through lengthy files to find the relevant argument for the network reason code.

For example, if the dispute network reason code indicates “Canceled Merchandise”, but the customer didn’t comply with your cancellation policy, don’t submit your entire Terms and Conditions agreement. Upload only the relevant cancellation policy section and use a callout or arrow to emphasize the details your customer violated.
![Comparison of good and bad evidence file examples](https://b.stripecdn.com/docs-statics-srv/assets/best-practice-file-length.7874dbd14cb83e4b4b17eed38e6a4221.png)

- **Do:**
  - Paste relevant excerpts from your terms into a single doc.
  - Outline or underline text specific to the dispute type.
- **Don’t:**
  - Upload your entire terms of service.
  - Provide links to your terms of service or other relevant content on separate drives or websites.

You can also decrease file size by:

- Reducing font size
- Single spacing documents
- Shrinking images within PDFs

The following information is essential for file types:

| Evidence type                                 | Relevant data                            |
| --------------------------------------------- | ---------------------------------------- |
| Receipt                                       | Date, currency, amount of disputed items |
| Shipping documentation                        | Delivery date and full shipping address  |
| Cancellation policy or other Terms of service | Relevant subsections only                |
| Customer communication                        | Customer name and relevant message       |

## Include proof of customer authorization

Fraudulent disputes account for over half of all disputes. It’s important to prove the legitimate cardholder was aware of and authorized the transaction in such cases. Any data that shows proof of this is a standard part of a compelling response, such as:

- AVS (Address Verification System) matches
- CVC (Card Verification Code) confirmations
- Signed receipts or contracts
- IP address that matches the cardholder’s verified billing address

Stripe always includes any AVS or CVC results along with the purchase IP address (if available from your Stripe integration). But if you have any other evidence of authorization (for example, 3DS authentication) include it too.

## Include proof of service or delivery

After fraudulent disputes, other high frequency dispute [reasons](https://docs.stripe.com/disputes/categories.md) include claims from cardholders that products or services:

- Weren’t delivered
- Were defective or unsatisfactory
- Weren’t as described

Provide proof of service or delivery to refute such claims.

For a merchandise purchase, provide proof of shipment and delivery that includes the full delivery address, not just the city and postal code verification.

If your customer provides a “Ship to” name that differs from their own (for example, a gift purchase), be prepared to provide documentation explaining why they’re different. While it’s common practice to purchase and ship to an address that doesn’t match the verified billing address for the card, this is an additional dispute risk.

If your business provides digital goods, include evidence such as an IP address or system log proving the customer downloaded the content or used your software or service.

## Include a copy of your terms of service and refund policy

When it comes to disputes, fine print matters. For returns or refunds, it’s critical to provide proof that your customer agreed to and understood your terms of service at checkout, or didn’t follow your policies. Include a clean screenshot of how you present your terms of service during checkout, with the relevant policy clearly emphasized.

Don’t, however, include the text of your entire policy, because card issuers won’t read through it all to find the relevant copy.

## Combine files of the same evidence type

You must specify an evidence type for each file you upload, and you can only submit one piece of evidence per type. For example, you can combine several items representing communication with your customer (email messages, text screenshots, phone transcripts, and so on) into a single file for the `Customer communication` evidence. This also decreases your overall file length.

## Formatting documents and images to upload 

Include large, clear images for review. Whether you upload files through the Dashboard or the API, both have limitations on the acceptable file types and the combined file size.

- Only PDF, JPEG, or PNG file types are accepted
- The combined file size can’t be more than 4.5MB
- The combined page count must be less than 50 pages
- You can compress your files with tools such as [Smallpdf](https://smallpdf.com/)

When submitting documents or images as evidence, use the following recommendations to make sure they can remain legible:

- Use a 12 point font or larger
- Make sure that documents are US Letter or A4 size, in portrait orientation (you can still add screenshots to your documents in landscape orientation)
- Use bold text, callouts, or arrows to draw attention to pertinent information
- Avoid using color highlighting

When uploading screenshots:

- Crop the screenshot to the area of interest and circle any key components (for example, delivery confirmation or signature)
- Use the text fields in the dispute evidence form to describe what the image contains and how it supports your response

The card issuer won’t review a response containing any illegible text or data.

## Accepting disputes

You can accept a dispute, effectively agreeing that the cardholder’s reason for the dispute is valid. It isn’t considered an admission of wrongdoing and doesn’t affect your dispute fee, so it can be the best option unless you want to retrieve the disputed funds.

Take this action if you don’t intend to respond and submit evidence. Although accepting disputes doesn’t negatively affect your business any further, it’s not a viable alternative to an effective refund or returns policy. Dispute activity is calculated based on the disputes received, not won or lost, so dispute prevention is critical.

> Disputes incur a dispute fee that still applies if you accept the dispute.

## Misunderstandings

For disputes that are the result of a misunderstanding, your customer can tell their card issuer that they [no longer dispute the transaction](https://docs.stripe.com/disputes/withdrawing.md). We recommend you still submit evidence to show that the payment was valid and to make sure the card issuer knows you’re not accepting the dispute.

In cases where you agree that the customer should keep the disputed funds, accept the dispute rather than ask the cardholder to withdraw the dispute for a regular refund. Remember, the card networks don’t consider how many disputes you win or lose, only how many you receive—a withdrawn dispute still counts as a dispute.

## Disputes on partially refunded payments 

While uncommon, a customer can dispute a payment for the full amount even if they’ve already received a partial refund (for example, a refund of a smaller amount that has been agreed upon). We understand this is frustrating as it amounts to an over-refund of more than the original purchase. Always respond in such cases because card issuers are very willing to rectify this situation.

> Because merchants can’t contest Cartes Bancaires disputes, you can’t ask the issuer to consider an existing partial refund when the full amount of a Cartes Bancaires payment is disputed.

Even if you plan to accept the un-refunded portion of the dispute, it’s important to provide evidence of the partial refund in your response. Include the amount and date of the refund, and even a screenshot of the refund information from your Dashboard (this is known as a “credit issued” response).

In most cases, the card issuer cancels the original dispute and then creates a separate one for the corrected amount. On Stripe, we use the existing dispute to track the overall outcome. If the dispute is fully resolved in your favor, you receive the entire amount back. If it’s not, you only receive the partially refunded amount. In this case, the dispute’s `status` is set to `lost`.

## General evidence for dispute categories 

Every dispute reason has its own specific requirements, but some types of evidence are useful for all disputes.

> #### Evidence file size limits
> 
> Submit as much relevant evidence as possible while keeping the size and length of the final file within card issuer maximums:
> 
> - 4.5 MB for all networks
- 19 pages for Mastercard. For recommendations, see [Limit evidence file length](https://docs.stripe.com/disputes/best-practices.md#limit-file-length).

### Discrediting evidence

Providing evidence of one of the following helps increase your likelihood of proving a dispute invalid and overturning the chargeback:

| Evidence                                                                                                                             | Dashboard Evidence Category | API Evidence Parameter       |
| ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------- | ---------------------------- |
| Any documentation of the account owner [withdrawing the dispute](https://docs.stripe.com/disputes/withdrawing.md).                   | Customer communication      | `customer_communication`     |
| Proof that you already compensated the customer before they initiated the dispute (either within Stripe or using some other method). | Customer communication      | `refund_refusal_explanation` |

### Background evidence

The following types of evidence are relevant for most dispute types. Include them in every dispute response when possible. In the API, all of these data points are attributes of the [dispute evidence](https://docs.stripe.com/api/disputes/evidence_object.md) object. In the Dashboard, many of them are fields of information separate from the **Supporting evidence** section of the response form.

When your integration supports it, Stripe automatically captures most of the data for background evidence and pre-populates both the API evidence object attributes and the form fields in the Dashboard. The more information your integration [collects and passes to Stripe](https://docs.stripe.com/disputes/prevention/best-practices.md#collect-information) when your customer makes a payment, the better your ability to prevent disputes and fraud from occurring, and effectively challenge them when they do.

| Evidence                                                                                                                                                                                                                                                                                                     | Dashboard Evidence Category            | API Evidence Parameter   |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- | ------------------------ |
| The billing address provided by the customer (if the [AVS](https://docs.stripe.com/disputes/prevention/verification.md#avs-check) check was successful). This field is automatically filled when possible.                                                                                                   | Billing address                        | `billing_address`        |
| The name of the customer. This field is automatically filled when possible.                                                                                                                                                                                                                                  | Customer name                          | `customer_name`          |
| The email address of the customer. This field is automatically filled when possible.                                                                                                                                                                                                                         | Email                                  | `customer_email_address` |
| The IP address that the customer used when making the purchase. When possible, Stripe captures this data in the response and expands it to include geographical data.                                                                                                                                        | Other                                  | `customer_purchase_ip`   |
| A relevant document or contract showing the customer’s signature.                                                                                                                                                                                                                                            | Customer signature                     | `customer_signature`     |
| Any communication with the customer that you feel is relevant to your case (for example, emails proving that they received the product or service, or demonstrating their use of or satisfaction with the product or service). If you have multiple items of this type, consolidate them into a single file. | Customer communication                 | `customer_communication` |
| Any receipt or message sent to the customer notifying them of the charge. This field is automatically filled with a Stripe generated email receipt if any such receipt was sent.                                                                                                                             | Receipt                                | `receipt`                |
| A description of the product or service and any relevant details on how this was presented to the customer at the time of purchase.                                                                                                                                                                          | Product or service details Description | `product_description`    |

## Compelling evidence for Visa disputes

The Visa network has a technical specification for the evidence required to overturn disputes with a reason of [fraudulent](https://docs.stripe.com/disputes/categories.md?dispute-category=fraudulent#dispute-category-types), which they call *Compelling Evidence*.

You must provide at least one item (more is always better) that satisfies Visa’s Compelling Evidence specification for fraud disputes. Examples of evidence that meet Visa’s specification are labeled as `Compelling Evidence` in the Dashboard and in the [fraudulent](https://docs.stripe.com/disputes/categories.md?dispute-category=fraudulent#dispute-category-types) dispute type documentation.

If you don’t submit Compelling Evidence, your likelihood of overturning a Visa fraud dispute is very low, and while Visa is the only card network that designates this specification, Stripe recommends you apply the practice to all disputes.

### Visa CE 3.0 

Visa Compelling Evidence 3.0 (CE 3.0) introduced new qualifying criteria that allows businesses to show prior non-fraudulent history with the cardholder to combat [friendly fraud](https://docs.stripe.com/disputes/prevention/fraud-types.md#friendly-fraud). Submitting qualifying evidence for Visa CE 3.0 eligible disputes significantly increases the likelihood of an issuer overturning friendly fraud disputes in favor of the business. Stripe supports this feature by:

- Flagging disputes that are eligible for Visa CE 3.0 by searching your history for prior qualifying transactions
- Notifying you in the dispute email and in the [Dispute details page](https://dashboard.stripe.com/test/disputes) that the dispute qualifies for a Visa CE 3.0 counter response.
- Automatically adding qualifying transactions to your dispute evidence.
- Identifying required elements in the evidence form with (Required for Visa CE 3.0) badge.
- Pre-populating required information from qualifying transactions, when available.
- Submitting evidence for Visa CE 3.0 through the [Stripe API](https://docs.stripe.com/disputes/api/visa-ce3.md).

If you get a dispute that qualifies for a Visa CE 3.0 counter response, we recommend that you [submit evidence](https://docs.stripe.com/disputes/responding.md#respond). Read more about Visa CE 3.0 in our [Support FAQ](https://support.stripe.com/questions/how-does-stripe-support-visa-compelling-evidence-3-0).
