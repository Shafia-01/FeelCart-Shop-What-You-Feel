import requests

API_KEY = "5acd29613909b7e659da2c4e9159fab088f6c59af927c9e9d3895e35b786b862"  # Set this in your environment
BASE_URL = "https://serpapi.com/search.json"

def fetch_trending_products(query, num_results=5):
    if not API_KEY:
        print("❌ API key not set")
        return []

    params = {
        "engine": "walmart",
        "query": query,
        "api_key": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    print(f"🔍 DEBUG [{query}] keys: {list(data.keys())}")

    results = []
    organic = data.get("organic_results", [])
    if not organic:
        print("❌ No organic results found.")
        return []

    print(f"🧪 First raw item for [{query}]: {organic[0]}")  # <— Add this line to see structure

    for item in organic[:num_results]:
        results.append ({
            "title": item.get("title", "N/A"),
            "link": item.get("link") or f"https://www.walmart.com/search?q={query.replace(' ', '+')}",
            "price": item.get("price")})

    return results
