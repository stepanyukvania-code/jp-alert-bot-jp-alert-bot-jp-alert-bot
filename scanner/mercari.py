import requests
import re


BASE_URL = "https://www.mercari.com/jp/search/"


def search(keyword, limit=20):
    try:
        url = f"{BASE_URL}?keyword={requests.utils.quote(keyword)}"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        r = requests.get(url, headers=headers, timeout=10)
        html = r.text

        matches = re.findall(r'/jp/items/([a-zA-Z0-9]+)/', html)

        results = []
        seen = set()

        for item_id in matches:
            if item_id in seen:
                continue

            seen.add(item_id)

            results.append({
                "id": item_id,
                "title": keyword,
                "price": "",
                "url": f"https://www.mercari.com/jp/items/{item_id}/"
            })

            if len(results) >= limit:
                break

        return results

    except Exception as e:
        print("MERCARI ERROR:", e)
        return []
