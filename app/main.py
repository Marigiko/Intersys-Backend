from fastapi import FastAPI
from app.api.v1.router import api_router

app = FastAPI(
    title="Intersys API",
    version="1.0.0",
    description="API for Intersys application",
)

app.include_router(api_router, prefix="/api/v1")