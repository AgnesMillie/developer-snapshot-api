from collections import Counter


def classify_repository_archetype(repo_data: dict, file_paths: list[str]) -> str:
    """
    Classifies a repository into an archetype based on its files and metadata.

    Args:
        repo_data: The dictionary containing repository metadata from the GitHub API.
        file_paths: A flat list of all file paths in the repository.

    Returns:
        A string representing the classified archetype.
    """
    if is_fork(repo_data):
        return "Forked Repository"

    extension_counts = count_file_extensions(file_paths)
    file_set = set(file_paths)

    if is_frontend_web_app(file_paths, file_set):
        return "Frontend Web App"
    if backend_type := classify_backend(file_set):
        return backend_type
    if is_data_science_project(extension_counts, file_paths):
        return "Data Science / Notebooks"
    if is_mobile_app(file_paths):
        return "Mobile App"
    if is_devops_project(file_paths, file_set):
        return "DevOps / Infrastructure"
    if is_documentation_project(file_set, extension_counts, file_paths):
        return "Documentation"

    return "Generic Project"


def is_fork(repo_data: dict) -> bool:
    return repo_data.get("fork", False)


def count_file_extensions(file_paths: list[str]) -> Counter:
    return Counter(path.split('.')[-1] for path in file_paths if '.' in path)


def is_frontend_web_app(file_paths: list[str], file_set: set) -> bool:
    if 'package.json' in file_set:
        return any(path.startswith('src/components') or path.startswith('src/pages') for path in file_paths)
    return False


def classify_backend(file_set: set) -> str | None:
    if 'requirements.txt' in file_set:
        return "Python Backend"
    if 'pom.xml' in file_set:
        return "Java Backend (Maven)"
    if 'build.gradle' in file_set:
        return "Java Backend (Gradle)"
    if 'package.json' in file_set and 'server.js' in file_set:
        return "Node.js Backend"
    return None


def is_data_science_project(extension_counts: Counter, file_paths: list[str]) -> bool:
    return extension_counts['ipynb'] > len(file_paths) * 0.2 and len(file_paths) > 0


def is_mobile_app(file_paths: list[str]) -> bool:
    return 'android/app' in file_paths or 'ios/App' in file_paths


def is_devops_project(file_paths: list[str], file_set: set) -> bool:
    return 'Dockerfile' in file_set or 'docker-compose.yml' in file_set or any(path.endswith('.tf') for path in file_paths)


def is_documentation_project(file_set: set, extension_counts: Counter, file_paths: list[str]) -> bool:
    if 'mkdocs.yml' in file_set or '_config.yml' in file_set:
        return extension_counts['md'] > len(file_paths) * 0.5 and len(file_paths) > 0
    return False
