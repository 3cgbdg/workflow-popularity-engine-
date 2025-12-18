from fastapi import FastAPI

app = FastAPI(title="Workflow Popularity Engine")

@app.get("/health")
def health_check():
    return {"status": "ok"}
