# Dispute prevention

Automatically prevent disputes and lower your dispute rate.

Disputes, also known as chargebacks, can lead to significant costs. Dispute resolution and deflection help you save on these costs, reduce your dispute rates, and automate part of your dispute management process. To sign up for dispute prevention, go to your [Dispute settings](https://dashboard.stripe.com/settings/disputes).

Use dispute prevention to:

- Set resolution rules through [Stripe Radar](https://docs.stripe.com/radar/rules/disputes.md) to automatically resolve (refund) specific disputes. Resolved disputes don’t count towards your dispute rate and don’t incur a dispute received fee.
- Deflect disputes by sending extra transaction data with dispute deflection.
- Block disputes entirely if the extra transaction data provided with Order Insights is [Compelling Evidence (CE 3.0)](https://docs.stripe.com/disputes/get-started/prevention.md#compelling-evidence-30-with-oi) eligible.

You can review and manage dispute prevention from the Dashboard. Learn more about [disputes and fraud](https://docs.stripe.com/disputes.md).

## Benefits

Automatically resolving disputes can cost less than responding to certain disputes. If you’re part of the Visa Acquirer Monitoring Program (VAMP) or similar monitoring programs, then automatically resolving disputes can help you exit the program. Learn more about [monitoring programs](https://docs.stripe.com/disputes/monitoring-programs.md).

|  |
|  |
| ![Rate reduction using automatic rules.](https://b.stripecdn.com/docs-statics-srv/assets/verifi-lower-disputes.ea031da338e5a6479b0966e593ed2615.png) | ![Turn on dispute prevention in your dashboard.](https://b.stripecdn.com/docs-statics-srv/assets/verifi-zero-integration.8e2e9287f3217f1acb7faca32f71c24b.png) | ![Increased revenue retention.](https://b.stripecdn.com/docs-statics-srv/assets/verifi-lower-costs.37f379911d16ca5a4001844c661b0d06.png) |
| **Lower dispute rates**

  Automatically refunded disputes don’t count towards your dispute rate.                                                    | **No integration required**

  Stripe integrates directly with Verifi and provides your existing transaction data on your behalf at time of lookup.            | **Lower costs**

  Fewer disputes means fewer dispute fees and operational costs to counter disputes.                                    |

## Deflection

Dispute deflection uses your transaction data to help cardholders recognize the charge before they initiate a dispute. When eligible, adding Compelling Evidence 3.0 can block disputes entirely.
![The process of adding Order Insight and Compelling Evidence 3.0 to prevent disputes.](https://b.stripecdn.com/docs-statics-srv/assets/verifi-oi-diagram.21971b1eecb82c373982ee5e88abc4d2.png)

## Resolution

Automatically resolve disputes based on custom rules you set through the [Radar Dashboard](https://docs.stripe.com/radar/rules/disputes.md). Disputes caught and resolved by the rules you set through dispute resolution don’t count towards your overall dispute rate.
![The process of resolving disputes with no impact on your dispute rate for non fraud disputes.](https://b.stripecdn.com/docs-statics-srv/assets/prevention-resolution-diagram.56eb68feefaa1e0f4221c60b5918217e.png)

## Smart Disputes 

[Smart Disputes](https://docs.stripe.com/disputes/smart-disputes.md) automates evidence collection and submission for eligible card disputes. When you receive an eligible dispute, Stripe uses an AI rules engine to build a tailored evidence packet from your transaction data, cardholder data, and Stripe network data, then submits it automatically before the deadline.

Smart Disputes complements dispute prevention: dispute prevention tools reduce the number of disputes you receive, while Smart Disputes handles any that do come through. It automates the response process so you don’t miss deadlines or spend time manually assembling evidence.

## See also

- [How disputes work](https://docs.stripe.com/disputes/how-disputes-work.md)
- [Respond to disputes](https://docs.stripe.com/disputes/responding.md)
- [Manage disputes programmatically](https://docs.stripe.com/disputes/api.md)
