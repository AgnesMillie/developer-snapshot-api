from fastapi import APIRouter
from src.v1.services import github_service

router = APIRouter()


@router.get("/users/{username}/repos", tags=["Users"])
async def get_user_repos(username: str):
    """
    Retrieves a list of public repositories for a given GitHub username.
    The endpoint layer is kept thin, its main responsibility is to call
    the appropriate service and return the response.
    """
    # All the complex logic (API calls, error handling) is in the service layer.
    return await github_service.get_public_repos_by_username(username)
