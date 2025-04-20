from dataclasses import dataclass

@dataclass
class Category:
    id: str
    name: str

@dataclass
class SubCategory:
    id: str
    category_id: str
    name: str

@dataclass
class Item:
    id: str
    subcategory_id: str
    name: str
    quantity: int

@dataclass
class SubItem:
    id: str
    item_id: str
    name: str
    quantity: int