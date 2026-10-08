"""Dump the API's data to penguins.json for the static page.
Run while the API is up:  python export_static.py
"""
import json

import httpx

BASE = "http://127.0.0.1:8000/api/v1"

with httpx.Client(timeout=15) as c:
    ids = [p["id"] for p in c.get(f"{BASE}/penguins", params={"limit": 100}).json()]
    data = [c.get(f"{BASE}/penguins/{i}").json() for i in ids]

with open("penguins.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print(f"Wrote {len(data)} species to penguins.json")
