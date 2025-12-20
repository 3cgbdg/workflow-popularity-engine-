
from fastapi import FastAPI
from backend.app.api.workflows import router as workflow_router

app = FastAPI(title="Workflow Popularity Engine")

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(workflow_router)
