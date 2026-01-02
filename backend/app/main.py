from fastapi import FastAPI
from backend.app.api.workflows import router as workflow_router
from backend.app.logger import logger

app = FastAPI(title="Workflow Popularity Engine")


@app.get("/health")
def health_check():
    logger.info("GET /workflows")
    return {"status": "ok"}


app.include_router(workflow_router)
