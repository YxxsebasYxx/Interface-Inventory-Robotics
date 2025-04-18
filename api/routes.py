from fastapi import FastAPI, HTTPException
from services.inventory_service import InventoryService
from repositories.category_repo import CategoryRepo
from repositories.item_repo import ItemRepo

app = FastAPI()

# Inicialización de repositorios y servicio
cat_repo = CategoryRepo()
item_repo = ItemRepo()
service = InventoryService(cat_repo, item_repo)

@app.get("/categories")
def read_categories():
    return service.get_categories()

@app.get("/categories/{cat_id}/items")
def read_items(cat_id: str):
    items = service.get_items_by_category(cat_id)
    if not items:
        raise HTTPException(status_code=404, detail="No items found")
    return items