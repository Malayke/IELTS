import json
import re
import enchant

def is_english_word(word):
    d = enchant.Dict("en_US")
    return d.check(word)

def is_english_compound_word(compound_word):
    return all(is_english_word(word) for word in compound_word.split())


def is_alpha_string(s: str):
    # Return False if the string is empty
    if not s or s == ' ':
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