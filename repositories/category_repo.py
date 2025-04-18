from data.models import Category

class CategoryRepo:
    def __init__(self):
        self._cats: list[Category] = []

    def add(self, category: Category):
        self._cats.append(category)

    def list_all(self) -> list[Category]:
        return self._cats