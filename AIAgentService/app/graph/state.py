from typing import TypedDict


class AuthAnalysisState(TypedDict):

    repo_path: str

    files: list[str]

    auth_files: list[str]

    file_contents: dict[str, str]

    explanation: str