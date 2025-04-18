from repositories.category_repo import CategoryRepo
from repositories.item_repo import ItemRepo
import re
import pandas as pd

class InventoryService:
    def __init__(self, cat_repo: CategoryRepo, item_repo: ItemRepo):
        self.cat_repo = cat_repo
        self.item_repo = item_repo

    def get_categories(self):
        return self.cat_repo.list_all()

    def get_items_by_category(self, cat_id: str):
        return self.item_repo.find_by_category(cat_id)

    def search_items(self, grupo: str = None, subgrupo: str = None, regex: str = None):
        df = self.item_repo.find_all()  # Este método debe devolver un DataFrame con todos los ítems

        resultados = df

        if grupo:
            resultados = resultados[resultados['Grupo'].astype(str).str.contains(grupo, case=False, na=False)]

        if subgrupo:
            resultados = resultados[resultados['Subgrupo'].astype(str).str.contains(subgrupo, case=False, na=False)]

        if regex:
            columnas_buscar = ['Descripción', 'Nombre del Ítem']  # Ajusta esto según tus columnas reales
            mask = resultados[columnas_buscar[0]].astype(str).str.contains(regex, flags=re.IGNORECASE, regex=True)
            for col in columnas_buscar[1:]:
                mask |= resultados[col].astype(str).str.contains(regex, flags=re.IGNORECASE, regex=True)
            resultados = resultados[mask]

        return resultados
