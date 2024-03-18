from logging import getLogger, Logger, INFO
from typing import Annotated
from fastapi import APIRouter, Depends

from services.mock_service import MockService
from models.globals import Version

_DOMAIN = 'posts'
_posts_service: MockService | None = None
_logger = getLogger("posts.routing")

router = APIRouter(prefix=f'/{Version.v1.value}/{_DOMAIN}')
async def get_logger():
    global _logger
    return _logger

async def get_service():
    global _posts_service
    if _posts_service is None:
        _posts_service = MockService(_DOMAIN)
    return _posts_service


@router.get(path="/")
async def get_all(service: Annotated[MockService, Depends(get_service)],
                  logger: Annotated[Logger, Depends(get_logger)]):
    logger.info('get all')
    return service.get_items()

@router.get(path="/{itemId}")
async def get_all(itemId: str, service: Annotated[MockService, Depends(get_service)]):
    return await service.get_item(itemId)
