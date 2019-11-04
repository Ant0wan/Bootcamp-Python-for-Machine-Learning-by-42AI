#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   count.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/04 12:35:58 by abarthel          #+#    #+#              #
#   Updated: 2019/11/04 12:35:58 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import string


def output_analysis(c, ul, ll, pm, sp):
    list = ['The text contains {0} characters:'.format(c)]
    list.append('- {0} upper letters'.format(ul))
    list.append('- {0} lower letters'.format(ll))
    list.append('- {0} punctuation marks'.format(pm))
    list.append('- {0} spaces'.format(sp))
    print('\n'.join(list), end='\n')


def text_analyzer(text=""):
    """Description of text_analyzer(text):

This function counts the number of upper characters, lower characters,
punctuation and spaces in a given text.

Parameters: text (str): A text variable.

Returns: no value.
"""
    if not text:
        text = input("What is the text to analyse?\n>> ")
    c, ul, ll, pm, sp = 0, 0, 0, 0, 0
    for i in text:
        c += 1
        if i.isupper():
            ul += 1
        elif i.islower():
            ll += 1
        elif i in string.punctuation:
            pm += 1
        elif i is ' ':
            sp += 1
    output_analysis(c, ul, ll, pm, sp)
