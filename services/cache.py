import json
import os

FILE = "data/seen.json"

def load():
    if not os.path.exists(FILE):
        return set()
    return set(json.load(open(FILE)))

def save(data):
    json.dump(list(data), open(FILE, "w"))
