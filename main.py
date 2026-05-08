from scanner.mercari import search
from services.telegram import send

results = search("iphone")

for r in results:
    send(f"{r['title']} | {r['url']}")
