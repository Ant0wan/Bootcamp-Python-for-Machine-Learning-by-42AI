#!/usr/bin/env python3
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


def ft_progress(listy):
    start = time()
    total = len(listy)
    for i in listy:
        elapsed = float(time() - start)
        avg_per_operation = elapsed / (i + 1)
        eta = avg_per_operation * (total - i - 1)
        prct = (i + 1) / total
        print("ETA: {:4.2f}s [{:4.0%}] {}/{} | elapsed time elapsed {:4.2f}s".format(eta, prct, i+1, total, elapsed), end='\r')
        yield i


if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)

#    listy = range(3333)
#    ret = 0
#    for elem in ft_progress(listy):
#        ret += elem
#        sleep(0.005)
#    print()
#    print(ret)

