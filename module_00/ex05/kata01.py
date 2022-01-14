#!/usr/bin/env python3
"""
kata01
"""

LANGUAGES = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

if __name__ == '__main__':
    for key, val in LANGUAGES.items():
        print(key, 'was created by', val, sep=' ', end='\n')
