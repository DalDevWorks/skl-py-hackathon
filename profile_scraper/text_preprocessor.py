'''
text_preprocessor takes string as input and removes numbers,
punctuation, and stop words.
'''

import string
import re

from stop_words import get_stop_words
from string import maketrans

stop_words = get_stop_words('english')

def remove_punctuation(line):
    in_chars = string.punctuation
    out_char = "                                "
    translate_line = maketrans(in_chars, out_char)
    return line.translate(translate_line)

def remove_numbers(line):
    in_chars = string.digits
    out_char = "          "
    translate_line = maketrans(in_chars, out_char)
    return line.translate(translate_line)

def remove_stopwords(line):
    tokenized = line.split()
    filtered_sentence = ""

    for w in tokenized:
        if w not in stop_words:
            filtered_sentence += w + " "

    return filtered_sentence

def text_preprocessor(in_string):

    lower_line = in_string.lower()
    no_stop_words = remove_stopwords(lower_line)
    nopunc_line = remove_punctuation(lower_line)
    nonum_line = remove_numbers(nopunc_line)

    processed_line = ""

    tokenized = nonum_line.split()

    for w in tokenized:
        if len(w) > 2:
            processed_line += w + " "

    return processed_line
