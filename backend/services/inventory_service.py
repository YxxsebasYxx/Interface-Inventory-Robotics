from backend.repositories.category_repo import CategoryRepo
from backend.repositories.subcategory_repo import SubCategoryRepo
from backend.repositories.item_repo import ItemRepo
from backend.repositories.subitem_repo import SubItemRepo
from typing import List, Dict, Any
import re

class InventoryService:
    def __init__(
        self,
        cat_repo: CategoryRepo,
        subcat_repo: SubCategoryRepo,
        item_repo: ItemRepo,
        subitem_repo: SubItemRepo
    ):
        self.cat_repo = cat_repo
        self.subcat_repo = subcat_repo
        self.item_repo = item_repo
        self.subitem_repo = subitem_repo

    def get_categories(self):
        return self.cat_repo.list_all()

    def get_subcategories(self, cat_id: str):
        return self.subcat_repo.list_by_category(cat_id)

    def get_items(self, subcat_id: str):
        return self.item_repo.list_by_subcategory(subcat_id)

    def get_subitems(self, item_id: str):
        return self.subitem_repo.list_by_item(item_id)

    def search(self, pattern: str) -> Dict[str, Any]:
        regex = re.compile(pattern, re.IGNORECASE)
        return {
            'categories': [c for c in self.cat_repo.list_all() if regex.search(c.name)],
            'subcategories': [s for s in self.subcat_repo.list_all() if regex.search(s.name)],
            'items': [i for i in self.item_repo.list_all() if regex.search(i.name)],
            'subitems': [si for si in self.subitem_repo.list_all() if regex.search(si.name)],
        }