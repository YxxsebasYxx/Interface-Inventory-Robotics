from dataclasses import dataclass

@dataclass
class Category:
    id: str
    name: str

@dataclass
class Item:
    id: str
    category_id: str
    name: str
    quantity: int