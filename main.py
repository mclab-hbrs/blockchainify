#!/usr/bin/env python
import argparse
import random
import sys
import os


if sys.version_info.major < 3:
    print("This program requires Python 3.", file=sys.stderr)
    sys.exit(1)


LANG_MANGLING = {
    "DE": lambda word, tech_word: " " + tech_word + "-" + word + " ",
    "EN": lambda word, tech_word: " " + tech_word + " " + word + " "
}
LANGS = list(LANG_MANGLING.keys())
WORDLIST_DIR = "word_lists"


parser = argparse.ArgumentParser()
parser.add_argument("textfile", help="File to blockchainify.")
parser.add_argument("-l", "--lang", default=LANGS[0], choices=LANGS, help="language to use.")
args = parser.parse_args()


def read_file(file_name):
    try:
        return open(file_name).read()
    except FileNotFoundError:
        print(f"File '{file_name}' does not exist.", file=sys.stderr)
        sys.exit(1)


def read_wordlist(lang, suffix=""):
    wl_path = os.path.join(WORDLIST_DIR, lang + suffix)
    return read_file(wl_path).split("\n")


def main():
    text_file = args.textfile
    text = read_file(text_file)

    lang_words = read_wordlist(args.lang)
    tech_words = read_wordlist(args.lang, "_tech")

    for word in lang_words:
        text = text.replace(" " + word + " ", LANG_MANGLING[args.lang](word, random.choice(tech_words)))

    print(text)


if __name__ == '__main__':
    main()
