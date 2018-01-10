""" https://twitter.com/qikipedia/status/951061069568626688 """
import re

A = ord('a')
Z = ord('z')

CYPHER = lambda ch: chr(Z - ord(ch) + A)
CLEAN_UP = re.compile('[a-z]+')
WORDS_FILE = "words.txt"

def check_word(word):
    clean_word = CLEAN_UP.match(word).group()
    cyphyer_word = "".join(map(CYPHER, clean_word))
    backwards_word = clean_word[::-1]
    return cyphyer_word == backwards_word


def get_wizard_words(words_file):
    with open(words_file) as w_f:
        words = w_f.readlines()
        wizard_words = filter(check_word, words)
    return list(wizard_words)


if __name__ == "__main__":
    wizard_words = get_wizard_words(WORDS_FILE)
    for wizard_word in wizard_words:
        print(CLEAN_UP.match(wizard_word).group())
