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
    if not nb:
    
    if nb % 2:
        print('I\'m Odd.')
    else:
        print('I\'m Even.')


if __name__ == '__main__':
    if len(sys.argv) > 1 and len(sys.argv) < 2:
        odd_or_even(sys.argv[1])
