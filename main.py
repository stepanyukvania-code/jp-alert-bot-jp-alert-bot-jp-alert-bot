print("START")

from scanner.mercari import search
from services.telegram import send

print("IMPORT OK")

results = search("iphone")

print("RESULTS COUNT:", len(results))
print("RESULTS:", results)

if not results:
    send("NO RESULTS FOUND")
else:
    for r in results:
        send(f"{r['title']} | {r['url']}")

print("END")
