
import sqlite3, os
from sklearn.datasets import load_iris

DB_PATH = os.path.join("data", "iris.db")

def main():
    os.makedirs("data", exist_ok=True)
    iris = load_iris(as_frame=True)
    df = iris.frame.rename(columns={
        "sepal length (cm)": "sepal_length",
        "sepal width (cm)": "sepal_width",
        "petal length (cm)": "petal_length",
        "petal width (cm)": "petal_width",
        "target": "species_id"
    })
    df["species"] = df["species_id"].map(dict(enumerate(iris.target_names)))
    df = df.drop(columns=["species_id"])

    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS iris (id INTEGER PRIMARY KEY, sepal_length REAL, sepal_width REAL, petal_length REAL, petal_width REAL, species TEXT)")
    cur.execute("DELETE FROM iris")
    cur.executemany(
        "INSERT INTO iris (sepal_length, sepal_width, petal_length, petal_width, species) VALUES (?, ?, ?, ?, ?)",
        df[["sepal_length","sepal_width","petal_length","petal_width","species"]].itertuples(index=False, name=None)
    )
    con.commit()
    con.close()
    print(f"Ingested {len(df)} rows into {DB_PATH}")

if __name__ == "__main__":
    main()
