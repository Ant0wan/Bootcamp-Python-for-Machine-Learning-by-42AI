#!/usr/bin/env python3
"""
ex02
"""

import sys


def odd_or_even(number):
    """
        Check whether it is odd or even.
    """

    if not int(number):
        print('I\'m Zero.', end='\n')
    elif int(number) % 2:
        print('I\'m Odd.', end='\n')
    else:
        print('I\'m Even.', end='\n')


if __name__ == '__main__':
    ARGC = len(sys.argv)
    if ARGC == 1:
        sys.exit()
    elif 1 < ARGC < 3 and sys.argv[1].isdigit():
        odd_or_even(sys.argv[1])
    else:
        print('ERROR', end='\n')
