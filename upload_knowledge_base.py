import os
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT", "").rstrip("/")
API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION", "2025-03-01-preview")
KNOWLEDGE_BASE_PATH = Path(os.getenv("KNOWLEDGE_BASE_PATH", "./knowledge-base"))

if not ENDPOINT or not API_KEY:
    raise ValueError("Missing AZURE_OPENAI_ENDPOINT or AZURE_OPENAI_API_KEY in .env")

headers = {"api-key": API_KEY}

# Step 1: Upload files
print("Uploading files...")
file_ids = []
for file_path in sorted(KNOWLEDGE_BASE_PATH.iterdir()):
    if file_path.is_file() and file_path.suffix in (".md", ".pdf"):
        print(f"  Uploading {file_path.name}...")
        with open(file_path, "rb") as f:
            response = requests.post(
                f"{ENDPOINT}/openai/files?api-version={API_VERSION}",
                headers={"api-key": API_KEY},
                files={"file": (file_path.name, f, "text/plain")},
                data={"purpose": "assistants"}
            )
        response.raise_for_status()
        file_id = response.json()["id"]
        file_ids.append(file_id)
        print(f"    -> {file_id}")

print(f"\nUploaded {len(file_ids)} files.")

# Step 2: Create vector store
print("\nCreating vector store...")
response = requests.post(
    f"{ENDPOINT}/openai/vector_stores?api-version={API_VERSION}",
    headers={**headers, "Content-Type": "application/json"},
    json={"name": "stripe-docs-index"}
)
response.raise_for_status()
vector_store_id = response.json()["id"]
print(f"Vector store created: {vector_store_id}")

# Step 3: Add files to vector store
print("\nIndexing files into vector store...")
response = requests.post(
    f"{ENDPOINT}/openai/vector_stores/{vector_store_id}/file_batches?api-version={API_VERSION}",
    headers={**headers, "Content-Type": "application/json"},
    json={"file_ids": file_ids}
)
response.raise_for_status()
batch_id = response.json()["id"]

# Poll until done
while True:
    r = requests.get(
        f"{ENDPOINT}/openai/vector_stores/{vector_store_id}/file_batches/{batch_id}?api-version={API_VERSION}",
        headers=headers
    )
    r.raise_for_status()
    status = r.json()["status"]
    counts = r.json().get("file_counts", {})
    print(f"  Status: {status} | {counts}")
    if status in ("completed", "failed", "cancelled"):
        break
    time.sleep(3)

print(f"\n✅ Done!")
print(f"\nAdd this to your .env file:")
print(f"AZURE_OPENAI_VECTOR_STORE_ID={vector_store_id}")
