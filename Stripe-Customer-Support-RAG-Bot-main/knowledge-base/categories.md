# Dispute reason code categories

Learn about reason code categories and evidence guidelines.

Each payment method (such as a card, digital wallet, Buy now, Pay Later), defines hundreds of codes that represent specific reasons for dispute claims. These reasons often overlap across all of the different payment networks, thus Stripe organizes each payment method’s codes into one of eight categories. Each category is based on the general type of claim and the evidence required to effectively challenge it. You can manage disputes using the [Dashboard](https://docs.stripe.com/disputes/responding.md) or the [API](https://docs.stripe.com/disputes/api.md).

## Reason code categories 

The following tables show the Stripe categories for each payment method’s dispute reason codes. The reason code is available on the [dispute object](https://docs.stripe.com/api/disputes/object.md#dispute_object-payment_method_details-card-network_reason_code). For more information about Visa, Mastercard, and Amex, see [Dispute reason codes](https://docs.stripe.com/disputes/reason-codes-defense-requirements.md).

### Visa 

| Stripe category       | Visa code                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Credit not processed  | - 13.6 Credit not processed
  - 13.7 Canceled Merchandise/Services                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Duplicate             | - 12.6.1  Duplicate processing
  - 12.6.2  Paid by other means                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Fraudulent            | - 33    Fraud analysis request
  - 10.1  EMV Liability Shift Counterfeit Fraud
  - 10.2  EMV Liability Shift Non-Counterfeit Fraud
  - 10.3  Other Fraud - Card Present Environment
  - 10.4  Other Fraud - Card Absent Environment
  - 10.5  Visa Fraud Monitoring Program                                                                                                                                                                                                                                                      |
| General               | - 28    Request for copy bearing signature
  - 30    Cardholder request due to dispute
  - 34    Legal process request
  - 11.1  Card Recovery Bulletin
  - 11.2  Declined Authorization
  - 11.3  No Authorization
  - 12.1  Late Presentment
  - 12.2  Incorrect Transaction Code
  - 12.3  Incorrect Currency
  - 12.4  Incorrect Account Number
  - 12.5  Incorrect Amount
  - 12.7  Invalid Data
  - 13.8  Original Credit Transaction Not Accepted                                                                         |
| Product not received  | - 13.1	Merchandise/Services Not Received
  - 13.9	Non-Receipt of Cash or Load Transaction Value                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Product unacceptable  | - 13.3	Not as Described or Defective Merchandise/Services
  - 13.4	Counterfeit Merchandise
  - 13.5	Misrepresentation                                                                                                                                                                                                                                                                                                                                                                                                            |
| Subscription canceled | - 13.2	Canceled Recurring                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Noncompliant          | - C028	Refinancing of an Existing Debit
  - C030	Delayed or Amended Charges
  - C031	Sold Paper
  - C034	Merchant Processed Credit without a Previous Debit
  - C035	Merchant Must Process a Reversal If Sale Processed In Error
  - C036	Electronic Commerce Transaction
  - C038	T&E Advance Deposit Service
  - C045	Dispute Reduction Service Returned
  - C048	Split Transaction
  - C050	Other, See Attached Documentation
  - C071	Prohibitions
  - C081	Limits of Fee Collection
  - C0135	Improperly Assessed Surcharge |
| Unrecognized          | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### Mastercard 

| Stripe Category       | Mastercard Codes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Credit not processed  | - 4860	Credit Not Processed
  - 4860	Timeshares
  - 4860	Credit Posted as a Purchase                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Duplicate             | - 4834	Transaction Amount Differs
  - 4834	Cardholder Debited More than Once for the Same Goods or Services
  - 4834	ATM Disputes
  - 4834	Charges for Loss, Theft, or Damages
  - 4834	Late Presentment
  - 4834	POI Currency Conversion (Dynamic Currency Conversion)
  - 4834	Merchant Credit Correcting Error Resulting in Cardholder Currency Exchange Loss
  - 4834	Improper Merchant Surcharge (Intra-European and Inter-European transactions only)
  - 4834	Unreasonable Amount—Intra-European Economic Area (EEA) Transactions Only                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Fraudulent            | - 6341	Fraud investigation
  - 4837	No Cardholder Authorization
  - 4849	Questionable Merchant Activity
  - 4870	Chip Liability Shift
  - 4871	Chip Liability Shift—Lost/Stolen/Never Received Issue (NRI) Fraud                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| General               | - 6305	Cardholder does not agree with amount billed
  - 6322	Request Transaction Certificate for a chip transaction
  - 6323	Cardholder needs information for personal records
  - 6342	Potential chargeback or compliance documentation is required
  - 6343	IIAS Audit (for healthcare transactions only)
  - 6390	Identifies a syntax error return
  - 4808	General Chargeback AND General Arbitration Chargeback
  - 4807	Deprecated
  - 4812	Account number not on file
  - 4859	Addendum, No-show, or ATM Dispute
  - 4859	German Domestic Rule - Card Acceptor Unwilling or Unable to Render Services
  - 4859	Addendum Dispute
  - 4859	No-show Hotel Charge
  - 4831	Transaction Amount Differs
  - 4831	Cardholder Debited More than Once for the Same Goods or Services
  - 4831	Merchant Credit Correcting Error Resulting in Cardholder Currency Exchange Loss
  - 4842	DEPRECATED: Late Presentment
  - 4846	DEPRECATED: POI Currency Conversion (Dynamic Currency Conversion)
  - 4901	Required Documentation Not Received to Support Second Presentment
  - 4902	Documentation Received was Illegible
  - 4903	Scanning error—Unrelated Documents or Partial Scan
  - 4905	Acquirer Reference Data (ARD) Does Not Match or is Invalid
  - 4908	Invalid Acquirer Reference Data; Documentation Received
  - 4968	bad code - needs investigation
  - 4840	bad code - needs investigation |
| Product not received  | - 4855	Transaction Did Not Complete                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Product unacceptable  | - 4853	General Defective/Not as Described
  - 4853	Goods or Services Were Either Not as Described or Defective
  - 4853	Goods or Services Not Provided
  - 4853	Failed Travel Merchant—Intra-EEA and Domestic European Transactions Only
  - 4853	Digital Goods Purchase of USD 25 or Less
  - 4853	Credit Not Processed
  - 4853	Counterfeit Goods
  - 4853	Cardholder Dispute of a Recurring Transaction
  - 4853	Issuer Dispute of a Recurring Transaction
  - 4853	Addendum Dispute
  - 4853	No-show Hotel Charge
  - 4853	Transaction Did Not Complete
  - 4853	Timeshares
  - 4853	Credit Posted as a Purchase                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Subscription canceled | - 4841	Digital Goods Purchase of USD 25 or Less
  - 4841	Canceled Recurring or Digital Goods Transactions
  - 4841	Cardholder Dispute of a Recurring Transaction
  - 4841	Issuer Dispute of a Recurring Transaction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Unrecognized          | - 6321	Cardholder does not recognize transaction
  - 4863	Cardholder Does Not Recognize—Potential Fraud                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

### American Express 

| Stripe Category       | Amex Codes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Credit not processed  | - A01	Charge Amount Exceeds Authorization Amount
  - C02	Credit Not Processed
  - C04	Goods/Services Returned or Refused
  - C05	Goods/Services Canceled
  - C18	“No Show” or CARDeposit Canceled
  - P03	Credit Processed as Charge
  - P05	Incorrect Charge Amount
  - 061	Credit Processed as Charge
  - 062	Charge Processed as Credit
  - 154	Goods/Services Canceled/Refused
  - 158	Goods Returned (Request Credit)
  - 170	Canceled lodging reservation/CARDeposit not received
  - 175	Credit Not Processed
  - 680	Incorrect Charge Amount                                                                                                                                                                                                                                                                                                                       |
| Duplicate             | - C14	Paid by Other Means
  - P08	Duplicate Charge
  - 173	Duplicate Charge
  - 684	Paid by Other Means                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Fraudulent            | - F10	Missing Imprint
  - F24	Multiple ROCs
  - F29	Card Not Present
  - F30	EMV Liability Shift - Counterfeit
  - F31	EMV Liability Shift - Lost/Stolen/Non-Received
  - FR2	Fraud Full Recourse Program
  - FR4	Immediate Chargeback Program
  - FR5	Immediate Chargeback Program
  - FR6	Partial Immediate Chargeback Program
  - 177	Unauthorized Charge
  - 193	Fraudulent Charge                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| General               | - A02	No Valid Authorization
  - A08	Authorization Approval Expired
  - M10	Vehicle Rental - Capital Damages, Theft, or Loss of Use
  - R03	Insufficient Reply
  - R13	No Reply
  - M01	Chargeback Authorization
  - P01	Unassigned Card Number
  - P04	Charge Processed as Credit
  - P07	Late Submission
  - P22	Non-Matching Card Number
  - P23	Currency Discrepancy
  - M04	Merchant Accepted
  - M11	Reversal Due To Credit
  - M36	See Notes
  - M38	Reversal
  - M39	Correct a Previous Transaction
  - M42	Reversal Request Too Late
  - S01	Reversal Request Denied
  - S04	Reversal Request Under Review, Please Wait
  - OP1	General
  - 147	Charge paid by Insurance Company
  - 169	Charge submitted in an invalid currency
  - 693	Questioning Charge for Damage/Theft/Loss
  - S02	Reviewed Support; Will not be Debiting Account
  - S03	Support received |
| Product not received  | - C08	Goods/Services Not Received or Only Partially Received
  - 004	Product Not Received
  - 155	Goods not Received (Request Credit)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Product unacceptable  | - C31	Goods/Services Not As Described
  - C32	Goods/Services Damaged or Defective
  - 024	Goods Damaged/Defective
  - 059	Goods Damaged/Defective (Request Repair)
  - 063	Product Quality Unacceptable                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Subscription canceled | - C28	Canceled Recurring Billing
  - 021	Goods/Services Canceled/Expired                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Unrecognized          | - 127	Unrecognized Charge
  - 176	Unrecognized Charge (Card Not Present)
  - 691	Requesting Support                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### Discover 

| Stripe Category       | Discover Codes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Credit not processed  | - 8002	Credit Not Processed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Duplicate             | - 4534	Duplicate Processing
  - 4865	Paid By Other Means                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Fraudulent            | - 6041	Transaction Documentation Request for Fraud Analysis
  - 4866	Fraud Chip Card Counterfeit Transaction
  - 4867	Fraud Chip Card and PIN Transaction
  - 7010	Fraud Card Present Transaction
  - 7030	Fraud Card Not Present Transaction                                                                                                                                                                                                                                                                         |
| General               | - 6021	Transaction Documentation Request
  - 6005	Transaction Documentation Request Due to Cardholder Dispute
  - 6040	Good Faith Investigation
  - 4542	Late Presentation
  - 4550	Credit/Debit Posted Incorrectly
  - 4553	Cardholder Disputes Quality of Goods or Services
  - 4586	Altered Amount
  - 4752	Does Not Recognize
  - 4753	Invalid Cardholder Number
  - 4757	Violation of Operating Regulations
  - 4762	Good Faith Investigation
  - 4863	Authorization Non Compliance
  - 6050	Disputes Compliance |
| Product not received  | - 4755	Non-Receipt of Goods or Services
  - 4864	Non Receipt Of Cash From ATM                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Product unacceptable  | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Subscription canceled | - 4541	Recurring Payment                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Unrecognized          | None                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### Klarna 

| Stripe Category      | Klarna Code                                                 |
| -------------------- | ----------------------------------------------------------- |
| Credit not processed | - Return                                                    |
| Duplicate            | - Already paid                                              |
| Fraudulent           | - Unauthorized purchase                                     |
| General              | - Incorrect invoice
  - Pandemic impact
  - High risk order |
| Product not received | - Goods not received                                        |
| Product unacceptable | - Faulty goods                                              |

### Paypal 

| Stripe Category       | PayPal Code                                        |
| --------------------- | -------------------------------------------------- |
| Credit not processed  | - Credit not processed                             |
| Duplicate             | - Duplicate transaction
  - Payment by other means |
| Fraudulent            | - Unauthorized                                     |
| General               | - Other
  - Problem with remittance                |
| Product not received  | - Merchandise or service not received              |
| Product unacceptable  | - Merchandise or service not as described          |
| Subscription canceled | - Canceled recurring billing                       |
| Unrecognized          | - Incorrect amount                                 |

### Cash App Pay 

| Stripe Category      | Cash App Pay Code                                                                                                                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Unrecognized         | - FR10 Customer has no knowledge of the Payment.
  - FR11 Customer has no knowledge of the Payment and liability has shifted to the Merchant due to collusion, fraud monitoring program thresholds, or any other reason. |
| Duplicate            | - PE10 Payment was processed twice.
  - PE12 Customer paid by other means.                                                                                                                                               |
| General              | - PE11 Payment amount differs from agreed amount.                                                                                                                                                                        |
| Credit Not Processed | - CD10 Canceled services.
  - CD13 The purchase was canceled or returned, but the Refund hasn’t been processed.                                                                                                          |
| Product Unacceptable | - CD11 Goods or services differ from what was agreed upon for the Payment.                                                                                                                                               |
| Product Not Received | - CD12 The goods or services were not received.                                                                                                                                                                          |

## Category defense guidelines 

Use the selector to choose the category that matches the reason given for your dispute to see guidelines for responding.

#### Credit not processed

The customer claims they’re entitled to a full or partial refund because they returned the purchased product or didn’t fully use it, or the transaction was otherwise canceled or not fully fulfilled, but you haven’t yet provided a refund or credit.

### How to prevent it

- Have a clear return or cancellation policy that’s easy to find or explicitly disclosed to the customer prior to purchase.
- Honor your written policies promptly when a customer requests and is entitled to a full or partial refund.

### How to overturn it

Explain and demonstrate one or more of the following:

- You already issued the refund your customer is entitled to
- The customer isn’t entitled to a refund
- The customer [withdrew the dispute](https://docs.stripe.com/disputes/withdrawing.md)

Choose the product type of the disputed transaction to see relevant evidence suggestions.

- **Physical products** are tangible goods that were either purchased in a store or shipped to the recipient, so evidence often proves the customer is in possession of the item.
- **Digital products or services** are often virtual in nature and don’t have trackable shipping data, so focus on evidence of usage, login, or download.
- **Offline services** include purchases that are made in advance, such as event tickets and reservations, where evidence of a cancellation policy can be material.

#### evidence you can submit for - Physical product

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Designate this Dashboard label or API parameter |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| The language of your refund policy, as provided to the customer. This might be:
  - The text copied from your policy page
  - A screenshot of the policy on a receipt
  - A PDF of the applicable part of your business’s terms and conditions                                                                                                                                                                                                                                                                      | `refund_policy`                                 |
| An explanation of how and where the applicable policy was provided to your customer prior to purchase.                                                                                                                                                                                                                                                                                                                                                                                                              | `refund_policy_disclosure`                      |
| Your explanation for why the customer isn’t entitled to a refund, or no further refund, if you already issued a partial refund.                                                                                                                                                                                                                                                                                                                                                                                     | `refund_refusal_explanation`                    |
| Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

  If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

  - A screenshot of a text conversation
  - A PDF of an email exchange
  - A PDF of your written account of a phone conversation, including dates of contact | `customer_communication`                        |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - Whether you already issued the refund the cardholder is entitled to
  - Whether or not the customer returned the merchandise in whole or in part. If they partially used the merchandise or returned it, or whether the dispute amount exceeds the value of the unused portion
  - Whether the cardholder withdrew the dispute                                                                                              | `uncategorized_text` `uncategorized_file`       |

#### evidence you can submit for - Digital product or service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Designate this Dashboard label or API parameter             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| The language of the applicable cancellation or refund policy, as provided to the customer. This might be:
  - The text copied from your policy page
  - A screenshot of the policy on a receipt
  - A PDF of the applicable part of your business’s terms and conditions                                                                                                                                                                                                                                            | `cancellation_policy` `refund_policy`                       |
| An explanation of how and where you provided the applicable policy to your customer prior to purchase.                                                                                                                                                                                                                                                                                                                                                                                                              | `cancellation_policy_disclosure` `refund_policy_disclosure` |
| Your explanation for why the customer isn’t entitled to a cancellation or refund.                                                                                                                                                                                                                                                                                                                                                                                                                                   | `cancellation_rebuttal` `refund_refusal_explanation`        |
| Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

  If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

  - A screenshot of a text conversation
  - A PDF of an email exchange
  - A PDF of your written account of a phone conversation, including dates of contact | `customer_communication`                                    |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:
  - Whether you already issued the refund the cardholder is entitled to
  - Whether or not the customer used the digital product or service in whole or in part. If they partially used it, or whether the dispute amount exceeds the value of the unused portion
  - Whether the cardholder withdrew the dispute                                                                                                                | `uncategorized_text` `uncategorized_file`                   |

#### evidence you can submit for - Offline service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Designate this Dashboard label or API parameter             |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| The language of your refund policy, as provided to the customer. This might be:
  - The text copied from your policy page
  - A screenshot of the policy on a receipt
  - A PDF of the applicable part of your business’s terms and conditions                                                                                                                                                                                                                                                                      | `cancellation_policy` `refund_policy`                       |
| An explanation of how and where you provided the applicable policy to your customer prior to purchase.                                                                                                                                                                                                                                                                                                                                                                                                              | `cancellation_policy_disclosure` `refund_policy_disclosure` |
| Your explanation for why the customer isn’t entitled to a refund.                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `cancellation_rebuttal` `refund_refusal_explanation`        |
| Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

  If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

  - A screenshot of a text conversation
  - A PDF of an email exchange
  - A PDF of your written account of a phone conversation, including dates of contact | `customer_communication`                                    |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - Whether you already issued the refund the cardholder is entitled to
  - If they partially used the service, or whether the dispute amount exceeds the value of the unused portion
  - Whether the cardholder withdrew the dispute                                                                                                                                                                                           | `uncategorized_text` `uncategorized_file`                   |

#### Duplicate

The customer claims they were charged multiple times for the same product or service.

### How to prevent it

- If a customer’s card is accidentally charged more than once for a single payment, correct the duplicates immediately and get in touch with the customer to let them know you’ve handled the issue.
- Send detailed receipts that explain every payment and make it easy to distinguish the unique reason for each.
- If you built your own Stripe integration, ensure it can [handle errors](https://docs.stripe.com/api/errors/handling.md) without double-charging.
- Honor your written policies promptly when a customer requests and is entitled to a refund for a duplicate payment.

### How to overturn it

Explain and demonstrate one or more of the following:

- Each payment was for a separate product or service
- You already issued a refund to your customer
- The customer [withdrew the dispute](https://docs.stripe.com/disputes/withdrawing.md)

Choose the product type of the disputed transaction to see relevant evidence suggestions.

- **Physical products** are tangible goods that were either purchased in a store or shipped to the recipient, so evidence often proves the customer is in possession of the item.
- **Digital products or services** are often virtual in nature and don’t have trackable shipping data, so focus on evidence of usage, login, or download.
- **Offline services** include purchases that are made in advance, such as event tickets and reservations, where evidence of a cancellation policy can be material.

#### evidence you can submit for - Physical product

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Designate this Dashboard label or API parameter |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| The charge ID for the previous payment that appears to be a duplicate of the disputed one. If no duplicate charge exists, you can’t provide a duplicate charge ID when prompted to supply evidence in the Dashboard. In such cases, you can select **All Fields** from the gear menu and provide alternate evidence that is applicable to the dispute in question.                                                                                                                                                     | `duplicate_charge_id`                           |
| An explanation of the difference between the disputed payment and the one the customer believes it’s a duplicate of.                                                                                                                                                                                                                                                                                                                                                                                                   | `duplicate_charge_explanation`                  |
| Documentation for the prior payment that can uniquely identify it, such as a separate receipt. This document should be paired with a similar document from the disputed payment that proves the two are separate. This should also include a separate shipping label or receipt for the other payment. If multiple products were shipped together, provide a packing list that shows each purchase.                                                                                                                    | `duplicate_charge_documentation`                |
| A shipping label or receipt for the product the disputed payment is for.                                                                                                                                                                                                                                                                                                                                                                                                                                               | `shipping_documentation`                        |
| Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

  If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

  - A screenshot of a text conversation
  - A PDF of an email exchange
  - A PDF of your written account of a phone conversation, including dates of contact    | `customer_communication`                        |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - Any and all information documenting that each payment was made separately, such as copies of receipts. If the receipts don’t include the items purchased, be sure to include an itemized list. Each receipt should clearly indicate that the payments are for separate purchases of items or services.
  - Whether you already issued the refund the cardholder is entitled to
  - Whether the cardholder withdrew the dispute | `uncategorized_text` `uncategorized_file`       |

#### evidence you can submit for - Digital product or service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Designate this Dashboard label or API parameter |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| The charge ID for the previous payment that appears to be a duplicate of the disputed one. If no duplicate charge exists, you can’t provide a duplicate charge ID when prompted to supply evidence in the Dashboard. In such cases, you can select **All Fields** from the gear menu and provide alternate evidence that is applicable to the dispute in question.                                                                                                                                                                                                                                                                   | `duplicate_charge_id`                           |
| An explanation of the difference between the disputed payment and the one the customer believes it’s a duplicate of.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `duplicate_charge_explanation`                  |
| Documentation for the prior payment that can uniquely identify it, such as a separate receipt. Pair this document with a similar document from the disputed payment that proves the two are separate. Also include a separate shipping label or receipt for the other payment. If multiple products shipped together, provide a packing list that shows each purchase.                                                                                                                                                                                                                                                               | `duplicate_charge_documentation`                |
| Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

  If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

  - A screenshot of a text conversation
  - A PDF of an email exchange
  - A PDF of your written account of a phone conversation, including dates of contact                                                                                                                  | `customer_communication`                        |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - Any information documenting that each payment was made separately, such as copies of receipts. If the receipts don’t include the items purchased, be sure to include an itemized list. Make sure each receipt clearly indicates that the payments are for separate purchases of items or services. If you’ve been able to get in touch with the customer, be sure to address any concerns they had in your evidence.
  - Whether you already issued the refund the cardholder is entitled to
  - Whether the cardholder withdrew the dispute | `uncategorized_text` `uncategorized_file`       |

#### evidence you can submit for - Offline service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Designate this Dashboard label or API parameter |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| The charge ID for the previous payment that appears to be a duplicate of the one that is disputed. If no duplicate charge exists, you can’t provide a duplicate charge ID when prompted to supply evidence in the Dashboard. In such cases, you can select **All Fields** from the gear menu and provide alternate evidence that is applicable to the dispute in question.                                                                                                                                                                                                                                                                  | `duplicate_charge_id`                           |
| An explanation of the difference between the disputed payment and the one the customer believes it’s a duplicate of.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `duplicate_charge_explanation`                  |
| Documentation for the prior payment that can uniquely identify it, such as a separate receipt. Pair this document with a similar document from the disputed payment that proves the two are separate. Also include a separate shipping label or receipt for the other payment. If multiple products shipped together, provide a packing list that shows each purchase.                                                                                                                                                                                                                                                                      | `duplicate_charge_documentation`                |
| A copy of a service agreement or documentation for the disputed payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `service_documentation`                         |
| Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

  If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

  - A screenshot of a text conversation
  - A PDF of an email exchange
  - A PDF of your written account of a phone conversation, including dates of contact                                                                                                                         | `customer_communication`                        |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - Any information documenting that each payment was made separately, such as copies of receipts. If the receipts don’t include the items purchased, be sure to include an itemized list. Make sure that each receipt clearly indicates that the payments are for separate purchases of items or services. If you’ve been able to get in touch with the customer, make sure to address any concerns they had in your evidence.
  - Whether you already issued the refund the cardholder is entitled to
  - Whether the cardholder withdrew the dispute | `uncategorized_text` `uncategorized_file`       |

#### Fraudulent

This is the most common reason for a dispute and happens when a cardholder claims that they didn’t authorize the payment. The cardholder might have made an error and failed to recognize a legitimate charge on their credit card statement, or they might have genuinely been a victim of someone using their card fraudulently. This is a difficult dispute type to win because in many cases the reason for the dispute is correct. If you believe the payment was indeed fraud, the appropriate action is to either [accept the dispute](https://docs.stripe.com/disputes/responding.md) or decline to challenge it.

### How to prevent it

Because fraud disputes are so difficult to win, prevention is key. Good strategies include:

- Make sure your [statement descriptor](https://docs.stripe.com/get-started/account/statement-descriptors.md) is easily recognizable to your customers and reflects the URL or business name they would associate with their purchase
- Send [receipts](https://docs.stripe.com/receipts.md) upon payment so your customers can remember what they paid for
- Familiarize yourself with the [best practices for preventing fraud](https://docs.stripe.com/disputes/prevention/best-practices.md)

### How to overturn it

Explain and demonstrate one or more of the following:

- That the legitimate cardholder—or an authorized representative (such as an employee or family member)—did in fact make the payment
- That the payment was successfully authenticated with *3D Secure* (3D Secure (3DS) provides an additional layer of authentication for credit card transactions that protects businesses from liability for fraudulent card payments) and should therefore fall under liability shift (Stripe provides the *Electronic Commerce Indicator (ECI)* (An Electronic Commerce Indicator (ECI) is a code returned alongside a 3D Secure authentication result. It indicates the authentication method and result and may be used subsequently to, for example, determine eligibility for liability shift) automatically for you)
- You already issued a refund to the cardholder
- The customer [withdrew the dispute](https://docs.stripe.com/disputes/withdrawing.md) or otherwise acknowledged they recognize the charge and filed the fraud dispute in error
- For Visa specifically, provide [Compelling Evidence](https://docs.stripe.com/disputes/categories.md#visa)

> Visa disputes with reason code 10.5 are extremely rare and have no recourse to remedy the dispute. Visa considers these types of transactions fraudulent by Visa and doesn’t accept evidence for these disputes.

Choose the product type of the disputed transaction to see relevant evidence suggestions.

- **Physical products** are tangible goods that were either purchased in a store or shipped to the recipient, so evidence often proves the customer is in possession of the item.
- **Digital products or services** are often virtual in nature and don’t have trackable shipping data, so focus on evidence of usage, login, or download.
- **Offline services** include purchases that are made in advance, such as event tickets and reservations, where evidence of a cancellation policy can be material.

#### evidence you can submit for - Physical product

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Designate this Dashboard label or API parameter                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Evidence (for example, photographs or emails) to prove a link between the person receiving products and the cardholder, or proving that the cardholder disputing the transaction is in possession of the products.
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `customer_communication` `uncategorized_text` `uncategorized_file` |
| Evidence that the person who signed for the products was authorized to sign for—or is known by—the cardholder. If the products were collected from a physical location, you should provide:

  - Cardholder signature on the pickup form
  - A copy of identification presented by the cardholder
  - Details of identification presented by the cardholder
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `customer_signature` `uncategorized_text` `uncategorized_file`     |
| The address you shipped a physical product to. The shipping address must match a billing address verified with [AVS](https://docs.stripe.com/disputes/prevention/verification.md#avs-check) or be the address of a business that’s connected to the legitimate cardholder in some way.
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `shipping_address`                                                 |
| Documentation showing the product was shipped to the cardholder at the same address the cardholder provided to you. This should ideally include a copy of the shipment receipt or label, and show the full shipping address of the cardholder.
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `shipping_documentation`                                           |
| The date that a physical product began its route to the shipping address in a clear, human-readable format. This date is prior to the date of the dispute.
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `shipping_date`                                                    |
| The delivery service that shipped a physical product, such as Fedex, UPS, USPS, and so on. If multiple carriers were used for this purchase, separate them with commas.
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `shipping_carrier`                                                 |
| The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, separate them with commas. When Stripe compiles your evidence into a single document, these tracking numbers are expanded to include detailed delivery information from the carrier.
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `shipping_tracking_number`                                         |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - A signed order form for products purchased by mail or phone order
  - Evidence that the transaction was completed by a member of the cardholder’s family or household
  - Evidence of one or more non-disputed payments on the same card
  - Evidence that payments on the same card had been disputed as fraud prior to the issuer authorizing this transaction
  - Evidence that the card’s CVC value was presented at purchase, but the issuer either authorized the charge despite the check failing (`cvc_check` value of `fail`), or didn’t verify it in the first place (`cvc_check` value of `unchecked`)
  - For recurring payments, evidence of a legally binding contract held between your business and the cardholder, that the cardholder is using the products, and of any previous payments not disputed
  - Whether you already issued the refund the cardholder is entitled to
  - Whether the cardholder withdrew the dispute
(Compelling Evidence) | `uncategorized_file` `uncategorized_text`                          |

#### evidence you can submit for - Digital product or service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Designate this Dashboard label or API parameter |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| Customer’s IP address at the time of purchase
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `customer_purchase_ip`                          |
| Name of customer
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `customer_name`                                 |
| Email address of customer
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `customer_email_address`                        |
| Server or activity logs showing proof that the customer accessed or downloaded the purchased digital product after they made the payment. This should ideally include IP addresses, corresponding timestamps, and any detailed recorded activity.
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `access_activity_log`                           |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - Device geographical location at the date and time of transaction
  - Device ID, number, and name (if applicable)
  - Evidence that the transaction was completed by a member of the cardholder’s family or household
  - Evidence of one or more non-disputed payments on the same card
  - Evidence that payments on the same card had been disputed as fraud prior to the issuer authorizing this transaction
  - Evidence that the card’s CVC value was presented at purchase, but the issuer either authorized the charge despite the check failing (`cvc_check` value of `fail`), or didn’t verify it in the first place (`cvc_check` value of `unchecked`)
  - Whether you already issued the refund the cardholder is entitled to
  - Whether the cardholder withdrew the dispute
(Compelling Evidence) | `uncategorized_file` `uncategorized_text`       |

#### evidence you can submit for - Offline service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Designate this Dashboard label or API parameter                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Evidence (for example, photographs or emails) to prove a link between the person receiving the service and the cardholder, or proving that the cardholder disputing the transaction has used or is still using the service.
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `customer_communication` `uncategorized_text` `uncategorized_file` |
| Evidence that the person who signed for the service was authorized to sign for—or is known by—the cardholder. Provide any of the following, if you have them:

  - Cardholder signature on the pickup form
  - A copy of identification presented by the cardholder
  - Details of identification presented by the cardholder
(Compelling Evidence)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `customer_signature` `uncategorized_text` `uncategorized_file`     |
| Documentation showing that the service was provided to the cardholder, including the date that the cardholder received or began receiving the purchased service in a clear, human-readable format. This could include a copy of a signed contract, work order, or other form of written agreement.

  For passenger transportation or services or travel and expense transactions, evidence that the service was provided and any of the following:

  - Proof that the ticket was received at the cardholder’s billing address
  - Evidence of payments related to the disputed payment, such as seat upgrades, extra baggage, and purchases made on board the passenger transport
  - Details of loyalty program rewards earned or redeemed, including address and phone number, that establish a link to the cardholder
  - Evidence that other payments related to the original payment, like upgrades, were not disputed
(Compelling Evidence)                                                                                                            | `service_date` `service_documentation`                             |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - A signed order form for products purchased by mail or phone order
  - Evidence that the transaction was completed by a member of the cardholder’s family or household
  - Evidence of one or more non-disputed payments on the same card
  - Evidence that payments on the same card had been disputed as fraud prior to the issuer authorizing this transaction
  - Evidence that the card’s CVC value was presented at purchase, but the issuer either authorized the charge despite the check failing (`cvc_check` value of `fail`), or didn’t verify it in the first place (`cvc_check` value of `unchecked`)
  - For recurring payments, evidence of a legally binding contract held between your business and the cardholder, that the cardholder is using the products, and of any previous payments not disputed
  - Whether you already issued the refund the cardholder is entitled to
  - Whether the cardholder withdrew the dispute
(Compelling Evidence) | `uncategorized_file` `uncategorized_text`                          |

#### General

This is an uncategorized dispute, so contact the customer for additional details to find out why they disputed the payment. This should be fairly rare for cards disputes.

#### Product not received

The customer claims they did not receive the products or services purchased.

### How to prevent it

- For physical products, promptly ship them after payment is made
- Estimate shipping and delivery dates as accurately as you can, and communicate clearly with your customer. If shipping delays arise unexpectedly, keep your customer informed.
- Save shipping labels, and for high-value products consider requiring a signature upon receipt.
- Make it easy for your customers to reach out when they have issues receiving their products (for example: send [receipts](https://docs.stripe.com/receipts.md) upon payment so your customers can easily reply to get in touch).
- For digital goods or services, maintain access logs or documentation that tie usage back to the customer.
- Honor your written policies promptly when a customer requests a full or partial refund they’re entitled to for products or services they didn’t receive.

### How to overturn it

Explain and demonstrate one or more of the following:

- The product was in fact delivered or isn’t expected to have been delivered yet (for example, the agreed-upon delivery date is still in the future)
- You already issued a refund to the cardholder
- The customer [withdrew the dispute](https://docs.stripe.com/disputes/withdrawing.md)

Choose the product type of the disputed transaction to see relevant evidence suggestions.

- **Physical products** are tangible goods that were either purchased in a store or shipped to the recipient, so evidence often proves the customer is in possession of the item.
- **Digital products or services** are often virtual in nature and don’t have trackable shipping data, so focus on evidence of usage, login, or download.
- **Offline services** include purchases that are made in advance, such as event tickets and reservations, where evidence of a cancellation policy can be material.

#### evidence you can submit for - Physical product

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Designate this Dashboard label or API parameter                |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Evidence proving that the cardholder disputing the transaction is in possession of the products.                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `uncategorized_text` `uncategorized_file`                      |
| Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

  If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

  - A screenshot of a text conversation
  - A PDF of an email exchange
  - A PDF of your written account of a phone conversation, including dates of contact                                         | `customer_communication`                                       |
| Evidence that someone signed for the products when they were picked up or delivered. If they collected the products from a physical location, make sure you provide:

  - Cardholder signature on the pickup form
  - A copy of identification presented by the cardholder
  - Details of identification presented by the cardholder                                                                                                                                                                                                                        | `customer_signature` `uncategorized_text` `uncategorized_file` |
| The address you shipped a physical product to. The shipping address needs to match a billing address verified with [AVS](https://docs.stripe.com/disputes/prevention/verification.md#avs-check) or be the address of a business that’s connected to the cardholder in some way.                                                                                                                                                                                                                                                                             | `shipping_address`                                             |
| Documentation showing you shipped the product to the cardholder at the same address the cardholder provided to you. Ideally include a copy of the shipment receipt or label, and show the full shipping address of the cardholder.                                                                                                                                                                                                                                                                                                                          | `shipping_documentation`                                       |
| The date that a physical product began its route to the shipping address in a clear, human-readable format.                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `shipping_date`                                                |
| The delivery service that shipped a physical product, such as Fedex, UPS, USPS, and so on. If multiple carriers were used for this purchase, separate them with commas.                                                                                                                                                                                                                                                                                                                                                                                     | `shipping_carrier`                                             |
| The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, separate them with commas. When Stripe compiles your evidence into a single document, these tracking numbers are expanded to include detailed delivery information from the carrier.                                                                                                                                                                                                                         | `shipping_tracking_number`                                     |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - Evidence that the agreed-upon delivery date hasn’t arrived yet
  - If the purchase was made up of multiple different shipments and some of them were delivered successfully, evidence that the dispute amount exceeds the value of the unreceived shipments
  - Evidence that delivery is being held by customs in the cardholder’s country
  - Whether you already issued the refund the cardholder is entitled to
  - Whether the cardholder withdrew the dispute | `uncategorized_file` `uncategorized_text`                      |

#### evidence you can submit for - Digital product or service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Designate this Dashboard label or API parameter |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Customer’s IP address at the time of purchase                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `customer_purchase_ip`                          |
| Name of customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `customer_name`                                 |
| Email address of customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `customer_email_address`                        |
| Server or activity logs showing proof that the customer accessed or downloaded the purchased digital product after the payment was made. Ideally include IP addresses, corresponding timestamps, and any detailed recorded activity.                                                                                                                                                                                                                                                                                                                                                                     | `access_activity_log`                           |
| Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

  If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

  - A screenshot of a text conversation
  - A PDF of an email exchange
  - A PDF of your written account of a phone conversation, including dates of contact                                                                                      | `customer_communication`                        |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - Device geographical location at the date and time of transaction
  - Device ID, number, and name (if applicable)
  - Evidence that the agreed-upon delivery date hasn’t arrived yet
  - If the purchase was made up of multiple different electronic deliveries and some of them were delivered successfully, evidence that the dispute amount exceeds the value of the unreceived items
  - Whether you already issued the refund the cardholder is entitled to
  - Whether the cardholder withdrew the dispute | `uncategorized_file` `uncategorized_text`       |

#### evidence you can submit for - Offline service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Designate this Dashboard label or API parameter                |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| Evidence proving that the cardholder disputing the transaction received the service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `uncategorized_text` `uncategorized_file`                      |
| Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

  If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

  - A screenshot of a text conversation
  - A PDF of an email exchange
  - A PDF of your written account of a phone conversation, including dates of contact                                             | `customer_communication`                                       |
| Evidence that the service was signed for. If possible, you should provide:

  - Cardholder signature
  - A copy of identification presented by the cardholder
  - Details of identification presented by the cardholder                                                                                                                                                                                                                                                                                                                                         | `customer_signature` `uncategorized_text` `uncategorized_file` |
| Documentation showing that the service was provided to the cardholder, including the date that the cardholder received or began receiving the purchased service in a clear, human-readable format. This could include a copy of a signed contract, work order, or other form of written agreement.                                                                                                                                                                                                                                                              | `service_date` `service_documentation`                         |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - Evidence that the agreed-upon service date hasn’t arrived yet
  - If the purchase was made up of multiple different shipments and some of them were delivered successfully, evidence that the dispute amount exceeds the value of the unreceived shipments
  - Evidence that delivery is being held by customs in the cardholder’s country
  - Whether you have already issued the refund the cardholder is entitled to
  - Whether the cardholder withdrew the dispute | `uncategorized_file` `uncategorized_text`                      |

#### Product unacceptable

The customer received the product but claims it was defective or damaged in some way, or was not described or represented in an accurate manner prior to purchase.

### How to prevent it

- Ensure that the description of products or services shown in advertisements, online, and transaction receipts, or used in telephone order-taking scripts are accurate, complete, and not misleading.
- Never refer cardholders to the manufacturer in lieu of attempting to resolve the issue directly—the business selling the product or service is liable and must be the point of contact for resolution.

### How to overturn it

Explain and demonstrate one or more of the following:

- That the product or service was accurately represented prior to purchase
- That the product wasn’t damaged or defective
- You already issued a refund to your customer
- The customer [withdrew the dispute](https://docs.stripe.com/disputes/withdrawing.md)

Choose the product type of the disputed transaction to see relevant evidence suggestions.

- **Physical products** are tangible goods that were either purchased in a store or shipped to the recipient, so evidence often proves the customer is in possession of the item.
- **Digital products or services** are often virtual in nature and don’t have trackable shipping data, so focus on evidence of usage, login, or download.
- **Offline services** include purchases that are made in advance, such as event tickets and reservations, where evidence of a cancellation policy can be material.

#### evidence you can submit for - Physical product

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Designate this Dashboard label or API parameter |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| A description of the product as you represented it to the customer, or images that display how you showed the product to the customer prior to purchase.                                                                                                                                                                                                                                                                                                                                                            | `product_description` `uncategorized_file`      |
| Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

  If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

  - A screenshot of a text conversation
  - A PDF of an email exchange
  - A PDF of your written account of a phone conversation, including dates of contact | `customer_communication`                        |
| The language of your refund policy and how you disclosed it to the customer prior to purchase. This might be:

  - The text copied from your policy page
  - A screenshot of the policy on a receipt
  - A PDF of the applicable part of your business’s terms and conditions

  Depending on network and context, the issuer might or might not take this into consideration, but it can’t hurt your case and is generally worth including.                                                                        | `refund_policy` `refund_policy_disclosure`      |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - Whether or not the customer returned the product to you.
  - If the product was partially used or consumed, whether the dispute amount exceeds the value of the unused portion
  - Whether you already issued the refund the cardholder is entitled to
  - Whether you have already provided a replacement product
  - Whether the cardholder withdrew the dispute                                                          | `uncategorized_file` `uncategorized_text`       |

#### evidence you can submit for - Digital product or service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Designate this Dashboard label or API parameter |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| A description of the digital product or service as it was represented to the customer, or images that display how the customer was shown the product prior to purchase.                                                                                                                                                                                                                                                                                                                                             | `product_description` `uncategorized_file`      |
| Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

  If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

  - A screenshot of a text conversation
  - A PDF of an email exchange
  - A PDF of your written account of a phone conversation, including dates of contact | `customer_communication`                        |
| Any server or activity logs showing proof that the cardholder accessed or downloaded the purchased digital product. This information should include IP addresses, corresponding timestamps, and any detailed recorded activity.                                                                                                                                                                                                                                                                                     | `access_activity_log`                           |
| The language of your refund policy and how you disclosed it to the customer prior to purchase. This might be:

  - The text copied from your policy page
  - A screenshot of the policy on a receipt
  - A PDF of the applicable part of your business’s terms and conditions

  Depending on network and context, the issuer might or might not take this into consideration, but it can’t hurt your case and is generally worth including.                                                                        | `refund_policy` `refund_policy_disclosure`      |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - If the product was partially used or consumed, whether the dispute amount exceeds the value of the unused portion
  - Whether you already issued the refund the cardholder is entitled to
  - Whether you already provided a replacement service
  - Whether the cardholder withdrew the dispute                                                                                                                            | `uncategorized_file` `uncategorized_text`       |

#### evidence you can submit for - Offline service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Designate this Dashboard label or API parameter |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| A description of the service as you represented it to the customer, or images that display how you advertised the service to the customer prior to purchase.                                                                                                                                                                                                                                                                                                                                                        | `product_description` `uncategorized_file`      |
| Whether or not the customer attempted to resolve the issue with you prior to filing a dispute. If they didn’t reach out to you before the dispute, state that clearly.

  If you did communicate with them prior to the dispute, or if later conversations shed light on the facts of the case, submit this with your evidence. This could look like:

  - A screenshot of a text conversation
  - A PDF of an email exchange
  - A PDF of your written account of a phone conversation, including dates of contact | `customer_communication`                        |
| The language of your refund policy and how it was disclosed to the customer prior to purchase. This might be:

  - The text copied from your policy page
  - A screenshot of the policy on a receipt
  - A PDF of the applicable part of your business’s terms and conditions

  Depending on network and context, the issuer might or might not take this into consideration, but it can’t hurt your case and is generally worth including.                                                                        | `refund_policy` `refund_policy_disclosure`      |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - If the service was only partially used, whether the dispute amount exceeds the value of the unused portion
  - Whether you already issued the refund the cardholder is entitled to
  - Whether you already provided a replacement service
  - Whether the cardholder withdrew the dispute                                                                                                                                   | `uncategorized_file` `uncategorized_text`       |

#### Subscription canceled

The customer claims that you continued to charge them after a subscription was canceled.

### How to prevent it

- Promptly cancel subscriptions upon request, making sure to pass the cancellation along to Stripe if you use our [subscription](https://docs.stripe.com/billing.md) functionality and provide your customer with a confirmation of the cancellation.
- Make it clear on your signup page that your customers are agreeing to a recurring payment and include information about whether or not you plan to notify the customer before each payment.
- Make sure cancellation procedures and policies are clearly communicated to your customers.

### How to overturn it

Explain and demonstrate one or more of the following:

- The subscription was still active and that the customer was aware of, and did not follow, your cancellation procedure.
- You already issued a refund to your customer
- The customer [withdrew the dispute](https://docs.stripe.com/disputes/withdrawing.md)

Choose the product type of the disputed transaction to see relevant evidence suggestions.

- **Physical products** are tangible goods that were either purchased in a store or shipped to the recipient, so evidence often proves the customer is in possession of the item.
- **Digital products or services** are often virtual in nature and don’t have trackable shipping data, so focus on evidence of usage, login, or download.
- **Offline services** include purchases that are made in advance, such as event tickets and reservations, where evidence of a cancellation policy can be material.

#### evidence you can submit for - Physical product

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Designate this Dashboard label or API parameter |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Your subscription cancellation policy, as shown to the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `cancellation_policy`                           |
| An explanation of how and when the customer was shown your cancellation policy prior to purchase.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `cancellation_policy_disclosure`                |
| A justification for why the customer’s subscription was not canceled, or if it was canceled, why this particular payment is still valid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `cancellation_rebuttal`                         |
| A notification sent to the customer of a renewal or continuation of the subscription, or an acknowledgement from the customer of their continued use of the product or service after the date they claim they canceled the subscription (if available).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `customer_communication`                        |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - If the product was consumed prior to the billing (in cases where billing occurs regularly, but consumption of whatever is being billed for happens prior to the billing)
  - If the product was partially used, whether the dispute amount exceeds the value of the unused portion
  - If customer is mistaken about what the actual cancellation date was (for example, in cases where the cancellation was set for a future date)
  - If the payment was actually an [installment payment](https://docs.stripe.com/payments/buy-now-pay-later.md) (some networks permit this dispute reason code only for genuinely recurring transactions, not installments of a single payment)
  - Whether you already issued the refund the cardholder is entitled to
  - Whether you already provided a replacement service
  - Whether the cardholder withdrew the dispute | `uncategorized_file` `uncategorized_text`       |

#### evidence you can submit for - Digital product or service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Designate this Dashboard label or API parameter |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Your subscription cancellation policy, as shown to the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `cancellation_policy`                           |
| An explanation of how and when the customer was shown your cancellation policy prior to purchase.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `cancellation_policy_disclosure`                |
| A justification for why the customer’s subscription wasn’t canceled, or if it was canceled, why this particular payment is still valid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `cancellation_rebuttal`                         |
| A notification sent to the customer of a renewal or continuation of the subscription, or an acknowledgement from the customer of their continued use of the product or service after the date they claim they canceled the subscription (if available).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `customer_communication`                        |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - What controls you have in place for customers to regulate automated spending, monitor their own usage, and prevent inadvertent automated billing.
  - If the digital product or service was consumed prior to the billing (in cases where billing occurs regularly, but consumption whatever is being billed for happens prior to the billing)
  - If the product was partially used, whether the dispute amount exceeds the value of the unused portion
  - If the customer is mistaken about what the actual cancellation date was (for example, in cases where the cancellation was set for a future date)
  - If the payment was actually an [installment payment](https://docs.stripe.com/payments/buy-now-pay-later.md) (some networks permit this dispute reason code only for genuinely recurring transactions, not installments of a single payment)
  - Whether you already issued the refund the cardholder is entitled to
  - Whether you already provided a replacement product or service
  - Whether the cardholder withdrew the dispute | `uncategorized_file` `uncategorized_text`       |

#### evidence you can submit for - Offline service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Designate this Dashboard label or API parameter |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Your subscription cancellation policy, as shown to the customer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `cancellation_policy`                           |
| An explanation of how and when the customer was shown your cancellation policy prior to purchase.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `cancellation_policy_disclosure`                |
| A justification for why the customer’s subscription wasn’t canceled, or if it was canceled, why this particular payment is still valid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `cancellation_rebuttal`                         |
| The date on which the cardholder received or began receiving the purchased service in a clear, human-readable format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `service_date`                                  |
| Documentation showing proof that a service was provided to the cardholder. This could include a copy of a signed contract, work order, or other form of written agreement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `service_documentation`                         |
| A notification sent to the customer of a renewal or continuation of the subscription, or an acknowledgement from the customer of their continued use of the product or service after the date they claim they canceled the subscription (if available).                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `customer_communication`                        |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - If the service was consumed prior to the billing (in cases where billing occurs regularly, but consumption of whatever is being billed for happens prior to the billing)
  - If the service was partially used, whether the dispute amount exceeds the value of the unused portion
  - If the customer is mistaken about what the actual cancellation date was (for example, in cases where the cancellation was set for a future date)
  - Whether you already issued the refund the cardholder is entitled to
  - Whether you already provided a replacement service
  - Whether the cardholder withdrew the dispute | `uncategorized_file` `uncategorized_text`       |

#### Unrecognized

The customer doesn’t recognize the payment appearing on their card statement. This is effectively indistinguishable from the Fraudulent reason.

### How to prevent it

- Make sure your [statement descriptor](https://docs.stripe.com/get-started/account/statement-descriptors.md) is easily recognizable to your customers and reflects the URL or business name they would associate with their purchase
- Send [receipts](https://docs.stripe.com/receipts.md) upon payment so your customers can recall what they paid for

### How to overturn it

Explain and demonstrate one or more of the following:

- That the legitimate cardholder—or an authorized representative (such as an employee or family member)—did in fact make the payment
- You already issued a refund to the cardholder
- The customer [withdrew the dispute](https://docs.stripe.com/disputes/withdrawing.md) or otherwise acknowledged they recognize the charge and filed the fraud dispute in error

Choose the product type of the disputed transaction to see relevant evidence suggestions.

- **Physical products** are tangible goods that were either purchased in a store or shipped to the recipient, so evidence often proves the customer is in possession of the item.
- **Digital products or services** are often virtual in nature and don’t have trackable shipping data, so focus on evidence of usage, login, or download.
- **Offline services** include purchases that are made in advance, such as event tickets and reservations, where evidence of a cancellation policy can be material.

#### evidence you can submit for - Physical product

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Designate this Dashboard label or API parameter                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Evidence (for example, photographs or emails) to prove a link between the person receiving products and the cardholder, or proving that the cardholder disputing the transaction is in possession of the products.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `customer_communication` `uncategorized_text` `uncategorized_file` |
| Evidence that the person who signed for the products was authorized to sign for—or is known by—cardholder. If they collected the products from a physical location, make sure you provide:

  - Cardholder signature on the pickup form
  - A copy of identification presented by the cardholder
  - Details of identification presented by the cardholder                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `customer_signature` `uncategorized_text` `uncategorized_file`     |
| The address you shipped a physical product to. The shipping address must match a billing address verified with [AVS](https://docs.stripe.com/disputes/prevention/verification.md#avs-check) or be the address of a business that’s connected to the legitimate cardholder in some way.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `shipping_address`                                                 |
| Documentation showing the product was shipped to the cardholder at the same address the cardholder provided to you. This should ideally include a copy of the shipment receipt or label, and show the full shipping address of the cardholder.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `shipping_documentation`                                           |
| The date that a physical product began its route to the shipping address in a clear, human-readable format. This date is prior to the date of the dispute.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `shipping_date`                                                    |
| The delivery service that shipped a physical product, such as Fedex, UPS, USPS, and so on. If multiple carriers were used for this purchase, separate them with commas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `shipping_carrier`                                                 |
| The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, separate them with commas. When Stripe compiles your evidence into a single document, these tracking numbers are expanded to include detailed delivery information from the carrier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `shipping_tracking_number`                                         |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - A signed order form for products purchased by mail or phone order
  - Evidence that the transaction was completed by a member of the cardholder’s family or household
  - Evidence of one or more non-disputed payments on the same card
  - Evidence that payments on the same card had been disputed as fraud prior to the issuer authorizing this transaction
  - Evidence that the card’s CVC value was presented at purchase, but the issuer either authorized the charge despite the check failing (`cvc_check` value of `fail`), or didn’t verify it in the first place (`cvc_check` value of `unchecked`)
  - For recurring payments, evidence of a legally binding contract held between your business and the cardholder, that the cardholder is using the products, and of any previous payments not disputed
  - Whether you already issued the refund the cardholder is entitled to
  - Whether the cardholder withdrew the dispute | `uncategorized_file` `uncategorized_text`                          |

#### evidence you can submit for - Digital product or service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Designate this Dashboard label or API parameter |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| Customer’s IP address at the time of purchase                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `customer_purchase_ip`                          |
| Name of customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `customer_name`                                 |
| Email address of customer                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `customer_email_address`                        |
| Server or activity logs showing proof that the customer accessed or downloaded the purchased digital product after making the payment. Ideally include IP addresses, corresponding timestamps, and any detailed recorded activity.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `access_activity_log`                           |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - Device geographical location at the date and time of transaction
  - Device ID, number, and name (if applicable)
  - Evidence that the transaction was completed by a member of the cardholder’s family or household
  - Evidence of one or more non-disputed payments on the same card
  - Evidence that payments on the same card had been disputed as fraud prior to the issuer authorizing this transaction
  - Evidence that the card’s CVC value was presented at purchase, but the issuer either authorized the charge despite the check failing (`cvc_check` value of `fail`), or didn’t verify it in the first place (`cvc_check` value of `unchecked`)
  - Whether you already issued the refund the cardholder is entitled to
  - Whether the cardholder withdrew the dispute | `uncategorized_file` `uncategorized_text`       |

#### evidence you can submit for - Offline service

| For this type of recommended evidence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Designate this Dashboard label or API parameter                    |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Evidence (for example, photographs or emails) to prove a link between the person receiving the service and the cardholder, or proving that the cardholder disputing the transaction has used or is still using the service.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `customer_communication` `uncategorized_text` `uncategorized_file` |
| Evidence that the person who signed for the service was authorized to sign for—or is known by—the cardholder. Provide any of the following, if you have them:

  - Cardholder signature on the pickup form
  - A copy of identification presented by the cardholder
  - Details of identification presented by the cardholder                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `customer_signature` `uncategorized_text` `uncategorized_file`     |
| Documentation showing that the service was provided to the cardholder, including the date that the cardholder received or began receiving the purchased service in a clear, human-readable format. This could include a copy of a signed contract, work order, or other form of written agreement.

  For passenger transportation or services or travel and expense transactions, evidence that the service was provided and any of the following:

  - Proof that the ticket was received at the cardholder’s billing address
  - Evidence of payments related to the disputed payment, such as seat upgrades, extra baggage, and purchases made on board the passenger transport
  - Details of loyalty program rewards earned or redeemed, including address and phone number, that establish a link to the cardholder
  - Evidence that other payments related to the original payment, like upgrades, weren’t disputed                                                                                                             | `service_date` `service_documentation`                             |
| Any argument invalidating the dispute reason, such as a PDF or screenshot showing:

  - A signed order form for products purchased by mail or phone order
  - Evidence that the transaction was completed by a member of the cardholder’s family or household
  - Evidence of one or more non-disputed payments on the same card
  - Evidence that payments on the same card had been disputed as fraud prior to the issuer authorizing this transaction
  - Evidence that the card’s CVC value was presented at purchase, but the issuer either authorized the charge despite the check failing (`cvc_check` value of `fail`), or didn’t verify it in the first place (`cvc_check` value of `unchecked`)
  - For recurring payments, evidence of a legally binding contract held between your business and the cardholder, that the cardholder is using the products, and of any previous payments not disputed
  - Whether you already issued the refund the cardholder is entitled to
  - Whether the cardholder withdrew the dispute | `uncategorized_file` `uncategorized_text`                          |

#### Noncompliant

Businesses receive Visa compliance disputes in certain cases when the card issuer believes the disputed transaction doesn’t conform to Visa’s network rules. If Visa compliance disputes can’t be resolved between the parties, the dispute is resolved by the network in exchange for a fee.

If you contest a Visa compliance dispute, in addition to the applicable Stripe dispute fees, Stripe collects a 500 USD (or local equivalent) amount to cover the network costs associated with resolving Visa compliance disputes. Stripe refunds the 500 USD network fee if you win the dispute. Learn how to [respond to Visa compliance disputes using the API](https://docs.stripe.com/disputes/api/visa-compliance.md).

> Compliance cases filed by issuers are referred to as pre-compliance disputes by Visa. Learn more about [Visa rules](https://usa.visa.com/content/dam/VCOM/download/about-visa/visa-rules-public.pdf).

## See also

- [Understand fraud](https://docs.stripe.com/disputes/prevention.md)
