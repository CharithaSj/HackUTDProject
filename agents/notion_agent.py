
import os
import json
import base64
import mimetypes
import requests
from notion_client import Client
from openai import OpenAI
from dotenv import load_dotenv
from typing import Dict, List

load_dotenv()

# Initialize clients
notion = Client(auth=os.getenv("NOTION_TOKEN"))
openrouter_client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)


# ========== NEMOTRON ANALYSIS (THE KEY PART) ==========

def analyze_with_nemotron(user_query: str, notion_content: str) -> str:
    """
    Use Nemotron to actually ANALYZE the content and answer the question.
    This is the reasoning/decision-making layer you're missing.
    """
    prompt = f"""You are analyzing Notion workspace data to answer a user's question.

USER QUESTION: {user_query}

NOTION DATA:
{notion_content}

INSTRUCTIONS:
1. Read through ALL the data provided above
2. FILTER: Ignore any pages/sections that are clearly unrelated to the user's question
3. IDENTIFY: Find specific information relevant to answering the question (look in text, tables, and image content)
4. ANALYZE: Provide a clear, data-driven answer with specific details from the relevant data
5. If you find specific numbers, dates, or facts, include them
6. If the data doesn't contain enough info to answer, say so clearly
7. Be concise but thorough - focus on actionable insights
8. Do NOT mention irrelevant pages in your answer - only discuss data that helps answer the question

FORMAT YOUR RESPONSE EXACTLY LIKE THIS:

[Your detailed answer here with insights, metrics, and analysis]

---
SOURCES USED: [List only the page names you actually referenced in your answer, comma-separated]

ANSWER:"""

    try:
        response = openrouter_client.chat.completions.create(
            model="nvidia/llama-3.1-nemotron-70b-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,  # Lower temp for factual analysis
            max_tokens=1000
        )
        
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        return f"Error during analysis: {e}"


# ========== SIMPLE NOTION SEARCH ==========

def search_notion(query: str, max_results: int = 10) -> List[Dict]:
    """
    Domain-agnostic Notion search with intelligent fallback
    
    Strategy:
    1. Try searching with user's query (searches page titles only - Notion API limitation)
    2. If we get results, use them
    3. If we get nothing, pull ALL pages and let Nemotron filter relevance during analysis
    
    This works for any domain since we're not hardcoding keywords
    """
    try:
        # Step 1: Search with user's specific query
        results = notion.search(
            query=query,
            filter={"property": "object", "value": "page"},
            page_size=max_results
        )
        
        found_pages = results.get("results", [])
        
        # Step 2: If we found pages, return them
        if found_pages:
            print(f"  ✓ Found {len(found_pages)} pages matching query")
            return found_pages
        
        # Step 3: No matches - Notion only searches titles, not content
        # Pull ALL pages and let Nemotron filter during analysis
        print(f"  ⚠️  No pages match '{query}' in titles")
        print(f"  → Pulling all pages (Notion API can't search table content)")
        print(f"  → Nemotron will identify relevant data during analysis")
        
        all_pages_results = notion.search(
            filter={"property": "object", "value": "page"},
            page_size=max_results
        )
        
        all_pages = all_pages_results.get("results", [])
        print(f"  ✓ Retrieved {len(all_pages)} total pages for analysis")
        
        return all_pages
    
    except Exception as e:
        print(f"Search error: {e}")
        return []


# ========== CONTENT EXTRACTION (Simplified from your code) ==========

def extract_page_title(page_object: Dict) -> str:
    """Extract title from page"""
    try:
        properties = page_object.get("properties", {})
        
        for prop_name, prop_value in properties.items():
            if prop_value.get("type") == "title":
                title_parts = prop_value.get("title", [])
                if title_parts:
                    return "".join([part.get("plain_text", "") for part in title_parts])
        
        return "Untitled"
    
    except:
        return "Unknown"


def extract_rich_text(rich_text_array: List) -> str:
    """Extract text from Notion rich text"""
    if not rich_text_array:
        return ""
    
    return "".join([
        item.get("plain_text", "") 
        for item in rich_text_array 
        if isinstance(item, dict)
    ])


