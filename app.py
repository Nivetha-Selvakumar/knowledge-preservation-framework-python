# from fastapi import FastAPI

# from routes.github_routes import router as github_router

# app = FastAPI(title="KnowSphere Agent Server", version="1.0.0")

# app.include_router(github_router)


# @app.get("/")
# def home():
#     return {"status": "Running", "agent": "Central Agent"}

from fastapi import FastAPI

from routes.github_routes import router as github_router

from routes.github_webhook_routes import router as github_webhook_router

app = FastAPI(title="Adaptive Multi-Agent Service", version="1.0.0")


app.include_router(github_router)

app.include_router(github_webhook_router)


@app.get("/")
def root():

    return {"status": "UP", "service": "Adaptive Multi-Agent Service"}
