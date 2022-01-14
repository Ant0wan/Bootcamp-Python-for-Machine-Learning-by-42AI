#!/usr/bin/env python3
"""
ex01
"""

import sys


def rev_alpha():
    """
    Reverse string arguments, capitals and stings.
    """
    if len(sys.argv) > 1:
        letter_list = []
        for i in sys.argv[:0:-1]:
            letter_list.append(i[::-1].swapcase())
        print(' '.join(letter_list), end='\n')


if __name__ == '__main__':
    rev_alpha()
