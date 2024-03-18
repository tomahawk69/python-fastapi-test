import logging
from fastapi import FastAPI
from repo.data import Storage
from routers.items import router as items_router
from routers.service import router as service_router
from routers.posts import router as service_posts

logging.basicConfig(format="%(levelname)s:     %(name)s: %(message)s", level=logging.INFO)

app = FastAPI()

app.include_router(items_router)
app.include_router(service_router)
app.include_router(service_posts)

