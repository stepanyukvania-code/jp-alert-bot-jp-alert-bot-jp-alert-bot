
import json

from scanner.mercari import search
from services.telegram import send
from store import load_queries

SEEN_FILE = "data/seen.json"


def load_seen():
    try:
        with open(SEEN_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    except:
        return set()


def save_seen(seen):
    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(list(seen), f)


def format_item(i):
    return f"{i['title']}\n{i['price']}\n{i['url']}"


def run_scan_once():
    seen = load_seen()
    queries = load_queries()

    for q in queries:
        items = search(q)

        for i in items:
            if not i.get("id"):
                continue

            if i["id"] in seen:
                continue

            seen.add(i["id"])
            send(format_item(i))

    save_seen(seen)


if __name__ == "__main__":
    run_scan_once()
