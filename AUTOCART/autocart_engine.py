import json
from typing import List, Dict
from AUTOCART.walmart_api import fetch_trending_products
from AUTOCART.autocart_rules import get_top_n_items, needs_refill, get_category

def generate_autocart(user_data: List[Dict], top_n: int = 5) -> List[Dict]:
    top_items = get_top_n_items(user_data, top_n)
    cart = []

    for item in top_items:
        if not needs_refill(user_data, item):
            continue
        category = get_category(item)
        suggestions = fetch_trending_products(item, num_results=5)
        if suggestions:
            top = suggestions[0]
            cart.append({
                "item": item,
                "suggested": {
                    "title": top.get("title"),
                    "link": top.get("link")
                },
                "category": category
            })
    return cart

if __name__ == "__main__":
    with open("user_history.json", "r") as f:
        user_data = json.load(f)

    result = {}
    for i, (user, data) in enumerate(user_data.items(), start=1):
        cart = generate_autocart(data)
        result[user] = cart
        print(f"🛒 AutoCart for {user}:")
        for entry in cart:
            print(f"  • {entry['item']} → {entry['suggested']['title']} ({entry['suggested'].get('link')}) [{entry['category']}]")
        print()

    with open("autocart_results.json", "w") as f:
        json.dump(result, f, indent=4)
    print("✅ AutoCart data exported to: autocart_results.json")
