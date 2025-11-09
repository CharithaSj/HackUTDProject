import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

NIM_BASE_URL = "https://integrate.api.nvidia.com/v1"
MODEL_ID = "nvidia/llama-3.3-nemotron-super-49b-v1.5"

api_key = os.getenv("NVIDIA_API_KEY")
if not api_key:
    raise RuntimeError("Set NVIDIA_API_KEY in your environment or .env before running this cell.")

client = OpenAI(api_key=api_key, base_url=NIM_BASE_URL)
print(f"Client ready for {MODEL_ID}")

def get_current_weather(location: str, unit: str = "celsius") -> dict:
    """Return dummy weather data for the requested location."""
    forecast = {
        "temperature_c": 19,
        "temperature_f": 66,
        "condition": "clear skies",
        "humidity": 0.72,
        "wind_kph": 8.0,
    }
    if unit.lower().startswith("f"):
        temperature = forecast["temperature_f"]
        unit_label = "F"
    else:
        temperature = forecast["temperature_c"]
        unit_label = "°C"

    return {
        "location": location,
        "summary": forecast["condition"],
        "temperature": temperature,
        "unit": unit_label,
        "humidity": forecast["humidity"],
        "wind_kph": forecast["wind_kph"],
    }

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Look up the current weather for a city and return structured conditions.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "City and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "Temperature unit to return.",
                    },
                },
                "required": ["location"],
            },
        },
    }
]
messages = [
    {
        "role": "system",
        "content": "You are a helpful weather assistant. Call tools when you need real-world data before replying to the user.",
    },
    {
        "role": "user",
        "content": "What's the weather like in San Francisco this afternoon?",
    },
]

first_completion = client.chat.completions.create(
    model=MODEL_ID,
    messages=messages,
    tools=tools,
    tool_choice="auto",
    temperature=0.2,
    max_tokens=512,
)
assistant_message = first_completion.choices[0].message
print("Assistant requested tool:")
print(assistant_message)

assistant_dict = {
    "role": assistant_message.role,
    "content": assistant_message.content or "",
}
if assistant_message.tool_calls:
    assistant_dict["tool_calls"] = [
        {
            "id": call.id,
            "type": call.type,
            "function": {
                "name": call.function.name,
                "arguments": call.function.arguments,
            },
        }
        for call in assistant_message.tool_calls
    ]

messages.append(assistant_dict)

for call in assistant_message.tool_calls or []:
    if call.function.name != "get_current_weather":
        continue
    call_args = json.loads(call.function.arguments or "{}")
    tool_response = get_current_weather(**call_args)
    print("Tool response:")
    print(tool_response)
    messages.append(
        {
            "role": "tool",
            "tool_call_id": call.id,
            "name": call.function.name,
            "content": json.dumps(tool_response),
        }
    )


final_completion = client.chat.completions.create(
    model=MODEL_ID,
    messages=messages,
    temperature=0.2,
    max_tokens=512
)
final_message = final_completion.choices[0].message
print("\nFinal model answer:\n")
print(final_message.content)