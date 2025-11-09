import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
print("🔑 Key snippet:", os.getenv("NVIDIA_API_KEY")[:10])

client = OpenAI(
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1"
)

try:
    response = client.chat.completions.create(
        model="nvidia/llama-3.3-nemotron-super-49b-v1.5",
        messages=[{"role": "user", "content": "Hello, test connection"}],
        max_tokens=10
    )
    print("✅ Success:", response.choices[0].message.content)
except Exception as e:
    print("❌ Error:", e)
