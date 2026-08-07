# Stripe Customer Support RAG Bot

A locally-run AI chatbot built with Streamlit and Azure OpenAI that answers Stripe-related support questions using a RAG (Retrieval-Augmented Generation) pipeline over 30 Stripe documentation files.

---

## What It Does

- **RAG Pipeline** - 30 Stripe docs (Markdown + PDF) are chunked, embedded, and stored in an Azure vector store. Every user question retrieves the most relevant docs before generating an answer.
- **Concise, actionable answers** - 2–4 sentence responses with exact steps, timelines, and next actions (e.g. "Go to Stripe Dashboard > Payments > Disputes").
- **Clickable source citations** - Each answer links directly to the relevant Stripe documentation pages.
- **Confidence-based escalation** - The model scores its confidence (HIGH / MEDIUM / LOW) internally. If LOW or MEDIUM, the user is shown Stripe's real support links:
  - 💬 Live Chat & Email → https://support.stripe.com/contact
  - 📖 Stripe Help Center → https://support.stripe.com
  - 🏦 Stripe Dashboard Support → https://dashboard.stripe.com/support
- **Empathetic tone** - Detects frustrated or distressed language ("still waiting", "it's been weeks", "unacceptable") and opens with: *"I'm really sorry to hear that, I understand how stressful this must be."*
- **Gibberish detection** - If the input is random characters or unintelligible, responds with: *"I didn't quite understand that - could you please retype your question?"*
- **Out-of-scope handling** - Refuses non-Stripe questions with: *"I'm Stripe's customer support bot, so I'm only able to help with Stripe-related questions. For this one, you'll likely find a great answer with a quick internet search!"*
- **Stripe-branded UI** - White background, Stripe wordmark top-left, orange→pink→purple gradient, centered input on load.

---

## RAG Architecture

```
User Question
     ↓
Azure Vector Store (30 Stripe docs, embedded with text-embedding-ada-002)
     ↓ file_search retrieval
Top relevant chunks
     ↓ augmented into prompt
gpt-4.1-mini → Answer + Confidence score
     ↓
Streamlit UI (answer + citations + escalation if needed)
```

---

## Setup

### 1. Create a Project Folder

```bash
mkdir stripe-rag-chatbot
cd stripe-rag-chatbot
```

### 2. Clone the Repo

```bash
git clone https://github.com/DRJohnson21/Stripe-Customer-Support-RAG-Bot
cd Stripe-Customer-Support-RAG-Bot
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it:

- **Mac/Linux:** `source .venv/bin/activate`
- **Windows:** `.venv\Scripts\Activate.ps1`

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create the `.env` File

Copy `.env.template` to `.env` and fill in your Azure OpenAI values:

```env
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_DEPLOYMENT=gpt-4.1-mini
AZURE_OPENAI_API_VERSION=2025-03-01-preview
AZURE_OPENAI_VECTOR_STORE_ID=your_vector_store_id
```

> ⚠️ Never commit `.env` to GitHub. It is already in `.gitignore`.

### 6. Upload Knowledge Base & Create Vector Store

If you need to set up your own vector store, run the upload script:

```bash
python upload_knowledge_base.py
```

This will:
1. Upload all `.md` and `.pdf` files from your knowledge base folder to Azure
2. Create a new vector store named `stripe-docs-index`
3. Index all 30 files
4. Print the vector store ID - add it to your `.env` as `AZURE_OPENAI_VECTOR_STORE_ID`

> You will need `gpt-4.1-mini` and `text-embedding-ada-002` deployed on your Azure OpenAI resource.

### 7. Run the Chatbot

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

### 8. Stop the Chatbot

```
Ctrl + C
```

---

## Azure Requirements

| Resource | Model |
|---|---|
| Chat | `gpt-4.1-mini` |
| Embeddings | `text-embedding-ada-002` |
| API Version | `2025-03-01-preview` |

---

## Notes

- The `.env` file must be in the same folder as `app.py`.
- Do not commit `.env` - only `.env.template` belongs in the repo.
- The `upload_knowledge_base.py` script only needs to be run once per Azure resource to set up the vector store.
