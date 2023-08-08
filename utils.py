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

def is_alpha_word(s: str):
    if '[' in s or ']' in s:
        return False
    
    if s in ['a', 'an', 'be', 'to', 'of', 'at', 'as', 'in', 'on', 'do', 'up', 'go', 'no']:
        return True
    
    if len(s) < 3:
        return False
    
    if s.endswith("'s"):
        s = s.replace("'s", "")
    
    if '-' in s:
        slash_splited_word = s.split('-')
        for s in slash_splited_word:
            if not is_alpha_word(s):
                return False
    else:
        words = s.split()

        if len(words) == 1 and not s.isalpha():
            return False

        if len(words) == 1 and s.isupper() and is_english_word(s):
            return True

        if len(words) == 1 and has_multiple_uppercase(s):
            return False
        
        # Return False if the string is empty
        if not s or s == ' ':
            return False
        
        # detect like `zjH` `vJt` incorrect words 
        if ' ' not in s and sum(1 for c in s[1:] if c.isupper()) > 0:
            return False
    
    return True
    

def is_alpha_string(s: str):
    
    if not is_alpha_word(s):
        return False
    
    if "'s" in s:
        s = s.replace("'s", "")
    

    words = s.split()

    
    if len(words) > 1:
        for word in words:

            if '-' in word:
                slash_splited_word = word.split('-')
                for s in slash_splited_word:
                    if not is_alpha_word(s):
                        return False
                
            if "'s" in word:
                word = word.replace("'s","")
            word = word.strip()
            if word.startswith('(') and word.endswith(')'):
                word = word[1:-1]
            if not is_alpha_word(word):
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

# print(is_alpha_string("government-funded"))