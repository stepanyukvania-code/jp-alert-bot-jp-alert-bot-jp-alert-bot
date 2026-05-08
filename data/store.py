import json
import os

FILE = "queries.json"


def load_queries():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []


def save_queries(q):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(q, f, ensure_ascii=False)
