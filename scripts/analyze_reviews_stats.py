# scripts/analyze_reviews_stats.py
# Produces basic numeric/statistical summaries of your Steam reviews data.

import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path("data") / "iris.db"

def query_df(sql):
    with sqlite3.connect(DB_PATH) as con:
        return pd.read_sql_query(sql, con)

def main():
    print("\n--- Steam Reviews Statistical Summary ---\n")

    # 1️⃣ total reviews
    total = query_df("SELECT COUNT(*) AS total_reviews FROM steam_reviews")
    print(total.to_string(index=False))

    # 2️⃣ positive vs negative
    posneg = query_df("""
        SELECT 
            CASE voted_up WHEN 1 THEN 'Positive' ELSE 'Negative' END AS sentiment,
            COUNT(*) AS count,
            ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM steam_reviews), 1) AS percent
        FROM steam_reviews
        GROUP BY voted_up
        ORDER BY count DESC
    """)
    print("\nReview sentiment breakdown:")
    print(posneg.to_string(index=False))

    # 3️⃣ average playtime by sentiment
    avg_play = query_df("""
        SELECT 
            CASE voted_up WHEN 1 THEN 'Positive' ELSE 'Negative' END AS sentiment,
            ROUND(AVG(playtime), 1) AS avg_playtime_minutes
        FROM steam_reviews
        GROUP BY voted_up
    """)
    print("\nAverage playtime (minutes) by sentiment:")
    print(avg_play.to_string(index=False))

    # 4️⃣ average number of games owned by sentiment
    avg_owned = query_df("""
        SELECT 
            CASE voted_up WHEN 1 THEN 'Positive' ELSE 'Negative' END AS sentiment,
            ROUND(AVG(num_games_owned), 1) AS avg_games_owned
        FROM steam_reviews
        GROUP BY voted_up
    """)
    print("\nAverage number of games owned by sentiment:")
    print(avg_owned.to_string(index=False))

    print("\n------------------------------------------\n")

if __name__ == "__main__":
    main()
