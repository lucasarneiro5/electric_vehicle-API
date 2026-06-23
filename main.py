from fastapi import FastAPI
from routers.telemetry_router import router

app = FastAPI(
    title="Autonomous Vehicle Telemetry API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "Autonomous Vehicle Telemetry API"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }