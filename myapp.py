import os
from dotenv import load_dotenv
import requests

load_dotenv()

USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")

def delete_all_repositories(username: str, token: str) -> None:
    """
    Deletes all repositories associated with the authenticated GitHub user.

    Args:
        username (str): GitHub username.
        token (str): Personal access token for GitHub API authentication.

    Returns:
        None

    Note:
        Prints the result of each deletion attempt to the console.
    """
    headers = {"Authorization": f"token {token}"}
    repos_url = "https://api.github.com/user/repos"

    response = requests.get(repos_url, headers=headers)
    repos = response.json()

    for repo in repos:
        repo_name = repo["name"]
        delete_url = f"https://api.github.com/repos/{username}/{repo_name}"
        delete_response = requests.delete(delete_url, headers=headers)

        if delete_response.status_code == 204:
            print(f"Successfully deleted: {repo_name}")
        else:
            print(f"Failed to delete: {repo_name} – Status code: {delete_response.status_code}")


if __name__ == "__main__":
    GITHUB_USERNAME = USERNAME
    GITHUB_TOKEN = TOKEN

    delete_all_repositories(GITHUB_USERNAME, GITHUB_TOKEN)
