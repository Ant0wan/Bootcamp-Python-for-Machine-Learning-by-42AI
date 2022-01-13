#!/usr/bin/env python3
"""
ex04
"""

import sys
import math


def usage():
    """Display usage"""
    print('Usage: python operations.py', end='\n')
    print('Example:\n\tpython3.7 operations.py 10 3', end='\n')


def div(dividend, divisor):
    """Divide dividend by divisor"""
    if not divisor:
        return 'ERROR (div by zero)'
    return dividend / divisor


def mod(dividend, divisor):
    """Divide dividend modulo divisor"""
    if not divisor:
        return 'ERROR (modulo by zero)'
    return dividend % divisor


if __name__ == '__main__':
    ARGC = len(sys.argv)
    if ARGC > 3:
        print('InputError: too many arguments', end='\n')
        usage()
    elif ARGC == 3:
        try:
            ARG_ONE = float(sys.argv[1])
            ARG_TWO = float(sys.argv[2])
            print('Sum: {:>20}'.format(math.fsum([ARG_ONE, ARG_TWO])), end='\n')
            print('Difference: {:>13}'.format(ARG_ONE - ARG_TWO), end='\n')
            print('Product: {:>16}'.format(ARG_ONE * ARG_TWO), end='\n')
            print('Quotient: {:>15}'.format(div(ARG_ONE, ARG_TWO)), end='\n')
            print('Remainder: {:>14}'.format(mod(ARG_ONE, ARG_TWO)), end='\n')
        except ValueError:
            print('InputError: only numbers', end='\n')
            usage()
    usage()
