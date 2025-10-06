# scripts/fetch_reviews.py
# Fetches real Steam reviews for a given AppID and saves them as JSON (no DB writes yet).

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

APPID = 413150  # Stardew Valley
PAGES = 3       # number of pages to fetch (100 reviews per page); increase later if you want
PER_PAGE = 100

OUT_DIR = Path("data")
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = OUT_DIR / f"steam_{APPID}_reviews.json"

def fetch_page(appid: int, cursor: str, per_page: int = 100, language: str = "english"):
    base = f"https://store.steampowered.com/appreviews/{appid}"
    params = {
        "json": 1,
        "num_per_page": per_page,
        "language": language,
        "filter": "recent",        # recent reviews; you can change to 'updated' or remove
        "purchase_type": "all",    # include all purchase types
        "cursor": cursor,
    }
    url = base + "?" + urllib.parse.urlencode(params)
    with urllib.request.urlopen(url) as resp:
        return json.loads(resp.read().decode("utf-8"))

def main():
    all_reviews = []
    cursor = "*"  # required starting cursor per Valve’s API
    for page in range(1, PAGES + 1):
        data = fetch_page(APPID, cursor, PER_PAGE)
        if data.get("success") != 1:
            print(f"[page {page}] API returned non-success. Stopping.")
            break

        reviews = data.get("reviews", [])
        if not reviews:
            print(f"[page {page}] No more reviews. Stopping.")
            break

        all_reviews.extend(reviews)
        cursor = data.get("cursor", cursor)  # next cursor for pagination
        print(f"[page {page}] fetched {len(reviews)} reviews (total so far: {len(all_reviews)}).")

        # be polite to the API
        time.sleep(1.0)

    # Save raw reviews JSON so you can inspect it before ingesting to DB
    with OUT_PATH.open("w", encoding="utf-8") as f:
        json.dump(all_reviews, f, ensure_ascii=False, indent=2)

    print(f"\nSaved {len(all_reviews)} reviews to {OUT_PATH}")

if __name__ == "__main__":
    main()
