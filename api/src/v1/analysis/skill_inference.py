import json
from src.v1.services import github_service

# Nossa "Base de Conhecimento" de habilidades.
# Mapeia a 'chave' encontrada no arquivo para o nome 'bonito' da habilidade.
SKILL_MAP = {
    # Python
    "django": "Django",
    "flask": "Flask",
    "fastapi": "FastAPI",
    "pandas": "Pandas",
    "numpy": "NumPy",
    "scikit-learn": "Scikit-learn",
    "tensorflow": "TensorFlow",
    "pytorch": "PyTorch",

    # JavaScript / Node.js
    "react": "React",
    "vue": "Vue.js",
    "@angular/core": "Angular",
    "express": "Express.js",
    "next": "Next.js",
    "typescript": "TypeScript",

    # Java (strings que buscaremos no pom.xml)
    "spring-boot-starter-web": "Java (Spring Boot)",
    "quarkus": "Java (Quarkus)",
    "hibernate-core": "Java (Hibernate)",
}

# CORREÇÃO: Removido o 'async' desnecessário. Esta é uma função síncrona.


def _parse_requirements_txt(content: str) -> set[str]:
    """Parse a requirements.txt file content to extract skills."""
    skills = set()
    lines = content.splitlines()
    for line in lines:
        dependency = line.split('#')[0].strip()
        dependency = dependency.split('==')[0].split(
            '>=')[0].split('<=')[0].strip().lower()
        if dependency in SKILL_MAP:
            skills.add(SKILL_MAP[dependency])
    return skills

# CORREÇÃO: Removido o 'async' desnecessário.


def _parse_package_json(content: str) -> set[str]:
    """Parse a package.json file content to extract skills."""
    skills = set()
    try:
        data = json.loads(content)
        dependencies = data.get('dependencies', {})
        dev_dependencies = data.get('devDependencies', {})
        all_deps = {**dependencies, **dev_dependencies}
        for dep in all_deps.keys():
            if dep in SKILL_MAP:
                skills.add(SKILL_MAP[dep])
    except json.JSONDecodeError:
        print("Warning: Could not parse package.json")
    return skills

# CORREÇÃO: Removido o 'async' desnecessário.


def _parse_pom_xml(content: str) -> set[str]:
    """Parse a pom.xml file content with simple string matching."""
    skills = set()
    content_lower = content.lower()
    for key, skill_name in SKILL_MAP.items():
        if "java" in skill_name.lower() and key in content_lower:
            skills.add(skill_name)
    return skills


async def infer_skills_from_repo(owner: str, repo_name: str, file_tree: list[str]) -> set[str]:
    """
    Infers skills from a repository by analyzing its dependency files.
    Orchestrates the fetching and parsing of different file types.
    """
    inferred_skills = set()

    dependency_files_parsers = {
        "requirements.txt": _parse_requirements_txt,
        "package.json": _parse_package_json,
        "pom.xml": _parse_pom_xml,
    }

    for file_path in file_tree:
        filename = file_path.split('/')[-1]

        # CORREÇÃO: Lógica refatorada para evitar o 'if' aninhado.
        if filename not in dependency_files_parsers:
            continue

        content = await github_service.get_file_content(owner, repo_name, file_path)
        if not content:
            continue

        parser_func = dependency_files_parsers[filename]
        # A chamada agora é síncrona, sem 'await'.
        skills = parser_func(content)
        inferred_skills.update(skills)

    return inferred_skills
