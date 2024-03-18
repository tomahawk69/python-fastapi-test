from logging import getLogger
import requests

from models.globals import Post


BASE_URL = 'https://jsonplaceholder.typicode.com/fa/v1'


class MockService():
    _domain: str
    _logger = getLogger(__name__)
    def __init__(self, domain: str):
        self._domain = domain
    
    async def add_item(self, item: dict):
        return await requests.post(BASE_URL.join(self._domain), data=item)
    
    async def get_item(self, itemId: str):
        return await requests.get(BASE_URL.join(self._domain, '/', itemId))
    
    async def get_items(self) -> list[Post] :
        result = requests.get(BASE_URL.join(self._domain)).content
        self._logger.info("Get items", result)
        return result
