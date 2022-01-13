#!/usr/bin/env python3
"""
kata00
"""

T = (19, 42, 21)

if __name__ == '__main__':
    print('The {0} numbers are:\
 {1}'.format(len(T), ', '.join(str(i) for i in T)), end='\n')
