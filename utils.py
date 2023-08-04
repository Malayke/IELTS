import re
import json
import enchant
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


def get_wordnet_pos(word):
    """Map POS tag to first character lemmatize() accepts"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


def is_english_word(word):
    if not word or word == ' ':
        return False
    # if word.endswith("'s"):
    #     word = word[:-2]
    lemmatizer = WordNetLemmatizer()
    d = enchant.Dict("en_UK")
    word = lemmatizer.lemmatize(word, get_wordnet_pos(word))
    return d.check(word)


def is_english_compound_word(compound_word):
    return all(is_english_word(word) for word in compound_word.split())

def has_multiple_uppercase(s):
    return sum(1 for c in s if c.isupper()) > 1

def is_alpha_string(s: str):
    # Return False if the string is empty
    if not s or s == ' ':
        return False
    if has_multiple_uppercase(s):
        return False
    # detect like `zjH` `vJt` incorrect words 
    if sum(1 for c in s[1:] if c.isupper()) > 0:
        return False
    # Check if every word in the string is an English letter
    words = s.split()
    if s.endswith("'s"):
        words = s[:-2].split()
    for word in words:
        if not word.isalpha() or len(word) < 3:
            return False
    return True

def save_to_file(lst, filename):
    with open(filename, 'w') as f:
        json.dump(lst, f)

def load_from_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)


def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]

# print(is_english_word('cleaner'))