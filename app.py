import os
import re
import streamlit as st
from dotenv import load_dotenv
from openai import AzureOpenAI
from system_prompt import SYSTEM_PROMPT

load_dotenv()

CITATION_URLS = {
    "balance.md": ("Customer Invoice Balance", "https://docs.stripe.com/billing/customer/balance"),
    "best-practices.md": ("Dispute Evidence Best Practices", "https://docs.stripe.com/disputes/best-practices"),
    "billing_overview.md": ("How Subscriptions Work", "https://docs.stripe.com/billing/subscriptions/overview"),
    "cancel.md": ("Cancel Subscriptions", "https://docs.stripe.com/billing/subscriptions/cancel"),
    "categories.md": ("Dispute Reason Code Categories", "https://docs.stripe.com/disputes/categories"),
    "change-price.md": ("Change Subscription Price", "https://docs.stripe.com/billing/subscriptions/change-price"),
    "change.md": ("Modify Subscriptions", "https://docs.stripe.com/billing/subscriptions/change"),
    "customer.md": ("Customers", "https://docs.stripe.com/billing/customer"),
    "error-codes.md": ("Error Codes", "https://docs.stripe.com/error-codes"),
    "handling-payment-events.md": ("Handle Payment Events with Webhooks", "https://docs.stripe.com/payments/handling-payment-events"),
    "how-disputes-work.md": ("How Disputes Work", "https://docs.stripe.com/disputes/how-disputes-work"),
    "instant-payouts-banks.md": ("Institution Support for Instant Payouts", "https://docs.stripe.com/payouts/instant-payouts-banks"),
    "instant-payouts.md": ("Instant Payouts", "https://docs.stripe.com/payouts/instant-payouts"),
    "next-day-settlement.md": ("Next-Day Settlement", "https://docs.stripe.com/payouts/next-day-settlement"),
    "overview_invoicing.md": ("How Invoicing Works", "https://docs.stripe.com/invoicing/overview"),
    "pause.md": ("Pause Subscriptions", "https://docs.stripe.com/billing/subscriptions/pause"),
    "payouts.md": ("Receive Payouts", "https://docs.stripe.com/payouts"),
    "pending-updates.md": ("Pending Updates", "https://docs.stripe.com/billing/subscriptions/pending-updates"),
    "prebilling.md": ("Bill Customers in Advance", "https://docs.stripe.com/billing/subscriptions/prebilling"),
    "prevention-preview.md": ("Dispute Prevention", "https://docs.stripe.com/disputes/prevention"),
    "process-undelivered-events.md": ("Process Undelivered Webhook Events", "https://docs.stripe.com/webhooks/process-undelivered-events"),
    "prorations.md": ("Prorations", "https://docs.stripe.com/billing/subscriptions/prorations"),
    "refunds.md": ("Refund and Cancel Payments", "https://docs.stripe.com/refunds"),
    "signature.md": ("Webhook Signature Verification", "https://docs.stripe.com/webhooks/signature"),
    "subscription.md": ("Subscription Invoices", "https://docs.stripe.com/invoicing/subscription"),
    "trace-id.md": ("Payout Trace IDs", "https://docs.stripe.com/payouts/payout-reconciliation/trace-id"),
    "visa-compliance.md": ("Visa Compliance Disputes", "https://docs.stripe.com/disputes/visa-compliance"),
    "webhooks.md": ("Webhooks", "https://docs.stripe.com/webhooks"),
    "withdrawing.md": ("Dispute Withdrawals", "https://docs.stripe.com/disputes/withdrawing"),
    "FAQ for customers of businesses using Stripe _ Stripe_ Help & Support.pdf": ("Stripe FAQ", "https://support.stripe.com/questions/faq-for-customers-of-businesses-using-stripe"),
}


endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_API_KEY")
deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")
api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2025-03-01-preview")
vector_store_id = os.getenv("AZURE_OPENAI_VECTOR_STORE_ID")

