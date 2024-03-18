from fastapi import APIRouter

from models.globals import Version
from routers.common import enrich


router = APIRouter(prefix="/{version}/service")

@router.get("/health")
async def read_root(version: Version):
    result = {"status": "up"}
    enrich(result, version)
    return result


