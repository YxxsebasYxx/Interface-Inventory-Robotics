from backend.data.models import Item
from typing import List

class ItemRepo:
    def __init__(self):
        self._items: List[Item] = []

    def add(self, item: Item):
        self._items.append(item)

    def list_all(self) -> List[Item]:
        return self._items

    def list_by_subcategory(self, subcat_id: str) -> List[Item]:
        return [i for i in self._items if i.subcategory_id == subcat_id]