#!/usr/bin/env python3
"""
kata00
"""

T = (19, 42, 21)

if __name__ == '__main__':
    LENGTH = len(T)
    NUMBERS_STR = ', '.join(str(i) for i in T)
    print(f'The {LENGTH} numbers are: {NUMBERS_STR}', end='\n')
