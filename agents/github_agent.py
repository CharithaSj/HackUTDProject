import re
import requests
import os

def analyze_github(user_query: str) -> str:
    """
    Fetches basic GitHub repository information such as open issues, PRs, and stars.
    """

    # Try to extract repo name from URL (e.g. https://github.com/username/repo)
    match = re.search(r"github\.com/([\w\-]+)/([\w\-]+)", user_query)
    if not match:
        return "⚠️ Could not find a valid GitHub repo link in your query."

    username, repo = match.groups()
    api_url = f"https://api.github.com/repos/{username}/{repo}"

    headers = {}
    if os.getenv("GITHUB_TOKEN"):
        headers["Authorization"] = f"token {os.getenv('GITHUB_TOKEN')}"

    try:
        # Get repo metadata
        repo_data = requests.get(api_url, headers=headers)
        if repo_data.status_code != 200:
            return f"❌ Error fetching repo '{username}/{repo}': {repo_data.text}"

        repo_json = repo_data.json()

        # Get issues count
        issues_data = requests.get(f"{api_url}/issues?state=open", headers=headers)
        issues_count = len(issues_data.json()) if issues_data.status_code == 200 else "Unknown"

        # Build summary
        summary = (
            f"Repository: {username}/{repo}\n"
            f"Description: {repo_json.get('description', 'No description')}\n"
            f"Stars: {repo_json.get('stargazers_count', 0)}\n"
            f"Forks: {repo_json.get('forks_count', 0)}\n"
            f"Open Issues: {issues_count}\n"
            f"Last Updated: {repo_json.get('updated_at', 'Unknown')}\n"
        )

        return summary

    except Exception as e:
        return f"❌ Error fetching GitHub data: {e}"



# Optional standalone test
if __name__ == "__main__":
    test_input = input("Enter GitHub username, repo, or link: ").strip()
    print(analyze_github(test_input))
