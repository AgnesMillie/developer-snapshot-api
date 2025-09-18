import os
import httpx
from fastapi import HTTPException, status

# Load the GitHub API token from environment variables
GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
if not GITHUB_API_TOKEN:
    raise RuntimeError("GITHUB_API_TOKEN environment variable not set.")

# Define constants
GITHUB_API_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"Bearer {GITHUB_API_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}


async def get_public_repos_by_username(username: str) -> list:
    """
    Fetches a list of public repositories for a given GitHub username.

    Args:
        username: The GitHub username to search for.

    Returns:
        A list of repository data as dictionaries.

    Raises:
        HTTPException: If the user is not found or another API error occurs.
    """
    url = f"{GITHUB_API_URL}/users/{username}/repos"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=HEADERS)

            # Raise an HTTP exception for bad status codes (4xx or 5xx)
            response.raise_for_status()

            return response.json()

        except httpx.HTTPStatusError as e:
            if e.response.status_code == status.HTTP_404_NOT_FOUND:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"User '{username}' not found on GitHub."
                )
            else:
                raise HTTPException(
                    status_code=e.response.status_code,
                    detail=f"An error occurred while fetching data from GitHub: {e.response.text}"
                )
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Could not connect to GitHub API: {e}"
            )