def extract_table_data(table_block_id: str) -> str:
    """Extract table as markdown"""
    try:
        all_rows = []
        start_cursor = None
        
        while True:
            if start_cursor:
                response = notion.blocks.children.list(
                    table_block_id, 
                    start_cursor=start_cursor
                )
            else:
                response = notion.blocks.children.list(table_block_id)
            
            for row in response.get("results", []):
                if row["type"] == "table_row":
                    cells = row["table_row"]["cells"]
                    row_data = [
                        "".join([t["plain_text"] for t in cell])
                        for cell in cells
                    ]
                    all_rows.append(row_data)
            
            if not response.get("has_more", False):
                break
            
            start_cursor = response.get("next_cursor")
        
        if not all_rows:
            return ""
        
        # Format as markdown
        header = all_rows[0]
        data_rows = all_rows[1:]
        
        table = "| " + " | ".join(header) + " |\n"
        table += "| " + " | ".join(["---"] * len(header)) + " |\n"
        
        for row in data_rows:
            table += "| " + " | ".join(row) + " |\n"
        
        return table
    
    except Exception as e:
        print(f"Table extraction error: {e}")
        return ""


def parse_image_with_nemotron(image_url_or_path: str) -> str:
    """Parse image using Nemotron Parse"""
    nvidia_api_key = os.getenv("NVIDIA_API_KEY")
    
    if not nvidia_api_key:
        return ""
    
    try:
        if image_url_or_path.startswith("http"):
            img_data = requests.get(image_url_or_path).content
            b64_str = base64.b64encode(img_data).decode("ascii")
            mime = "image/jpeg"
        else:
            with open(image_url_or_path, "rb") as f:
                img_data = f.read()
            b64_str = base64.b64encode(img_data).decode("ascii")
            mime, _ = mimetypes.guess_type(image_url_or_path)
            if mime is None:
                mime = "image/jpeg"
    except:
        return ""
    
    url = "https://integrate.api.nvidia.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {nvidia_api_key}",
        "Content-Type": "application/json"
    }
    
    media_tag = f'<img src="data:{mime};base64,{b64_str}" />'
    
    payload = {
        "model": "nvidia/nemotron-parse",
        "messages": [{"role": "user", "content": media_tag}],
        "tools": [{"type": "function", "function": {"name": "markdown_no_bbox"}}],
        "tool_choice": {"type": "function", "function": {"name": "markdown_no_bbox"}},
        "max_tokens": 1024
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=120)
        if response.status_code == 200:
            result = response.json()
            tool_call = result['choices'][0]['message']['tool_calls'][0]
            arguments = json.loads(tool_call['function']['arguments'])
            return arguments[0]['text']
    except Exception as e:
        print(f"Image parsing error: {e}")
    
    return ""


def extract_page_content(page_id: str) -> Dict:
    """
    Extract ALL content from a Notion page
    Returns dict with text, tables, and image content
    """
    content = {
        "text": [],
        "tables": [],
        "images": []
    }
    
    try:
        start_cursor = None
        
        while True:
            if start_cursor:
                response = notion.blocks.children.list(
                    page_id,
                    start_cursor=start_cursor,
                    page_size=100
                )
            else:
                response = notion.blocks.children.list(page_id, page_size=100)
            
            blocks = response.get("results", [])
            
            for block in blocks:
                block_type = block["type"]
                
                # Text blocks
                if block_type in ["paragraph", "heading_1", "heading_2", "heading_3", 
                                 "bulleted_list_item", "numbered_list_item", "quote", "callout"]:
                    rich_text = block[block_type].get("rich_text", [])
                    text = extract_rich_text(rich_text)
                    if text.strip():
                        content["text"].append(text.strip())
                
                # Tables
                elif block_type == "table":
                    table_data = extract_table_data(block["id"])
                    if table_data:
                        content["tables"].append(table_data)
                
                # Images
                elif block_type == "image":
                    image_info = block["image"]
                    if image_info["type"] == "external":
                        image_url = image_info["external"]["url"]
                    elif image_info["type"] == "file":
                        image_url = image_info["file"]["url"]
                    else:
                        continue
                    
                    # Parse image with Nemotron
                    parsed = parse_image_with_nemotron(image_url)
                    if parsed:
                        content["images"].append(parsed)
            
            if not response.get("has_more", False):
                break
            
            start_cursor = response.get("next_cursor")
        
    except Exception as e:
        print(f"Content extraction error: {e}")
    
    return content


