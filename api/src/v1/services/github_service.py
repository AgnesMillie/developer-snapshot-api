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
    ... (o corpo desta função continua o mesmo de antes) ...
    """
    url = f"{GITHUB_API_URL}/users/{username}/repos"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=HEADERS)
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


# --- NOVA FUNÇÃO ADICIONADA ABAIXO ---

async def get_repo_file_tree(owner: str, repo_name: str, branch: str = "main") -> list[str]:
    """
    Fetches the file tree for a specific repository branch recursively.

    Args:
        owner: The owner of the repository.
        repo_name: The name of the repository.
        branch: The branch name to fetch the tree from (defaults to "main").

    Returns:
        A flat list of file paths in the repository.

    Raises:
        HTTPException: If the repository or tree is not found, or another API error occurs.
    """
    # O parâmetro recursive=1 é uma forma muito eficiente de buscar todos os arquivos em uma única chamada.
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo_name}/git/trees/{branch}?recursive=1"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=HEADERS)
            response.raise_for_status()

            data = response.json()
            # A API retorna uma árvore. Vamos extrair apenas os caminhos dos arquivos ('blob').
            file_paths = [item["path"] for item in data.get(
                "tree", []) if item.get("type") == "blob"]
            return file_paths

        except httpx.HTTPStatusError as e:
            if e.response.status_code == status.HTTP_404_NOT_FOUND:
                # Retorna lista vazia se o repositório ou a branch não for encontrado.
                return []
            # A API do GitHub retorna 409 Conflict para repositórios vazios.
            elif e.response.status_code == status.HTTP_409_CONFLICT:
                # Tratamos repositórios vazios como se não tivessem arquivos.
                return []
            else:
                raise HTTPException(
                    status_code=e.response.status_code,
                    detail=f"An error occurred while fetching repo tree for '{owner}/{repo_name}': {e.response.text}"
                )
        except httpx.RequestError as e:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail=f"Could not connect to GitHub API: {e}"
            )
