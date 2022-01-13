#!/usr/bin/env python3
"""
sos
"""

import sys


MAPPING = {
    'A': '.-',
    'B': '-…',
    'C': '-.-.',
    'D': '-…',
    'E': '.',
    'F': '…-.',
    'G': '–.',
    'H': '….',
    'I': '…',
    'J': '.—',
    'K': '-.-',
    'L': '.-…',
    'M': '–',
    'N': '-.',
    'O': '—',
    'P': '.–.',
    'Q': '–.-',
    'R': '.-.',
    'S': '…',
    'T': '-',
    'U': '…-',
    'V': '…-',
    'W': '.–',
    'X': '-…-',
    'Y': '-.–',
    'Z': '–…',
    '1': '.----',
    '2': '…—',
    '3': '…–',
    '4': '….-',
    '5': '……',
    '6': '-….',
    '7': '–…',
    '8': '—…',
    '9': '----.',
    '0': '-----',
    ',': '–…--',
    '.': '.-.-.-',
    '?': '…–…',
    '-': '-….-',
    '[': '-.–.',
    ']': '-.–.-',
    ' ': ' / '
    }


if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:
            j, s, encoded = 0, [], []
            for i in sys.argv[1::]:
                s.append(i.upper())
            for word in s:
                encoded.append('')
                for char in word:
                    encoded[j] += MAPPING[char] + ' '
                j += 1
            print(' / '.join(encoded), end='\n')
        except KeyError:
            print('ERROR', end='\n')
