from backend.data.models import SubCategory
from typing import List

class SubCategoryRepo:
    def __init__(self):
        self._subcats: List[SubCategory] = []

    def add(self, sc: SubCategory):
        self._subcats.append(sc)

    def list_all(self) -> List[SubCategory]:
        return self._subcats

    def list_by_category(self, cat_id: str) -> List[SubCategory]:
        return [s for s in self._subcats if s.category_id == cat_id]