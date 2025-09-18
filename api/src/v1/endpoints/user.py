import asyncio
from fastapi import APIRouter
from src.v1.services import github_service
# 1. Importamos o novo módulo
from src.v1.analysis import archetype_classifier, skill_inference
from datetime import datetime, timezone
from collections import Counter

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
    Retrieves a structured snapshot of a developer's profile, including
    repository classification, skill inference, and raw data.
    """
    # Etapa 1: Buscar a lista de repositórios do usuário.
    repos_data = await github_service.get_public_repos_by_username(username)

    # Etapa 2: Em paralelo, buscar a árvore de arquivos para cada repositório.
    file_tree_tasks = [
        github_service.get_repo_file_tree(
            owner=repo["owner"]["login"],
            repo_name=repo["name"],
            branch=repo["default_branch"]
        )
        for repo in repos_data
    ]
    file_trees = await asyncio.gather(*file_tree_tasks)

    # Etapa 3: Agora que temos as árvores de arquivos, podemos inferir as habilidades
    # de cada repositório, também em paralelo.
    skill_inference_tasks = [
        skill_inference.infer_skills_from_repo(
            owner=repo["owner"]["login"],
            repo_name=repo["name"],
            file_tree=file_trees[i]
        )
        for i, repo in enumerate(repos_data)
    ]
    # 'results_per_repo' será uma lista de conjuntos, ex: [ {'React', 'TypeScript'}, {'Django'}, ... ]
    results_per_repo = await asyncio.gather(*skill_inference_tasks)

    # Agregamos todas as habilidades de todos os repositórios em um único conjunto para ter a lista final.
    all_inferred_skills = set()
    for skill_set in results_per_repo:
        all_inferred_skills.update(skill_set)

    # Etapa 4: Classificamos os arquétipos (operação síncrona, pode ser em um loop simples).
    project_archetypes = []
    for i, repo in enumerate(repos_data):
        archetype = archetype_classifier.classify_repository_archetype(
            repo, file_trees[i])
        project_archetypes.append(archetype)
    archetype_counts = Counter(project_archetypes)

    # Etapa 5: Construímos a resposta final.
    snapshot = {
        "username": username,
        "snapshotDate": datetime.now(timezone.utc).isoformat(),
        # 2. Adicionamos a lista de skills
        "inferredSkills": sorted(all_inferred_skills),
        "mostImpactfulContribution": {},
        "collaborationStyle": "To be determined",
        "projectArchetypes": archetype_counts,
        "rawRepositoryCount": len(repos_data),
        "rawRepositoryData": repos_data
    }

    return snapshot
