from fastapi import APIRouter

from app.models.schemas_tortoise.status import Status

router = APIRouter()


@router.get("/status", response_model=Status, name="status_ping")
async def get_ping() -> Status:
    return Status(status=True)
