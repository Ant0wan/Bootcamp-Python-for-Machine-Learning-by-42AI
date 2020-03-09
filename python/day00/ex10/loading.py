#!/usr/local/bin/python3.7
# *************************************************************************** #
#                                                                             #
#                                                        :::      ::::::::    #
#   loading.py                                         :+:      :+:    :+:    #
#                                                    +:+ +:+         +:+      #
#   By: abarthel <abarthel@student.42.fr>          +#+  +:+       +#+         #
#                                                +#+#+#+#+#+   +#+            #
#   Created: 2019/11/05 13:41:50 by abarthel          #+#    #+#              #
#   Updated: 2019/11/05 13:41:50 by abarthel         ###   ########.fr        #
#                                                                             #
# *************************************************************************** #

from time import sleep, time
import sys


'''
ETA: 8.67s [ 23%][=====>                 ] 233/1000 | elapsed time 2.33s
'''


start = time()


def ft_progress(listy):
    for i in listy:
        eta = float(time() - start)
        prct = (i + 1) / len(listy)
        print("ETA: {0:4.2f}s [{1:4.0%}]".format(eta, prct), end='\r')
        yield i


if __name__ == "__main__":
    listy = range(100)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)
