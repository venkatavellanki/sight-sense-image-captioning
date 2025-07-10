# text_preprocessing.py

import string
import re
from pickle import dump
from tensorflow.keras.preprocessing.text import Tokenizer
from config import *

def load_doc(filename):
    with open(filename, 'r') as file:
        text = file.read()
    return text

def clean_captions(captions_dict):
    table = str.maketrans('', '', string.punctuation)
    for key, captions in captions_dict.items():
        captions = [c.lower().translate(table) for c in captions]
        captions = [' '.join([word for word in c.split() if len(word) > 1 and word.isalpha()]) for c in captions]
        captions_dict[key] = ['startseq ' + c + ' endseq' for c in captions]
    return captions_dict

def create_tokenizer(descriptions):
    lines = []
    for desc_list in descriptions.values():
        lines.extend(desc_list)
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)
    return tokenizer
