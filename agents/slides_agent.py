"""
slides_agent.py
---------------
Extracts text from a Google Slides presentation and summarizes it using
NVIDIA’s Nemotron model for concise insights.

Supports multiple analysis modes:
- summary  → overview and insights
- stats    → extract all numerical and metric data
- topics   → list and describe major topics
"""

from google.oauth2 import service_account
from googleapiclient.discovery import build
from dotenv import load_dotenv
from openai import OpenAI
import traceback
import re
import os

# ===========================================================
# 1. Load environment variables
# ===========================================================
load_dotenv()

# Validate API key and credentials
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
GOOGLE_CREDS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

if not NVIDIA_API_KEY:
    raise ValueError("❌ Missing NVIDIA_API_KEY — please add it to your .env file.")

# Fallback in case .env is missing the path
if not GOOGLE_CREDS or not os.path.exists(GOOGLE_CREDS):
    fallback = r"C:\Users\shah\Desktop\Academic Projects\HackUTDProject\credentials\slides-agent-service-key.json"
    print(f"⚠️ GOOGLE_APPLICATION_CREDENTIALS not valid. Falling back to: {fallback}")
    GOOGLE_CREDS = fallback


# ===========================================================
# 2. Initialize NVIDIA Nemotron client
# ===========================================================
client = OpenAI(
    api_key=NVIDIA_API_KEY,
    base_url="https://integrate.api.nvidia.com/v1"
)

MODEL_ID = "nvidia/llama-3.3-nemotron-super-49b-v1.5"


def nemotron_call(prompt: str, system_prompt: str = "You are a concise and analytical presentation summarizer.") -> str:
    """
    Sends text to NVIDIA Nemotron model for summarization or analysis.
    """
    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.4,
            max_tokens=800
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        tb = traceback.format_exc()
        return f"Nemotron API Error: {e}\n\nTraceback:\n{tb}"


# ===========================================================
# 3. Extract text from Google Slides
# ===========================================================
def extract_slides_text(presentation_url: str) -> str:
    """
    Extracts all text content from a Google Slides presentation.
    Requires a valid JSON service key with readonly access.
    """
    try:
        match = re.search(r"/presentation/d/([a-zA-Z0-9-_]+)", presentation_url)
        if not match:
            return "Invalid Google Slides link. Expected format: https://docs.google.com/presentation/d/<ID>/edit"
        presentation_id = match.group(1)

        abs_creds_path = os.path.abspath(GOOGLE_CREDS)
        if not os.path.exists(abs_creds_path):
            return f"Credentials file not found at {abs_creds_path}"

        # --- Authenticate and load the presentation ---
        credentials = service_account.Credentials.from_service_account_file(
            abs_creds_path,
            scopes=["https://www.googleapis.com/auth/presentations.readonly"]
        )
        service = build("slides", "v1", credentials=credentials)
        presentation = service.presentations().get(presentationId=presentation_id).execute()

        # --- Extract slide titles and text ---
        text_content = []
        for idx, slide in enumerate(presentation.get("slides", []), start=1):
            text_content.append(f"\n--- Slide {idx} ---")
            for element in slide.get("pageElements", []):
                shape = element.get("shape")
                if shape and "textElements" in shape.get("text", {}):
                    for te in shape["text"]["textElements"]:
                        if "textRun" in te:
                            content = te["textRun"]["content"].strip()
                            if content:
                                text_content.append(content)

        if not text_content:
            return "No text content found in this presentation."

        return "\n".join(text_content)

    except Exception as e:
        tb = traceback.format_exc()
        return f"Error reading Google Slides: {e}\n\nTraceback:\n{tb}"


# ===========================================================
# 4. Analyze slide content using Nemotron
# ===========================================================
def analyze_slides(presentation_url: str, mode: str = "summary") -> str:
    """
    Combines text extraction and Nemotron analysis for a presentation.
    Modes:
        summary → overview, insights, and breakdown
        stats   → extract all metrics and numbers
        topics  → list and describe major topics
    """
    print("📊 Extracting slide content...")
    slide_text = extract_slides_text(presentation_url)

    if "Error" in slide_text or "Invalid" in slide_text:
        return slide_text

    # Prevent overly long payloads
    if len(slide_text) > 12000:
        slide_text = slide_text[:12000] + "\n\n[Content truncated for analysis...]"

    print("🤖 Analyzing with NVIDIA Nemotron...")

    # --- Dynamic prompt selection ---
    if mode == "summary":
        analysis_prompt = (
            f"Analyze and summarize the following Google Slides content:\n\n{slide_text}\n\n"
            f"Provide:\n"
            f"- A short summary of the key topics\n"
            f"- Any actionable insights or conclusions\n"
            f"- A structured breakdown (bullet points)\n"
            f"Be factual and concise."
        )
    elif mode == "stats":
        analysis_prompt = (
            f"From the following slides, extract all quantitative and statistical data:\n\n{slide_text}\n\n"
            f"List key numbers, growth rates, trends, and relevant metrics with explanations."
        )
    elif mode == "topics":
        analysis_prompt = (
            f"Identify the main topics and subtopics discussed in the following slides:\n\n{slide_text}\n\n"
            f"Organize your response hierarchically by topic and subtopic."
        )
    else:
        return f"Invalid analysis mode: {mode}. Valid modes are: summary, stats, topics."

    return nemotron_call(analysis_prompt)


# ===========================================================
# 5. Manual test runner
# ===========================================================
if __name__ == "__main__":
    print("Google Slides Agent — Analyzer\n")
    test_url = input("Enter Google Slides link: ").strip()
    print("\nSelect analysis mode:")
    print("1. Summary (default)")
    print("2. Stats only")
    print("3. Topics overview")
    mode_choice = input("Enter 1, 2, or 3: ").strip()
    mode = "summary" if mode_choice == "1" or not mode_choice else \
           "stats" if mode_choice == "2" else \
           "topics" if mode_choice == "3" else "summary"

    print(f"\n🔍 Extracting and analyzing slides in '{mode}' mode...\n")
    output = analyze_slides(test_url, mode=mode)
    print("\n🧠 Final Analysis:\n")
    print(output)



# ===========================================================
# 5. Manual test block
# ===========================================================
if __name__ == "__main__":
    print("Google Slides Agent — Analyzer\n")
    test_url = input("Enter Google Slides link: ").strip()
    print("\nExtracting and analyzing slides...\n")
    output = analyze_slides(test_url)
    print("\n🧠 Final Analysis:\n")
    print(output)
