# Stripe Customer Support RAG Bot

An AI-powered customer support assistant that answers Stripe-related questions using retrieval-augmented generation (RAG). The app retrieves relevant content from a Stripe documentation knowledge base, generates a concise response with Azure OpenAI, cites the supporting sources, and directs uncertain or sensitive cases to Stripe Support.

> [!IMPORTANT]
> This is an independent demo project and is not affiliated with, endorsed by, or operated by Stripe. Do not enter card numbers, API keys, passwords, or other sensitive information into the chat.

## Features

- Retrieval over a curated Stripe documentation knowledge base
- Support for payments, refunds, billing, subscriptions, invoices, payouts, disputes, error codes, and webhooks
- Concise, actionable responses with relevant Stripe documentation links
- Confidence-based escalation to official Stripe support channels
- Out-of-scope and unintelligible-input handling
- Conversation history during the active Streamlit session
- Stripe-inspired responsive interface

## How It Works

```text
User question
     │
     ▼
Azure OpenAI file search ──► Vector store containing Stripe documentation
     │
     ▼
Relevant document chunks
     │
     ▼
Azure OpenAI response generation
     │
     ▼
Answer + confidence level + source links
     │
     ▼
Streamlit chat interface
```

The application sends the conversation and system instructions to the Azure OpenAI Responses API. The `file_search` tool retrieves relevant documents from the configured vector store. The app then removes internal citation markers, displays mapped source links, and offers official support options for medium- or low-confidence answers.

## Tech Stack

- Python
- Streamlit
- Azure OpenAI Responses API
- Azure OpenAI vector stores and file search
- python-dotenv

## Project Structure

```text
Stripe-Customer-Support-RAG-Bot-main/
├── knowledge-base/             # Stripe documentation used for retrieval
├── app.py                      # Streamlit UI and RAG workflow
├── system_prompt.py            # Support-agent behavior and safety rules
├── upload_knowledge_base.py    # Uploads and indexes the knowledge base
├── requirements.txt            # Python dependencies
└── README.md
```

## Prerequisites

Before running the project, you need:

- Python 3.10 or newer
- An Azure OpenAI resource
- A deployed chat model compatible with the Responses API and file search
- Your Azure OpenAI endpoint and API key

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MadhuDamani12/Stripe-Bot-.git
cd Stripe-Bot-/Stripe-Customer-Support-RAG-Bot-main
```

### 2. Create and activate a virtual environment

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt requests
```

`requests` is required by `upload_knowledge_base.py` but is not currently listed in `requirements.txt`.

### 4. Configure environment variables

Create a `.env` file in the same directory as `app.py`:

```dotenv
AZURE_OPENAI_ENDPOINT=https://YOUR-RESOURCE-NAME.openai.azure.com
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_DEPLOYMENT=your_chat_model_deployment_name
AZURE_OPENAI_API_VERSION=2025-03-01-preview
AZURE_OPENAI_VECTOR_STORE_ID=your_vector_store_id
```

Optional:

```dotenv
KNOWLEDGE_BASE_PATH=./knowledge-base
```

> [!WARNING]
> Never commit `.env` or expose your Azure credentials. Add `.env` and `.venv/` to `.gitignore` before committing local changes.

### 5. Create the vector store

Run the upload script once to upload the Markdown and PDF files from `knowledge-base/` and create the vector store:

```bash
python upload_knowledge_base.py
```

When indexing finishes, the script prints a value similar to:

```text
AZURE_OPENAI_VECTOR_STORE_ID=vs_...
```

Copy that value into your `.env` file. Re-running the script creates another vector store and uploads the files again.

### 6. Start the app

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) if Streamlit does not launch it automatically.

## Example Questions

- How long does a Stripe refund take?
- Why is my payout still pending?
- How do I cancel a subscription?
- Where can I find webhook signing secrets?
- What evidence should I submit for a dispute?

## Configuration Reference

| Variable | Required | Description |
| --- | --- | --- |
| `AZURE_OPENAI_ENDPOINT` | Yes | Base URL for the Azure OpenAI resource |
| `AZURE_OPENAI_API_KEY` | Yes | API key for the Azure OpenAI resource |
| `AZURE_OPENAI_DEPLOYMENT` | Yes | Name of the deployed chat model |
| `AZURE_OPENAI_API_VERSION` | No | Azure API version; defaults to `2025-03-01-preview` |
| `AZURE_OPENAI_VECTOR_STORE_ID` | Yes | ID of the vector store searched by the app |
| `KNOWLEDGE_BASE_PATH` | No | Knowledge-base directory used by the upload script; defaults to `./knowledge-base` |

## Troubleshooting

### `Missing Azure OpenAI settings`

Confirm that `.env` is next to `app.py`, contains the required variables, and has no extra quotes around the values. Restart Streamlit after changing it.

### `ModuleNotFoundError: No module named 'requests'`

Install the upload script's HTTP dependency:

```bash
pip install requests
```

### File search or vector store errors

Verify that `AZURE_OPENAI_VECTOR_STORE_ID` contains the ID printed by `upload_knowledge_base.py`, and that the vector-store indexing status completed successfully.

### No source links appear

The UI maps retrieved filenames to URLs defined in `CITATION_URLS` inside `app.py`. A source whose filename is not in that mapping is shown as plain text.

## Limitations

- The assistant only covers the Stripe topics represented in the included knowledge base.
- Responses may be incomplete or incorrect and should not replace official Stripe support.
- Chat history is stored only in the active Streamlit session.
- Escalation displays official support links; it does not create a support ticket automatically.
- The included documentation can become outdated as Stripe products and policies change.

## Security

- Keep `.env` and all credentials out of version control.
- Do not collect or submit cardholder data through this demo.
- Rotate any credential that has been accidentally committed.
- Review Azure usage, access controls, logging, and data-retention settings before production deployment.

## Contributing

Contributions are welcome. Open an issue or submit a pull request with a clear description of the proposed change. When updating the knowledge base, use current Stripe documentation and verify that the corresponding citation URL is present in `app.py`.

## Acknowledgments

- [Stripe Documentation](https://docs.stripe.com/)
- [Stripe Support](https://support.stripe.com/)
- [Streamlit](https://streamlit.io/)
- [Azure OpenAI](https://azure.microsoft.com/products/ai-services/openai-service)
