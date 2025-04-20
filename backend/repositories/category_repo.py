from backend.data.models import Category
from typing import List, Optional

class CategoryRepo:
    def __init__(self):
        self._cats: List[Category] = []

    def add(self, c: Category):
        self._cats.append(c)

    def list_all(self) -> List[Category]:
        return self._cats

    def find_by_id(self, cat_id: str) -> Optional[Category]:
        return next((c for c in self._cats if c.id == cat_id), None)