from fastapi import APIRouter, HTTPException, Query
from backend.config.settings import EXCEL_PATH
from backend.data.excel_loader import load_inventory_from_excel
from backend.repositories.category_repo import CategoryRepo
from backend.repositories.subcategory_repo import SubCategoryRepo
from backend.repositories.item_repo import ItemRepo
from backend.repositories.subitem_repo import SubItemRepo
from backend.services.inventory_service import InventoryService

router = APIRouter()

# Cargar datos y poblar repositorios
cats, subcats, items, subitems = load_inventory_from_excel(EXCEL_PATH)
cat_repo = CategoryRepo()
subcat_repo = SubCategoryRepo()
item_repo = ItemRepo()
subitem_repo = SubItemRepo()

for c in cats: cat_repo.add(c)
for sc in subcats: subcat_repo.add(sc)
for i in items: item_repo.add(i)
for si in subitems: subitem_repo.add(si)

service = InventoryService(cat_repo, subcat_repo, item_repo, subitem_repo)

@router.get("/", tags=["root"])
def root():
    return {"message": "Inventory API running"}

@router.get("/categories", tags=["categories"])
def list_categories():
    return service.get_categories()

@router.get("/categories/{cat_id}/subcategories", tags=["categories"])
def list_subcategories(cat_id: str):
    res = service.get_subcategories(cat_id)
    if not res:
        raise HTTPException(404, "No subcategories found")
    return res

@router.get("/subcategories/{subcat_id}/items", tags=["items"])
def list_items(subcat_id: str):
    res = service.get_items(subcat_id)
    if not res:
        raise HTTPException(404, "No items found")
    return res

@router.get("/items/{item_id}/subitems", tags=["subitems"])
def list_subitems(item_id: str):
    res = service.get_subitems(item_id)
    if not res:
        raise HTTPException(404, "No subitems found")
    return res

@router.get("/search", tags=["search"])
def search(q: str = Query(..., description="Pattern to search across all levels")):
    return service.search(q)