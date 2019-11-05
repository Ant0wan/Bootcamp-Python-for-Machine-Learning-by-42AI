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

from time import sleep
import sys
'''
ETA: 8.67s [ 23%][=====>                 ] 233/1000 | elapsed time 2.33s
'''

def ft_progress(listy):
    for i in listy:
        print("{:4.0%}".format((i + 1)/len(listy)), end='\r')
        yield i


listy = range(100)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.01)
print()
print(ret)
