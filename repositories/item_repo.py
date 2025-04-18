from data.models import Item

class ItemRepo:
    def __init__(self):
        self._items: list[Item] = []

    def add(self, item: Item):
        self._items.append(item)

    def find_by_category(self, category_id: str) -> list[Item]:
        return [i for i in self._items if i.category_id == category_id]