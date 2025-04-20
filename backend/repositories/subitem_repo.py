from backend.data.models import SubItem
from typing import List

class SubItemRepo:
    def __init__(self):
        self._subitems: List[SubItem] = []

    def add(self, si: SubItem):
        self._subitems.append(si)

    def list_all(self) -> List[SubItem]:
        return self._subitems

    def list_by_item(self, item_id: str) -> List[SubItem]:
        return [s for s in self._subitems if s.item_id == item_id]