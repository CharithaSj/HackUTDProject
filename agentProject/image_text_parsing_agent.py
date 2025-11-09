import os
import base64
import json
import mimetypes
import requests
from dotenv import load_dotenv

load_dotenv()


def parse_image(image_path, task="markdown_no_bbox"):
    """
    Parse image using Nemotron Parse API
    
    task options as given on site:
    - "markdown_bbox": Extract with bounding boxes
    - "markdown_no_bbox": Extract text as markdown (default)
    - "detection_only": Detect elements only
    """
    
    nvidia_api_key = os.getenv("NVIDIA_API_KEY")
    
    # Read image as base64
    with open(image_path, "rb") as f:
        data = f.read()
    b64_str = base64.b64encode(data).decode("ascii")
    
    # Guess MIME type
    mime, _ = mimetypes.guess_type(image_path)
    if mime is None:
        mime = "image/jpeg"
    
    # Build content with HTML-style image tag
    media_tag = f'<img src="data:{mime};base64,{b64_str}" />'
    content = f"{media_tag}"
    
    # Specify the tool
    tool_spec = [{"type": "function", "function": {"name": task}}]
    
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {nvidia_api_key}",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "nvidia/nemotron-parse",
        "messages": [{"role": "user", "content": content}],
        "tools": tool_spec,
        "tool_choice": {"type": "function", "function": {"name": task}},
        "max_tokens": 1024
    }
    
    print(f"Parsing image with Nemotron Parse ({task})...")
    
    response = requests.post(url, headers=headers, json=payload, timeout=120)
    
    if response.status_code != 200:
        print(f"Error {response.status_code}: {response.text}")
        return None
    
    result = response.json()
    
    # Extract the parsed content
    try:
        tool_call = result['choices'][0]['message']['tool_calls'][0]
        arguments = json.loads(tool_call['function']['arguments'])
        
        # Arguments is a LIST of dicts with "text" key
        extracted_text = arguments[0]['text']
        
        return extracted_text
    except Exception as e:
        print(f"Could not extract content: {e}")
        return None


if __name__ == "__main__":
    image_path = "/Users/sravyakotamraju/HackUTDProject/agentProject/IMG_2930.JPG"
    
    print("Testing NVIDIA Nemotron Parse\n")
    
    content = parse_image(image_path)
    
    if content:
        print("\nSUCCESS! Extracted Text:")
        print("="*60)
        print(content)
        print("="*60)
    else:
        print("\nFailed to parse image")