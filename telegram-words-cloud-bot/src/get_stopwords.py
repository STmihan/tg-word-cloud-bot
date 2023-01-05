import os


def get_stopwords() -> set:
    stopwords_files = os.listdir("./stopwords")
    stopwords = set()
    for file in stopwords_files:
        with open(f"./stopwords/{file}", "r", encoding="utf8") as f:
            stopwords.update(f.read().splitlines())

    return stopwords
