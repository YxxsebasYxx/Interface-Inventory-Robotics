import pandas as pd
from .models import Category, Item

def load_inventory_from_excel(path: str):
    df = pd.read_excel(path)
    categories = {}
    items = []

    for _, row in df.iterrows():
        cat_id = str(row['Group'])
        cat_name = row['GroupName']
        if cat_id not in categories:
            categories[cat_id] = Category(id=cat_id, name=cat_name)

        item = Item(
            id=str(row['ItemID']),
            category_id=cat_id,
            name=row['ItemName'],
            quantity=int(row['Quantity'])
        )
        items.append(item)

    return list(categories.values()), items