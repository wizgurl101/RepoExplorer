from langgraph.graph import StateGraph, END

from app.graph.state import AuthAnalysisState
from app.services.repository import scan_repository, find_auth_files


def scan_node(state: AuthAnalysisState) -> AuthAnalysisState:
    files = scan_repository(state["repo_path"])
    return {**state, "files": files}


def find_auth_node(state: AuthAnalysisState) -> AuthAnalysisState:
    auth_files = find_auth_files(state["files"])
    return {**state, "auth_files": auth_files}


def explain_node(state: AuthAnalysisState) -> AuthAnalysisState:
    return {**state, "explanation": "LangGraph was added"}


def build_graph():
    graph = StateGraph(AuthAnalysisState)

    graph.add_node("scan", scan_node)
    graph.add_node("find_auth", find_auth_node)
    graph.add_node("explain", explain_node)

    graph.set_entry_point("scan")
    graph.add_edge("scan", "find_auth")
    graph.add_edge("find_auth", "explain")
    graph.add_edge("explain", END)

    return graph.compile()


_graph = build_graph()


async def analyze_authentication(repo_path: str) -> AuthAnalysisState:
    initial_state: AuthAnalysisState = {
        "repo_path": repo_path,
        "files": [],
        "auth_files": [],
        "file_contents": {},
        "explanation": ""
    }

    return await _graph.ainvoke(initial_state)
