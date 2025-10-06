
from transformers import pipeline

MODEL_NAME = "distilbert-base-uncased-finetuned-sst-2-english"

def main():
    clf = pipeline("sentiment-analysis", model=MODEL_NAME)
    examples = [
        "I love this course!",
        "This assignment is difficult but interesting.",
        "I dislike bugs in my code."
    ]
    for t in examples:
        result = clf(t)[0]
        print(f"{t!r} -> label={result['label']}, score={result['score']:.3f}")

if __name__ == "__main__":
    main()
