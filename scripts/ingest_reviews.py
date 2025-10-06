# scripts/ingest_reviews.py
# Reads JSON reviews saved by fetch_reviews.py and inserts them into SQLite.

import json
import os
import sqlite3
from pathlib import Path

APPID = 413150  # Stardew Valley
DB_PATH = Path("data") / "iris.db"  # reuse existing SQLite db
JSON_PATH = Path("data") / f"steam_{APPID}_reviews.json"

def main():
    if not JSON_PATH.exists():
        raise FileNotFoundError(f"JSON file not found: {JSON_PATH}. Run scripts/fetch_reviews.py first.")

    # Load JSON array of reviews
    with JSON_PATH.open("r", encoding="utf-8") as f:
        reviews = json.load(f)
    print(f"Loaded {len(reviews)} reviews from {JSON_PATH}")

    # Connect to SQLite
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    # Create table for steam reviews (id autoinc, recommendationid unique to avoid duplicates)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS steam_reviews (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recommendationid TEXT UNIQUE,
            review_text TEXT,
            voted_up INTEGER,
            playtime INTEGER,
            num_games_owned INTEGER,
            timestamp INTEGER,
            language TEXT
        )
    """)

    # Prepare rows (filter to English; handle missing fields safely)
    rows = []
    for r in reviews:
        lang = r.get("language") or ""
        if lang.lower() != "english":
            continue

        rec_id = str(r.get("recommendationid", ""))
        text = (r.get("review") or "").strip()
        voted = 1 if r.get("voted_up") else 0

        author = r.get("author") or {}
        playtime = int(author.get("playtime_forever") or 0)
        num_owned = int(author.get("num_games_owned") or 0)
        ts = int(r.get("timestamp_created") or 0)

        if rec_id:  # skip if no id
            rows.append((rec_id, text, voted, playtime, num_owned, ts, lang))

    print(f"Prepared {len(rows)} English rows for insert")

    # Insert, ignoring duplicates by recommendationid
    cur.executemany(
        """
        INSERT OR IGNORE INTO steam_reviews
        (recommendationid, review_text, voted_up, playtime, num_games_owned, timestamp, language)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        rows
    )
    con.commit()

    # Show how many were inserted
    cur.execute("SELECT COUNT(*) FROM steam_reviews")
    total = cur.fetchone()[0]
    print(f"Total rows now in steam_reviews: {total}")

    con.close()
    print(f"Done. Data stored in {DB_PATH}")

if __name__ == "__main__":
    main()
