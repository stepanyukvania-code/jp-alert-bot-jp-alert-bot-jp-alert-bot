import requests


def search(keyword, limit=20):
    url = "https://www.mercari.com/jp/api/v1/search"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = {
        "keyword": keyword,
        "limit": limit,
        "page": 1,
        "sort": "score"
    }

    r = requests.post(url, json=payload, headers=headers)

    if r.status_code != 200:
        print("STATUS:", r.status_code)
        print("RAW:", r.text)
        return []

    data = r.json()

    items = data.get("items", [])

    results = []

    for i in items:
        results.append({
            "title": i.get("name"),
            "price": i.get("price"),
            "url": "https://www.mercari.com/jp/items/" + i.get("id", "")
        })

    return results
