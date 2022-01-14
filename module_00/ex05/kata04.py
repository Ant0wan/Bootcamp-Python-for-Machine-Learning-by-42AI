#!/usr/bin/env python3
"""
kata04
"""

if __name__ == '__main__':
    T = (0, 4, 132.42222, 10000, 12345.67)
    print(f'module_{T[0]:0>2}, ex_{T[1]:0>2} : {T[2]:.2f}, {T[3]:.2e},\
 {T[4]:.2e}', end='\n')
