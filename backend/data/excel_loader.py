import pandas as pd
from .models import Category, SubCategory, Item, SubItem

# Funciones auxiliares para limpiar valores

def safe_str(val):
    return str(val).strip() if pd.notna(val) else ""

def safe_int(val):
    return int(val) if pd.notna(val) else 0


def load_inventory_from_excel(path: str):
    df = pd.read_excel(path)

    categories = {}
    subcategories = {}
    items = {}
    subitems = []

    for _, row in df.iterrows():
        c_id = safe_str(row['Grupo'])
        c_name = safe_str(row['GrupoName'])
        if c_id and c_id not in categories:
            categories[c_id] = Category(id=c_id, name=c_name)

        sc_raw = safe_str(row['SubGrupo'])
        sc_id = f"{c_id}-{sc_raw}" if sc_raw else ""
        sc_name = safe_str(row['SubGrupoName'])
        if sc_raw and sc_id not in subcategories:
            subcategories[sc_id] = SubCategory(
                id=sc_id,
                category_id=c_id,
                name=sc_name
            )

        i_raw = safe_str(row['Item'])
        i_id = f"{sc_id}-{i_raw}" if i_raw else ""
        i_name = safe_str(row['ItemName'])
        qty = safe_int(row['Quantity'])
        if i_raw and i_id not in items:
            items[i_id] = Item(
                id=i_id,
                subcategory_id=sc_id,
                name=i_name,
                quantity=qty
            )

        si_raw = safe_str(row['SubItem'])
        si_id = f"{i_id}-{si_raw}" if si_raw else ""
        si_name = safe_str(row['SubItemName'])
        qty2 = safe_int(row['Quantity2'])
        if si_raw:
            subitems.append(SubItem(
                id=si_id,
                item_id=i_id,
                name=si_name,
                quantity=qty2
            ))

    return (
        list(categories.values()),
        list(subcategories.values()),
        list(items.values()),
        subitems
    )