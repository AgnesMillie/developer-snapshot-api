import asyncio  # Importamos a biblioteca de concorrência
from fastapi import APIRouter
from src.v1.services import github_service
# Importamos nosso novo classificador
from src.v1.analysis import archetype_classifier
from datetime import datetime, timezone

router = APIRouter()


@router.get("/users/{username}/repos", tags=["Users"])
async def get_user_repos(username: str):
    """
    Retrieves a list of public repositories for a given GitHub username.
    """
    return await github_service.get_public_repos_by_username(username)


@router.get("/users/{username}/snapshot", tags=["Users"])
async def get_user_snapshot(username: str):
    """
    Retrieves a structured snapshot of a developer's profile,
    including repository classification and raw data.
    """
    # 1. Buscamos a lista de repositórios do usuário.
    repos_data = await github_service.get_public_repos_by_username(username)

    # 2. Criamos uma lista de "tarefas" para buscar a árvore de arquivos de cada repositório em paralelo.
    tasks = [
        github_service.get_repo_file_tree(
            owner=repo["owner"]["login"],
            repo_name=repo["name"],
            branch=repo["default_branch"]
        )
        for repo in repos_data
    ]
    # Executamos todas as tarefas concorrentemente.
    file_trees = await asyncio.gather(*tasks)

    # 3. Classificamos cada repositório e coletamos os arquétipos.
    project_archetypes = []
    for i, repo in enumerate(repos_data):
        file_tree = file_trees[i]
        archetype = archetype_classifier.classify_repository_archetype(
            repo, file_tree)
        project_archetypes.append(archetype)

    # Usamos um Counter para agregar os resultados.
    from collections import Counter
    archetype_counts = Counter(project_archetypes)

    # 4. Construímos a resposta final.
    snapshot = {
        "username": username,
        "snapshotDate": datetime.now(timezone.utc).isoformat(),
        "inferredSkills": [],
        "mostImpactfulContribution": {},
        "collaborationStyle": "To be determined",
        "projectArchetypes": archetype_counts,  # Adicionamos os arquétipos contados
        "rawRepositoryCount": len(repos_data),
        "rawRepositoryData": repos_data
    }

    return snapshot
