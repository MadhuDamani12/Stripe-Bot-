# Handle payment events with webhooks

How to use webhooks to respond to offline payment events.

A *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) is an HTTP endpoint that receives events from Stripe.

Webhooks allow you to be notified about payment events that happen outside of your payment flow such as:

- Successful payments (`payment_intent.succeeded`)
- Disputed payments (`charge.dispute.created`)
- Available balance in your Stripe account (`balance.available`)

You can use the Dashboard for one-off actions like refunding a payment or updating a customer’s information, while webhooks help you scale your payments integration and process large volumes of business-critical events.

## Build your own webhook

You can build a webhook handler on your own server to manage all your offline payment flows. Start by exposing an endpoint that can receive requests from Stripe and use the CLI to locally test your integration. Each request from Stripe contains an [Event](https://docs.stripe.com/api/events/object.md) object with a reference to the object on Stripe that was modified.

## Create a webhook endpoint

Add a new endpoint in your application. You can act on certain events by checking the `type` field of the event object sent in the request body. Then you can print to standard output to make sure your webhook is working.

Start your server after adding the new endpoint.

#### Ruby

```ruby

# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
# Find your keys at https://dashboard.stripe.com/apikeys.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')

require 'stripe'
require 'sinatra'
require 'json'

# Using the Sinatra framework
set :port, 4242

post '/webhook' do
  payload = request.body.read
  event = nil

  begin
    event = Stripe::Event.construct_from(
      JSON.parse(payload, symbolize_names: true)
    )
  rescue JSON::ParserError => e
    # Invalid payload
    status 400
    return
  end

  # Handle the event
  case event.type
  when 'payment_intent.succeeded'
    payment_intent = event.data.object # contains a Stripe::PaymentIntent
    puts 'PaymentIntent was successful!'
  when 'payment_method.attached'
    payment_method = event.data.object # contains a Stripe::PaymentMethod
    puts 'PaymentMethod was attached to a Customer!'
  # ... handle other event types
  else
    puts "Unhandled event type: #{event.type}"
  end

  status 200
end
```

## Install and set up the Stripe CLI
For additional install options, see [Get started with the Stripe CLI](https://docs.stripe.com/stripe-cli.md).
After you have the Stripe CLI installed, run `stripe login` in the command line to generate a pairing code to link to your Stripe account. Press **Enter** to launch your browser and log in to your Stripe account to allow access. The generated API key is valid for 90 days. You can modify or delete the key under [API Keys](https://dashboard.stripe.com/apikeys) in the Dashboard.

> You can create a project-specific configuration by including the [–project-name](https://docs.stripe.com/cli/login#login-project-name) flag when you log in and when you run commands for that project.

Test

```bash
stripe login
Your pairing code is: humour-nifty-finer-magic
Press Enter to open up the browser (^C to quit)
```

If you want to use an existing API key, use the `--api-key` flag:

```bash
stripe login --api-key <<YOUR_SECRET_KEY>>
Your pairing code is: humour-nifty-finer-magic
Press Enter to open up the browser (^C to quit)
```

## Test your webhook locally

Use the CLI to forward events to your local webhook endpoint using the `listen` command.

Assuming your application is running on port 4242, run:

```bash
stripe listen --forward-to http://localhost:4242/webhook
```

In a different terminal tab, use the `trigger` CLI command to trigger a mock webhook event.

```bash
stripe trigger payment_intent.succeeded
```

The following event appears in your `listen` tab:

```bash
[200 POST] OK payment_intent.succeeded
```

“PaymentIntent was successful!” appears in the terminal tab your server is running.

## Optional: Check webhook signature

Stripe includes a signature in each event’s `Stripe-Signature` header. This allows you to verify that the events were sent by Stripe, and not by a third party. You can verify signatures either using our official libraries, or [verify signatures manually](https://docs.stripe.com/webhooks.md#verify-manually) using your own solution.

First, find your webhook endpoint secret and add it to your webhook handler as `endpoint_secret`. Because you’re still using the Stripe CLI to develop your endpoint locally, use the `trigger` command to get the webhook endpoint secret from the CLI.

```bash
stripe listen
```

The webhook endpoint secret starts with `whsec_` followed by a series of numbers and letters. Keep this webhook endpoint secret safe and never expose it publicly.

#### Ruby

```ruby

# Don't put any keys in code. See https://docs.stripe.com/keys-best-practices.
# Find your keys at https://dashboard.stripe.com/apikeys.
client = Stripe::StripeClient.new('<<YOUR_SECRET_KEY>>')

require 'stripe'
require 'sinatra'

# If you are testing your webhook locally with the Stripe CLI you
# can find the endpoint's secret by running `stripe listen`
# Otherwise, find your endpoint's secret in your webhook settings in
# the Developer Dashboardendpoint_secret = 'whsec_...'

# Using the Sinatra framework
set :port, 4242

post '/my/webhook/url' do
  payload = request.body.readsig_header = request.env['HTTP_STRIPE_SIGNATURE']
  event = nil

  beginevent = Stripe::Webhook.construct_event(
      payload, sig_header, endpoint_secret
    )
  rescue JSON::ParserError => e
    # Invalid payload
    puts "Error parsing payload: #{e.message}"
    status 400
    return
  rescue Stripe::SignatureVerificationError => e# Invalid signature
    puts "Error verifying webhook signature: #{e.message}"
    status 400
    return
  end

  # Handle the event
  case event.type
  when 'payment_intent.succeeded'
    payment_intent = event.data.object # contains a Stripe::PaymentIntent
    puts 'PaymentIntent was successful!'
  when 'payment_method.attached'
    payment_method = event.data.object # contains a Stripe::PaymentMethod
    puts 'PaymentMethod was attached to a Customer!'
  # ... handle other event types
  else
    puts "Unhandled event type: #{event.type}"
  end

  status 200
end
```

## Deploy your webhook endpoint

When you’re ready to deploy your webhook endpoint to production you need to do the following:

1. Use your [live mode API keys](https://docs.stripe.com/keys.md#test-live-modes) and not your test keys.
2. Configure your webhook endpoint in [Workbench](https://docs.stripe.com/workbench.md) or with the API.
3. To configure your endpoint in Workbench, go to the [Webhooks tab](https://dashboard.stripe.com/workbench/webhooks).
4. Click **Add destination** and enter the Stripe API version and the specific events you want Stripe to send. Click **Continue** and select **Webhook endpoint** from the list of available destination types. Click **Continue** and enter the URL of your endpoint, optional name, and optional description. Click **Create destination**.
5. Replace the webhook endpoint secret in your application with the new secret shown in the destination details view in Workbench for your endpoint.

Your application is now ready to accept live events. For more information on configuring your webhook endpoint, see the [Webhook Endpoint](https://docs.stripe.com/api/webhook_endpoints.md) API. For testing in a sandbox, [see our Development guide](https://docs.stripe.com/webhooks.md).
