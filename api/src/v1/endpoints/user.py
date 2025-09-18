from fastapi import APIRouter
from src.v1.services import github_service
from datetime import datetime, timezone  # Importamos para usar data e hora

router = APIRouter()


@router.get("/users/{username}/repos", tags=["Users"])
async def get_user_repos(username: str):
    """
    Retrieves a list of public repositories for a given GitHub username.
    """
    return await github_service.get_public_repos_by_username(username)


# --- NOVO ENDPOINT ADICIONADO ABAIXO ---

@router.get("/users/{username}/snapshot", tags=["Users"])
async def get_user_snapshot(username: str):
    """
    Retrieves a structured snapshot of a developer's profile,
    including raw repository data and placeholders for future analysis.
    """
    # 1. Buscamos os dados brutos usando nosso serviço existente.
    #    Toda a lógica de chamada à API do GitHub e tratamento de erros já está encapsulada.
    repos_data = await github_service.get_public_repos_by_username(username)

    # 2. Construímos a estrutura de resposta final do snapshot.
    snapshot = {
        "username": username,
        "snapshotDate": datetime.now(timezone.utc).isoformat(),
        "inferredSkills": [],  # Placeholder para funcionalidades futuras
        "mostImpactfulContribution": {},  # Placeholder para funcionalidades futuras
        # Placeholder para funcionalidades futuras
        "collaborationStyle": "To be determined",
        "projectArchetypes": [],  # Placeholder para funcionalidades futuras
        "rawRepositoryCount": len(repos_data),
        "rawRepositoryData": repos_data
    }

    return snapshot
