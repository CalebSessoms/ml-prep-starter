# scripts/analyze_reviews_text.py
# Finds the most common words used in positive vs negative Steam reviews.

import sqlite3, re
from collections import Counter
from pathlib import Path

DB_PATH = Path("data") / "iris.db"

# A simple English stopword list (can expand later)
STOPWORDS = {
    "the","a","an","and","or","but","if","then","else","when","while","for","to","of","in","on","at","by","with","as",
    "is","am","are","was","were","be","been","being","do","does","did","doing","have","has","had","having",
    "it","its","itself","this","that","these","those","there","here","i","me","my","myself","we","our","ours","ourselves",
    "you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","they","them",
    "their","theirs","themselves","who","whom","which","what","why","how","from","up","down","out","over","under","again",
    "further","then","once","same","so","too","very","can","could","should","would","will","just","also","than","into",
    "about","because","not","no","yes","all","any","both","each","few","more","most","other","some","such","only","own",
    "s","t","ll","re","ve","d","m","y","im","ive","youre","youve","cant","dont","didnt","doesnt","wont","wasnt","isnt",
    "games","game","play","played","playing","hours","hour","minute","minutes","time"  # filter generic gaming words
}

WORD_RE = re.compile(r"[a-z']+")

def tokenize(text: str):
    # Lowercase, keep alphabetic words and simple apostrophes (e.g., don't -> dont)
    text = text.lower().replace("’", "'")
    words = WORD_RE.findall(text)
    # Normalize basic contractions
    words = [w.replace("'", "") for w in words]
    return [w for w in words if w and w not in STOPWORDS and len(w) > 2]

def fetch_reviews():
    with sqlite3.connect(DB_PATH) as con:
        cur = con.cursor()
        cur.execute("SELECT review_text, voted_up FROM steam_reviews WHERE review_text IS NOT NULL AND LENGTH(review_text) > 0")
        return cur.fetchall()

def main():
    rows = fetch_reviews()
    pos_counter, neg_counter = Counter(), Counter()
    pos_tokens = neg_tokens = 0

    for text, voted_up in rows:
        tokens = tokenize(text or "")
        if voted_up == 1:
            pos_counter.update(tokens)
            pos_tokens += len(tokens)
        else:
            neg_counter.update(tokens)
            neg_tokens += len(tokens)

    def print_top(title, counter, total_tokens, n=15):
        print(f"\n{title}")
        print("-" * len(title))
        print(f"Total tokens: {total_tokens}")
        for word, count in counter.most_common(n):
            print(f"{word:<15} {count}")

    print("\n--- Steam Reviews Text Analysis ---")
    print_top("Positive reviews: top words", pos_counter, pos_tokens)
    print_top("Negative reviews: top words", neg_counter, neg_tokens)
    print("\n-----------------------------------")

if __name__ == "__main__":
    main()
