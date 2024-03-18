from datetime import datetime

from repo.data import Storage
from services.mock_service import MockService
from models.globals import Version

_storage: Storage | None = None


async def get_data_storage():
    global _storage
    if _storage is None:
        _storage = Storage()
    return _storage


def enrich(input: dict, version: Version | None):
    input.update({"version": version | Version.v1, "timestamp": datetime.now()})
