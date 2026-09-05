from pathlib import Path


IGNORED_DIRECTORIES = {
    ".git",
    "node_modules",
    "venv",
    ".venv",
    "__pycache__",
    "dist",
    "build"
}


def scan_repository(repo_path: str) -> list[str]:

    root = Path(repo_path)

    files = []

    for path in root.rglob("*"):

        if not path.is_file():
            continue

        if any(
            ignored in path.parts
            for ignored in IGNORED_DIRECTORIES
        ):
            continue

        files.append(str(path.relative_to(root)))

    return files

AUTH_KEYWORDS = [
    "auth",
    "authentication",
    "authorize",
    "authorization",
    "login",
    "logout",
    "session",
    "jwt",
    "token",
    "oauth",
    "user",
    "permission",
    "role"
]


def find_auth_files(files: list[str]) -> list[str]:

    auth_files = []

    for file in files:

        filename = file.lower()

        if any(
            keyword in filename
            for keyword in AUTH_KEYWORDS
        ):
            auth_files.append(file)

    return auth_files