st.set_page_config(page_title="Stripe Support", page_icon="💳", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

* { font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; }

/* White background */
.stApp { background-color: #ffffff; }

/* Gradient blob at bottom */
.stApp::before {
    content: '';
    position: fixed;
    bottom: 0; left: 0; right: 0;
    height: 55vh;
    background:
        radial-gradient(ellipse at 15% 100%, rgba(255,140,50,0.85) 0%, transparent 45%),
        radial-gradient(ellipse at 55% 90%, rgba(255,50,120,0.75) 0%, transparent 45%),
        radial-gradient(ellipse at 85% 70%, rgba(160,140,230,0.7) 0%, transparent 45%),
        radial-gradient(ellipse at 95% 95%, rgba(130,180,240,0.6) 0%, transparent 40%);
    z-index: 0;
    pointer-events: none;
}

/* Content above gradient */
.block-container {
    position: relative;
    z-index: 1;
    max-width: 680px;
    padding-top: 1.2rem;
    padding-bottom: 0.5rem;
}

/* Hide Streamlit chrome */
header[data-testid="stHeader"] { background: transparent; }
#MainMenu, footer { visibility: hidden; }

/* Stripe wordmark - fixed top left */
.stripe-top {
    position: fixed;
    top: 18px;
    left: 28px;
    z-index: 999;
}
.stripe-logo {
    font-size: 1.4rem;
    font-weight: 700;
    color: #0A2540;
    letter-spacing: -1px;
}

/* Disclaimer fixed at bottom */
.disclaimer {
    position: fixed !important;
    bottom: 14px;
    left: 0; right: 0;
    text-align: center;
    font-size: 0.75rem;
    color: #8898aa;
    z-index: 999;
}

/* Page title */
.stripe-title {
    text-align: center;
    font-size: 2rem;
    font-weight: 600;
    color: #0A2540;
    margin-bottom: 8px;
    line-height: 1.2;
}
.stripe-subtitle {
    text-align: center;
    font-size: 0.95rem;
    color: #425466;
    margin-bottom: 28px;
}

/* Force textarea white */
textarea, .stTextArea textarea, div[data-testid="stForm"] textarea {
    background-color: white !important;
    color: #0A2540 !important;
    border: none !important;
    box-shadow: none !important;
    font-size: 1rem !important;
    resize: none !important;
}

/* Chat messages */
[data-testid="stChatMessage"] {
    background: rgba(255,255,255,0.85) !important;
    border: 1px solid rgba(0,0,0,0.08) !important;
    border-radius: 12px !important;
    margin-bottom: 8px;
    backdrop-filter: blur(8px);
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li { color: #0A2540 !important; }

/* User message */
[data-testid="stChatMessage"]:has([data-testid="stChatMessageAvatarUser"]) {
    background: rgba(99,91,255,0.06) !important;
    border-color: rgba(99,91,255,0.15) !important;
}

/* Chat input */
[data-testid="stBottom"] {
    background: transparent !important;
    padding-top: 8px !important;
}
[data-testid="stChatInput"] textarea {
    background: white !important;
    border: 1px solid rgba(0,0,0,0.12) !important;
    border-radius: 10px !important;
    color: #0A2540 !important;
    font-size: 0.95rem !important;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06) !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: #8898aa !important; }
[data-testid="stChatInput"] textarea:focus {
    border-color: #635BFF !important;
    box-shadow: 0 0 0 3px rgba(99,91,255,0.12) !important;
}

/* Warning / escalation */
[data-testid="stAlert"] {
    background: rgba(255,255,255,0.8) !important;
    border: 1px solid rgba(99,91,255,0.25) !important;
    border-left: 3px solid #635BFF !important;
    border-radius: 10px !important;
    backdrop-filter: blur(8px);
}
[data-testid="stAlert"] p, [data-testid="stAlert"] a { color: #0A2540 !important; }

/* Captions / sources */
.stCaption { color: #697386 !important; font-size: 0.76rem !important; }
.stCaption a { color: #635BFF !important; text-decoration: none !important; }
.stCaption a:hover { text-decoration: underline !important; }
</style>

<div class="stripe-top">
    <span class="stripe-logo">stripe</span>
</div>
<div class="disclaimer">By messaging, you understand this is an AI assistant powered by Stripe documentation.</div>
<div class="stripe-title">How can we help you today?</div>
<div class="stripe-subtitle">This is Stripe's Customer Support Bot — Ask me anything about payments, refunds, billing, disputes, and more.</div>
""", unsafe_allow_html=True)

if not endpoint or not api_key or not deployment:
    st.error("Missing Azure OpenAI settings. Check your .env file.")
    st.stop()

client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version=api_version,
)

if "messages" not in st.session_state:
    st.session_state.messages = []

def render_citations(citations):
    if citations:
        links = []
        for c in citations:
            if c in CITATION_URLS:
                label, url = CITATION_URLS[c]
                links.append(f"[{label}]({url})")
            else:
                links.append(c)
        st.caption("📄 Sources: " + " · ".join(links))

def render_escalation(confidence):
    if confidence in ("LOW", "MEDIUM"):
        st.warning(
            "Need more help? Contact Stripe Support directly:\n\n"
            "💬 [Live Chat & Email](https://support.stripe.com/contact) · "
            "📖 [Stripe Help Center](https://support.stripe.com) · "
            "🏦 [Stripe Dashboard Support](https://dashboard.stripe.com/support)"
        )

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant":
            render_escalation(message.get("confidence"))
            render_citations(message.get("citations"))

# Centered input when no messages, bottom input when conversation is active
if not st.session_state.messages:
    st.markdown("""
    <style>
    /* Push content down to vertically center the input */
    .center-input-wrap { margin-top: 8vh; }
    div[data-testid="stForm"] {
        background: white;
        border: 1px solid rgba(0,0,0,0.10);
        border-radius: 12px;
        padding: 4px 8px 4px 16px;
        box-shadow: 0 2px 12px rgba(0,0,0,0.07);
    }
    div[data-testid="stForm"] textarea {
        border: none !important;
        box-shadow: none !important;
        font-size: 1rem !important;
        color: #0A2540 !important;
        resize: none;
    }
    div[data-testid="stForm"] button {
        background: #635BFF !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 6px 20px !important;
        font-weight: 500 !important;
    }
    .disclaimer { text-align: center; font-size: 0.75rem; color: #8898aa; margin-top: 12px; }
    </style>
    <div class="center-input-wrap"></div>
    """, unsafe_allow_html=True)

    with st.form("initial_input", clear_on_submit=True):
        user_input = st.text_area("", placeholder="Ask a Stripe support question...", height=100, label_visibility="collapsed")
        submitted = st.form_submit_button("→  Send")
    user_input = user_input.strip() if submitted and user_input.strip() else None

else:
    user_input = st.chat_input("Ask a Stripe support question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                input_messages = [{"role": "system", "content": SYSTEM_PROMPT}]
                for msg in st.session_state.messages:
                    input_messages.append({"role": msg["role"], "content": msg["content"]})

                response = client.responses.create(
                    model=deployment,
                    input=input_messages,
                    tools=[{
                        "type": "file_search",
                        "vector_store_ids": [vector_store_id],
                    }],
                    temperature=0.2,
                    max_output_tokens=500,
                    include=["file_search_call.results"],
                )

                # Debug: print response output structure to terminal
                for item in response.output:
                    print(f"[DEBUG] output type: {item.type}, keys: {vars(item).keys()}")
                    if item.type == "file_search_call":
                        results = getattr(item, "results", None)
                        print(f"[DEBUG] file_search results: {results}")
                        if results:
                            print(f"[DEBUG] first result attrs: {vars(results[0])}")

                # Clean citation markers from answer
                raw_text = response.output_text
                bot_reply = re.sub(r'【\d+:[^】]+】', '', raw_text).strip()

                # Extract confidence from answer (model appends CONFIDENCE: HIGH/MEDIUM/LOW)
                confidence = None
                confidence_match = re.search(r'CONFIDENCE:\s*(HIGH|MEDIUM|LOW)', bot_reply, re.IGNORECASE)
                if confidence_match:
                    confidence = confidence_match.group(1).upper()
                    bot_reply = re.sub(r'\s*CONFIDENCE:\s*(HIGH|MEDIUM|LOW)', '', bot_reply, flags=re.IGNORECASE).strip()

                # Extract citations from file_search_call results
                citations = []
                for item in response.output:
                    if item.type == "file_search_call":
                        results = getattr(item, "results", None) or []
                        for result in results:
                            # Try all possible attribute names
                            filename = (
                                getattr(result, "file_name", None) or
                                getattr(result, "filename", None) or
                                getattr(result, "name", None)
                            )
                            if filename and filename not in citations:
                                citations.append(filename)

                st.markdown(bot_reply)
                render_escalation(confidence)
                render_citations(citations)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": bot_reply,
                    "confidence": confidence,
                    "citations": citations,
                })

            except Exception as e:
                st.error(f"Error: {e}")
