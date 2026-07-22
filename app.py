from fastapi import FastAPI

from routes.github_routes import router as github_router

app = FastAPI(
    title="KnowSphere Agent Server",
    version="1.0.0"
)

app.include_router(github_router)

@app.get("/")
def home():
    return {
        "status": "Running",
        "agent": "Central Agent"
    }