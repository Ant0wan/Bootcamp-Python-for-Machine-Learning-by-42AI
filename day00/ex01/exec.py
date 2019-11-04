#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   exec.py                                            :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/04 09:36:12 by abarthel          #+#    #+#              #
#   Updated: 2019/11/04 09:36:14 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

import sys


def rev_alpha():
    if len(sys.argv) > 1:
        list = []
        for i in sys.argv[:0:-1]:
            list.append((i[::-1].swapcase()))
            print(' '.join(list), end='\n')


if __name__ == '__main__':
    rev_alpha()
