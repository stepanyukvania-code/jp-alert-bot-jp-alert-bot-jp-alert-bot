import time
import json
import threading

from config import INTERVAL
from scanner.mercari import search
from services.telegram import send
from bot.telegram_bot import run as telegram_run


QUERY_FILE = "data/queries.json"
SEEN_FILE = "data/seen.json"


def load_queries():
    try:
        with open(QUERY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def load_seen():
    try:
        with open(SEEN_FILE, "r", encoding="utf-8") as f:
            return set(json.load(f))
    except:
        return set()


def save_seen(seen):
    with open(SEEN_FILE, "w", encoding="utf-8") as f:
        json.dump(list(seen), f, ensure_ascii=False)


def format_item(i):
    return f"{i['title']}\n{i['price']}\n{i['url']}"


def run_scan():
    seen = load_seen()

    while True:
        queries = load_queries()

        print("SCAN:", queries)

        for q in queries:
            items = search(q)

            print("RESULT:", items)

            for i in items:
                if not i.get("id"):
                    continue

                if i["id"] in seen:
                    continue

                seen.add(i["id"])
                send(format_item(i))

        save_seen(seen)
        time.sleep(INTERVAL)


if __name__ == "__main__":
    from config import TELEGRAM_TOKEN

    threading.Thread(target=run_scan, daemon=True).start()
    telegram_run(TELEGRAM_TOKEN)
