import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# -----------------------------
# 1. Load API Key
# -----------------------------
load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")

if not api_key:
    raise RuntimeError("⚠️  Set NVIDIA_API_KEY in your .env file")

# -----------------------------
# 2. Initialize NVIDIA Client
# -----------------------------
NIM_BASE_URL = "https://integrate.api.nvidia.com/v1"
MODEL_ID = "nvidia/nvidia-nemotron-nano-9b-v2"  # ✅ exact name from your list

client = OpenAI(api_key=api_key, base_url=NIM_BASE_URL)
print(f"🚀 Sending request to model {MODEL_ID}...\n")

# -----------------------------
# 3. Define Conversation
# -----------------------------
messages = [
    {
        "role": "system",
        "content": (
            "You are a reasoning model that helps product managers and interns "
            "collaborate better. Provide both reasoning and final answers."
        ),
    },
    {
        "role": "user",
        "content": (
            "We want to improve collaboration between product managers and interns. "
            "Suggest 3 ways AI can help make communication and progress tracking easier."
        ),
    },
]

# -----------------------------
# 4. Send Request
# -----------------------------
response = client.chat.completions.create(
    model=MODEL_ID,
    messages=messages,
    temperature=0.4,
    max_tokens=500,
)

# -----------------------------
# 5. Handle Output Gracefully
# -----------------------------
msg = response.choices[0].message

# Print Reasoning (if any)
if hasattr(msg, "reasoning_content") and msg.reasoning_content:
    print("🧩 REASONING:\n")
    print(msg.reasoning_content)
    print("\n" + "-" * 60)

# Print Final Answer (if any)
if msg.content:
    print("💡 FINAL ANSWER:\n")
    print(msg.content)
# Print Tool Calls (if applicable)
elif hasattr(msg, "tool_calls") and msg.tool_calls:
    print("🧰 TOOL CALLS:\n")
    print(json.dumps(msg.tool_calls, indent=2))
# Fallback: Print everything if unknown
else:
    print("⚠️ No readable text returned. Full raw response below:\n")
    print(json.dumps(response.model_dump(), indent=2))


