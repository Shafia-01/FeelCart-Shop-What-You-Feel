from collections import Counter
from typing import List, Dict

CATEGORY_MAPPING = {
    "banana": "fruits",
    "milk": "dairy",
    "bread": "bakery",
    "detergent": "cleaning",
    "coffee": "beverages",
    "toilet paper": "cleaning",
    "cheese": "dairy"
}

def get_top_n_items(user_data: List[Dict], n: int = 5) -> List[str]:
    items = [entry["item"] for entry in user_data]
    counter = Counter(items)
    return [item for item, _ in counter.most_common(n)]

def needs_refill(user_data: List[Dict], item: str) -> bool:
    return True  # Placeholder logic

def get_category(item: str) -> str:
    return CATEGORY_MAPPING.get(item.lower(), "others")