# ========== MAIN QUERY FUNCTION ==========

def query_notion(user_question: str, max_pages: int = 5) -> Dict:
    """
    Complete pipeline: Search → Extract → Analyze
    This is what your team will call
    """
    print(f"\n🔍 Searching Notion for: '{user_question}'")
    
    # Step 1: Search Notion
    search_results = search_notion(user_question, max_results=max_pages)
    
    if not search_results:
        return {
            "answer": "I couldn't find any relevant pages in your Notion workspace.",
            "sources_extracted": [],
            "sources_used": [],
            "raw_content": ""
        }
    
    print(f"📄 Found {len(search_results)} pages")
    
    # Step 2: Extract content from all pages
    all_content = []
    sources_extracted = []
    
    for page in search_results:
        title = extract_page_title(page)
        page_id = page["id"]
        
        print(f"  📖 Extracting: {title}")
        
        try:
            page_content = extract_page_content(page_id)
            
            # Build formatted content for this page
            page_text = f"\n{'='*60}\nSOURCE: {title}\n{'='*60}\n"
            
            if page_content["text"]:
                page_text += "\nTEXT CONTENT:\n" + "\n".join(page_content["text"]) + "\n"
            
            if page_content["tables"]:
                page_text += f"\nTABLES ({len(page_content['tables'])}):\n"
                for table in page_content["tables"]:
                    page_text += f"\n{table}\n"
            
            if page_content["images"]:
                page_text += f"\nIMAGE CONTENT:\n"
                for img_text in page_content["images"]:
                    page_text += f"{img_text}\n"
            
            all_content.append(page_text)
            sources_extracted.append(title)
        
        except Exception as e:
            print(f"  ❌ Failed to extract from '{title}': {e}")
            continue
    
    if not all_content:
        return {
            "answer": "Found pages but couldn't extract any content.",
            "sources_extracted": sources_extracted,
            "sources_used": [],
            "raw_content": ""
        }
    
    # Combine all content
    combined_content = "\n".join(all_content)
    
    # Step 3: ANALYZE with Nemotron (THE KEY STEP)
    print(f"\n🤖 Analyzing with Nemotron...")
    full_response = analyze_with_nemotron(user_question, combined_content)
    
    # Step 4: Parse out sources used
    answer = full_response
    sources_used = []
    
    if "SOURCES USED:" in full_response:
        parts = full_response.split("SOURCES USED:")
        answer = parts[0].strip()
        sources_line = parts[1].strip()
        
        # Parse comma-separated sources
        sources_used = [s.strip() for s in sources_line.split(",") if s.strip()]
        
        # Clean up the answer to remove the separator line if present
        if answer.endswith("---"):
            answer = answer[:-3].strip()
    
    return {
        "answer": answer,
        "sources_extracted": sources_extracted,  # All pages we pulled content from
        "sources_used": sources_used,  # Only pages Nemotron actually referenced
        "raw_content": combined_content  # Include for debugging/team integration
    }


# ========== TEAM INTEGRATION INTERFACE ==========

def analyze_notion_data(query: str) -> str:
    """
    Clean interface for your team to use when integrating
    
    Example usage from another module:
        from notion_agent_fixed import analyze_notion_data
        
        answer = analyze_notion_data("What was our Q4 revenue?")
        print(answer)
    
    Returns just the answer text. For full details including sources, use query_notion()
    """
    result = query_notion(query)
    return result["answer"]


# ========== TESTING ==========

if __name__ == "__main__":
    # Test queries
    test_queries = [
        "What banking data do we have?",
        "Show me customer segmentation information",
        "What are our fraud loss metrics?",
        "What is the best lighting for money plants?"
    ]
    
    for query in test_queries:
        print(f"\n{'='*80}")
        print(f"QUERY: {query}")
        print('='*80)
        
        result = query_notion(query, max_pages=3)
        
        print(f"\n📊 ANSWER:")
        print("-" * 80)
        print(result["answer"])
        print("-" * 80)
        
        print(f"\n📚 SOURCES:")
        print(f"   Extracted from: {', '.join(result['sources_extracted'])}")
        if result.get('sources_used'):
            print(f"   Actually used: {', '.join(result['sources_used'])}")
        else:
            print(f"   Actually used: (not specified by model)")
        
        print("\n" + "="*80)