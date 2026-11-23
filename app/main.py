from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.core.config import get_settings
from app.schemas.common import MessageResponse

settings=get_settings()


app= FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version=settings.api_version
    )

app.include_router(health_router)

@app.get(
    "/",
    response_model=MessageResponse,
    tags=["general"]
    )
async def root():
    return {
         "message": "Enterprise Document Intelligence API is running"
        }
