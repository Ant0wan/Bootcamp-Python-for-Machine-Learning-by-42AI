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

import sys, math


if __name__ == '__main__':
    argc = len(sys.argv)
    if argc is 3 and sys.argv[1].isdigit and sys.argv[2].isdigit:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print('Sum: {:>20}'.format(a + b))
        print('Difference: {:>13}'.format(a - b))
