import json as JSON
import re
import sys
import os

from wordcloud import WordCloud
import get_stopwords as Stopwords


def strip_message(m):
    m = re.sub(r'[\n\r]', ' ', m)
    m = re.sub(r'[\d-]', ' ', m)
    m = re.sub(r'\W', ' ', m)
    m = re.sub(r' +', ' ', m)
    m = m.strip()
    m = m.lower()
    return m


def create_words_dict(msgs, stopwords):
    print("Creating words dictionary...")
    words = {}
    for m in msgs:
        for w in m.split():
            if w not in stopwords:
                if w in words:
                    words[w] += 1
                else:
                    words[w] = 1
    sorted_dict = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}

    return sorted_dict


def load_messages(file):
    with open(file, "r", encoding="utf8") as f:
        print("Loading messages...")
        data = JSON.load(f)
        messages = data["messages"]
        message_texts = []
        for m in messages:
            for text_block in m["text_entities"]:
                if text_block["type"] != "plain":
                    continue
                message_texts.append(strip_message(text_block["text"]))

    return list(filter(lambda x: len(x) > 0, message_texts))


def make_words_list(messages, stopwords):
    print("Making words list...")
    words = []
    for message in messages:
        words.extend(str(message).split(" "))
    words = list(filter(lambda x: len(x) > 2, words))
    words = list(filter(lambda x: x not in stopwords, words))
    return words


def output_wordcloud(words, name, username):
    print("Creating wordcloud...")
    wc = WordCloud(background_color="white",
                   width=1024,
                   height=1024,
                   stopwords=set(),
                   font_path="./assets/DroidSansMono.ttf")
    wc.generate(" ".join(words))
    wc.to_file(f'./output/{username}/{name}_wordcloud.png')


def output_dictionary(words, name, username):
    with open(f"./output/{username}/{name}_words.txt", "w", encoding="utf8") as f:
        for word in words:
            f.write(f"{word} {words[word]}\n")


def run_wordcloud_generator(file_path, username, external_stopwords=None):
    name = os.path.basename(file_path).split(".")[0]
    print("File: " + file_path)
    print("Name: " + name)

    messages = load_messages(file_path)
    print("Messages: " + str(len(messages)))
    stopwords = Stopwords.get_stopwords()
    if external_stopwords is not None:
        stopwords.update(external_stopwords)

    words = make_words_list(messages, stopwords)
    dictionary = create_words_dict(words, stopwords)

    output_dictionary(dictionary, name, username)
    output_wordcloud(words, name, username)
    print("Done")


def main(args):
    if len(args) == 0:
        for file in os.listdir("./data"):
            if file.endswith(".json"):
                run_wordcloud_generator(f"./data/{file}", "local")
    else:
        run_wordcloud_generator(args[0], "local")


if __name__ == '__main__':
    main(sys.argv[1:])
