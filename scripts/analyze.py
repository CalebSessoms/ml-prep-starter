
import sqlite3, pandas as pd

DB_PATH = "data/iris.db"

def query_df(sql):
    with sqlite3.connect(DB_PATH) as con:
        return pd.read_sql_query(sql, con)

def main():
    top_species = query_df("SELECT species, COUNT(*) AS n FROM iris GROUP BY species ORDER BY n DESC LIMIT 10")
    print("\nTop species by count:")
    print(top_species.to_string(index=False))

    avg_sepal = query_df("SELECT species, AVG(sepal_length) AS avg_sepal_length FROM iris GROUP BY species ORDER BY avg_sepal_length DESC")
    print("\nAverage sepal_length by species:")
    print(avg_sepal.to_string(index=False))

if __name__ == "__main__":
    main()
