#!/usr/bin/env python3
"""
ex03
"""

import string


def output_analysis(
        count, upletters, lowletters,
        punctmarks, spaces
):
    """Description of output_analysis(...):

    This function append all letters in a string

    Returns: no value.
    """
    displayed_list = [f'The text contains {count} characters:']
    displayed_list.append(f'- {upletters} upper letters')
    displayed_list.append(f'- {lowletters} lower letters')
    displayed_list.append(f'- {punctmarks} punctuation marks')
    displayed_list.append(f'- {spaces} spaces')
    print('\n'.join(displayed_list), end='\n')


def text_analyzer(text=""):
    """Description of text_analyzer(text):

    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.

    Parameters: text (str): A text variable.

    Returns: no value.
    """
    if not text:
        text = input("What is the text to analyse?\n>> ")
    count, upletters, lowletters, punctmarks, spaces = 0, 0, 0, 0, 0
    for i in text:
        count += 1
        if i.isupper():
            upletters += 1
        elif i.islower():
            lowletters += 1
        elif i in string.punctuation:
            punctmarks += 1
        elif i == ' ':
            spaces += 1
    output_analysis(count, upletters, lowletters, punctmarks, spaces)
