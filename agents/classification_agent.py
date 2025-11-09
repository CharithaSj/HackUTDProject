# agents/classification_agent.py
import re

def classify_sources(user_query: str):
    """
    Determines which data sources should be used based on the query.
    If the query references a specific slide (1–4), it returns the matching link ID.
    Also detects the analysis mode (summary, stats, title, topics).
    """

    query = user_query.lower()
    sources = []
    slide_target = None
    mode = "summary"  # Default mode

    # --- Targeted detections ---
     # --- Detect GitHub Repositories or Usernames ---
    if (
    "github" in query
    or "repo" in query
    or re.search(r"github\.com", query)
    or re.search(r"\b[a-zA-Z0-9-]{3,}\b", query) and (
        # common signs of a GitHub entity
        re.search(r"Dshah1003|UTDallasEPICS|EPICS|repo|fork|pull|issue|commit", query, re.IGNORECASE)
    )
):
       sources.append("github")


    if "notion" in query or "workspace" in query or "document" in query:
        sources.append("notion")

    if "slide" in query or "presentation" in query or re.search(r"slides\.google\.com", query):
        sources.append("slides")

    if "image" in query or "screenshot" in query or "diagram" in query:
        sources.append("images")

    # --- Detect specific slide numbers ---
    slide_match = re.search(r"slide\s*(\d+)", query)
    if slide_match:
        slide_num = int(slide_match.group(1))
        if 1 <= slide_num <= 4:
            slide_target = f"slide{slide_num}"
            if "slides" not in sources:
                sources.append("slides")

    # --- Detect mode of analysis ---
    if any(word in query for word in ["stat", "data", "numbers", "metrics", "figures"]):
        mode = "stats"
    elif any(word in query for word in ["topic", "subject", "theme"]):
        mode = "topics"
    elif any(word in query for word in ["title", "heading", "name"]):
        mode = "title"
    elif any(word in query for word in ["summarize", "overview", "analyze"]):
        mode = "summary"

    # --- Domain-based generalization ---
    finance_keywords = ["finance", "banking", "revenue", "fraud", "transaction"]
    if any(word in query for word in finance_keywords):
        sources.extend(["notion", "slides", "github", "images"])

    # --- Default fallback: check everything ---
    if not sources:
        sources = ["notion", "slides", "github", "images"]

    # Remove duplicates
    sources = list(set(sources))

    return {
        "sources": sources,
        "slide_target": slide_target,
        "mode": mode
    }


# ===========================================================
# For standalone testing
# ===========================================================
if __name__ == "__main__":
    test_queries = [
        "Summarize slide 1",
        "Show me stats from slide 2",
        "Topics covered in slide 3",
        "Title of slide 4",
        "Summarize financial transactions",
        "Show me open issues in https://github.com/Dshah1003/your-repo"
    ]

    for q in test_queries:
        print(f"\nQuery: {q}")
        result = classify_sources(q)
        print("Detected:", result)

