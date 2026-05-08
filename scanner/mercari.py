import requests


def search(keyword, limit=20):
    url = "https://api.mercari.jp/v2/entities:search"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Content-Type": "application/json"
    }

    payload = {
        "keyword": keyword,
        "pageSize": limit,
        "pageToken": ""
    }

    r = requests.post(url, json=payload, headers=headers)

    if r.status_code != 200:
        print("STATUS ERROR:", r.status_code)
        print(r.text)
        return []

    data = r.json()

    items = data.get("items", [])

    results = []

    for i in items:
        try:
            results.append({
                "title": i.get("name"),
                "url": "https://www.mercari.com/jp/items/" + i.get("id", ""),
                "price": i.get("price")
            })
        except:
            continue

    return results
