#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   whois.py                                           :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/04 11:15:37 by abarthel          #+#    #+#              #
#   Updated: 2019/11/04 11:15:40 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys


def odd_or_even(nb):
    if not int(nb):
        print('I\'m Zero.', end='\n')
    elif int(nb) % 2:
        print('I\'m Odd.', end='\n')
    else:
        print('I\'m Even.', end='\n')


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc > 1 and argc < 3 and sys.argv[1].isdigit():
        odd_or_even(sys.argv[1])
    else:
        print('ERROR', end='\n')
