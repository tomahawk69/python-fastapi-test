from typing import Annotated
from fastapi import APIRouter, Cookie, Header, Response, Path, status, Depends, HTTPException
from uuid import UUID

from models.globals import Version, Item
from routers.common import enrich
from globals import get_data_storage
from repo.data import Storage

router = APIRouter(prefix=f'/{Version.v1.value}/items')


@router.get("/me", response_model_exclude_unset=True, response_model_exclude_none=True)
async def read_item(
    q: str = "current user",
    id: Annotated[str | None, Cookie()] = None,
    correlation_id: Annotated[UUID | None, Header()] = None,
):
    result = {"userName": q, "id": id, "correlation_id": correlation_id}
    enrich(result, None)
    return result


@router.get("/{itemId}")
async def read_item(
    itemId: Annotated[int, Path(title="The ID of the item to get", ge=1)],
    stor: Annotated[Storage, Depends(get_data_storage)]
):
    item = stor.get(itemId)
    if item == None:
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        result = {"itemId": itemId, **item.model_dump()}
    enrich(result, None)
    return result


@router.get("/", response_model=list[dict])
async def get_all(stor: Annotated[Storage, Depends(get_data_storage)]):
    return list(
        map(lambda k: {"itemId": k[0], **k[1].model_dump()}, list(stor.getAll()))
    )


@router.post("/{itemId}", status_code=status.HTTP_201_CREATED)
async def add_item(
    itemId: Annotated[int, Path(title="The ID of the item to get", ge=1)],
    item: Item,
    stor: Annotated[Storage, Depends(get_data_storage)]
):
    if not stor.add(itemId, item):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Item already exists")
    result = {"itemId": itemId, **stor.get(itemId).model_dump()}
    enrich(result, None)
    return result
