#!/usr/bin/env python3
"""
filterwords
"""

import re
import sys


if __name__ == '__main__':
    try:
        STRING = re.sub(r'[^\w\s]', '', sys.argv[1])
        STRING = re.split(" +", STRING)
        print([word for word in STRING if len(word) > int(sys.argv[2])])
    except ValueError:
        print('ERROR', end='\n')
