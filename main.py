from scanner.mercari import search
from services.telegram import send

print("BOT START")

results = search("iphone")

print("RESULTS:", results)
print("LEN RESULTS:", len(results))

for r in results:
    text = f"{r.get('title')} - {r.get('price')}"
    send(text)

print("BOT END")
