import os
from openai import OpenAI
from dotenv import load_dotenv

# --- Load NVIDIA API key from your .env file ---
load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")

if not api_key:
    raise RuntimeError("⚠️  Set NVIDIA_API_KEY in your .env file")

# --- Initialize client for Mini-4B ---
NIM_BASE_URL = "https://integrate.api.nvidia.com/v1"
MODEL_ID = "nvidia/nemotron-mini-4b-instruct"

client = OpenAI(api_key=api_key, base_url=NIM_BASE_URL)

# --- Define prompt for Mini-4B ---
messages = [
    {
        "role": "system",
        "content": "You are an intelligent assistant that helps product managers organize ideas, summarize discussions, and generate structured tasks."
    },
    {
        "role": "user",
        "content": (
            "From the following project update, summarize the key points "
            "and create 2 prioritized JIRA-style tickets.\n\n"
            "Update: The login page crashes when users enter special characters "
            "in the password field. The design team also mentioned adding a new "
            "animation for the signup flow."
        )
    },
]

# --- Send the request ---
print(f"Sending prompt to model {MODEL_ID}...\n")
response = client.chat.completions.create(
    model=MODEL_ID,
    messages=messages,
    temperature=0.3,
    max_tokens=400,
)

# --- Display result ---
print("✅ Response:\n")
print(response.choices[0].message.content)
