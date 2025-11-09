import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
NIM_BASE_URL = "https://integrate.api.nvidia.com/v1"
MODEL_ID = "nvidia/nemotron-70b-instruct"


if not NVIDIA_API_KEY:
    raise ValueError("Missing NVIDIA_API_KEY in .env file")

client = OpenAI(api_key=NVIDIA_API_KEY, base_url=NIM_BASE_URL)


def nemotron_call(prompt: str, system: str = "You are a helpful AI agent.") -> str:
    """
    Sends prompt to NVIDIA Nemotron model and returns the generated text.
    """
    try:
        response = client.chat.completions.create(
            model=MODEL_ID,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Nemotron API Error: {e}"
