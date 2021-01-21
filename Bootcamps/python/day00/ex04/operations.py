#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   operations.py                                      :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/04 15:03:42 by abarthel          #+#    #+#              #
#   Updated: 2019/11/04 15:03:42 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys
import math


def usage():
    print('Usage: python operations.py', end='\n')
    print('Example:\n\tpython3.7 operations.py 10 3', end='\n')


def div(a, b):
    if not b:
        return ('ERROR (div by zero)')
    else:
        return (a / b)


def mod(a, b):
    if not b:
        return ('ERROR (modulo by zero)')
    else:
        return (a % b)


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc > 3:
        print('InputError: too many arguments', end='\n')
        usage()
    elif argc is 3:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            print('Sum: {:>20}'.format(math.fsum([a, b])), end='\n')
            print('Difference: {:>13}'.format(a - b), end='\n')
            print('Product: {:>16}'.format(a * b), end='\n')
            print('Quotient: {:>15}'.format(div(a, b)), end='\n')
            print('Remainder: {:>14}'.format(mod(a, b)), end='\n')
        except ValueError:
            print('InputError: only numbers', end='\n')
            usage()
    else:
        usage()
