import requests
import re
import json


def search(keyword, limit=20):
    url = f"https://www.mercari.com/jp/search/?keyword={keyword}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    html = r.text

    # пробуємо витягнути JSON з сторінки
    match = re.search(r'window\.__INITIAL_STATE__\s*=\s*({.*?});', html)

    if not match:
        print("NO DATA FOUND")
        return []

    try:
        data = json.loads(match.group(1))
    except:
        print("JSON PARSE ERROR")
        return []

    print("DATA FOUND")

    return []
