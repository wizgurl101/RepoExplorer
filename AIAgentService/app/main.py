from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="RepoExplorer"
)

app.include_router(router)