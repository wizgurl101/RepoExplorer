from fastapi import APIRouter
from app.graph.auth_graph import analyze_authentication

router = APIRouter(prefix="/api")


@router.get("/analyze-auth")
async def analyze_auth(repo_path: str):
    result = await analyze_authentication(repo_path)

    return result