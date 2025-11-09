"""
Project Manager Agent — Enhanced and Efficient Version
------------------------------------------------------
• Runs only relevant agents (Slides, Notion, GitHub, Images)
• Executes multiple agents per query if needed
• Displays dynamic progress indicators
• Logs all detailed results to /outputs folder
"""

import os
import time
from datetime import datetime
from agents.classification_agent import classify_sources
from agents.notion_agent import analyze_notion_data as get_notion_data
from agents.github_agent import analyze_github as get_github_data
from agents.image_agent import parse_image as get_image_data
from agents.slides_agent import analyze_slides

# ===========================================================
# 1. Mapped Google Slides links
# ===========================================================
SLIDE_LINKS = {
    "slide1": r"https://docs.google.com/presentation/d/1nW35OzCsJxcnu64AvHJA1QnCg_aYOJyTqbhYljrcEmI/edit",
    "slide2": r"https://docs.google.com/presentation/d/1Y7-tt8vv8_xSoGpOcPsGNNmmB2Gg1YzUdqy6xzQK1cU/edit?usp=sharing",
    "slide3": r"https://docs.google.com/presentation/d/1p2QUOoSGbm0gVPrmFqGg5eikJBJSMIH5TFQW_wdJgdU/edit?usp=sharing",
    "slide4": r"https://docs.google.com/presentation/d/1p2QUOoSGbm0gVPrmFqGg5eikJBJSMIH5TFQW_wdJgdU/edit?usp=sharing",
}


# ===========================================================
# 2. Query Processor
# ===========================================================
def process_query(user_query: str) -> str:
    """
    Routes the query to only the relevant agents.
    Displays progress and combines results cleanly.
    """
    print(f"\n🔍 Processing query: {user_query}")
    classification = classify_sources(user_query)
    sources = classification["sources"]
    slide_target = classification.get("slide_target")
    mode = classification.get("mode", "summary")

    combined_output = []
    summary_log = []

    # =======================================================
    # Slides Agent
    # =======================================================
    if "slides" in sources:
        print("\n🎞️ Fetching Google Slides data...")
        time.sleep(0.5)
        try:
            if slide_target and slide_target in SLIDE_LINKS:
                result = analyze_slides(SLIDE_LINKS[slide_target], mode)
                combined_output.append(f"=== SLIDES ({slide_target}) ===\n{result}")
                summary_log.append(f"✓ {slide_target.capitalize()} — analyzed in {mode} mode.")
            else:
                result = analyze_slides(SLIDE_LINKS["slide1"], mode)
                combined_output.append("=== SLIDES (Default) ===\n" + result)
                summary_log.append("✓ Default slide analyzed.")
        except Exception as e:
            combined_output.append(f"⚠️ Slides analysis failed: {e}")
            summary_log.append("✗ Slides — error during analysis.")

    # =======================================================
    # Notion Agent
    # =======================================================
    if "notion" in sources:
        print("\n🧩 Fetching Notion workspace data...")
        time.sleep(0.5)
        try:
            result = get_notion_data(user_query)
            combined_output.append("=== NOTION ===\n" + result)
            summary_log.append("✓ Notion data retrieved.")
        except Exception as e:
            combined_output.append(f"⚠️ Notion error: {e}")
            summary_log.append("✗ Notion failed.")

    # =======================================================
    # GitHub Agent
    # =======================================================
    if "github" in sources:
        print("\n🐙 Fetching GitHub repository data...")
        time.sleep(0.5)
        try:
            result = get_github_data(user_query)
            combined_output.append("=== GITHUB ===\n" + result)
            summary_log.append("✓ GitHub data analyzed.")
        except Exception as e:
            combined_output.append(f"⚠️ GitHub error: {e}")
            summary_log.append("✗ GitHub failed.")

    # =======================================================
    # Image Agent
    # =======================================================
    if "images" in sources:
        print("\n🖼️ Fetching Image data...")
        time.sleep(0.5)
        try:
            result = get_image_data(user_query)
            combined_output.append("=== IMAGES ===\n" + result)
            summary_log.append("✓ Image data parsed.")
        except Exception as e:
            combined_output.append(f"⚠️ Image error: {e}")
            summary_log.append("✗ Image parsing failed.")

    # =======================================================
    # If no relevant agents were detected
    # =======================================================
    if not combined_output:
        combined_output.append("⚠️ No valid source detected for this query.")
        summary_log.append("✗ No relevant sources found.")

    # =======================================================
    # Save results
    # =======================================================
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    output_path = f"outputs/combined_results_{timestamp}.txt"

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"USER QUERY: {user_query}\n\n")
        f.write("SOURCE SUMMARY:\n")
        for line in summary_log:
            f.write(f"  {line}\n")
        f.write("\n\n" + "\n\n".join(combined_output))

    # =======================================================
    # Print concise output
    # =======================================================
    print("\n🧠 Summary:")
    for line in summary_log:
        print("  " + line)

    print("\n--- Final Output ---\n")
    print("\n\n".join(combined_output[:1]))  # Only most relevant result
    print(f"\n📂 Full log saved to: {output_path}")

    return "\n\n".join(combined_output)


# ===========================================================
# 3. Run interactively
# ===========================================================
if __name__ == "__main__":
    print("🚀 Running Enhanced PM Agent...\n")
    user_query = input("Enter your query (e.g., 'Title of slide 4' or 'Show stats from slide 3'): ")
    process_query(user_query)
