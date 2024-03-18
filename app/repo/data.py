from app.models.globals import Item
from datetime import datetime


class Storage:
    __data: dict[int, Item] = dict()

    def add(self, itemId: int, item: Item) -> bool:
        add = item.model_copy()
        add.created = datetime.now()
        return self.__data.setdefault(itemId, add) == add

    def get(self, itemId: int) -> Item:
        return self.__data.get(itemId)

    def getAll(self):
        return self.__data.items()
