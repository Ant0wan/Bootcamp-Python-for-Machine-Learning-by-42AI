#!/usr/bin/env python3
"""
loading

Display like:
ETA: 8.67s [ 23%][=====>                 ] 233/1000 | elapsed time 2.33s
"""

from time import sleep, time
import sys


def ft_progress(listy):
    """Yield function"""
    start = time()
    total = len(listy)
    for i in listy:
        elapsed = float(time() - start)
        avg_per_operation = elapsed / (i + 1)
        eta = avg_per_operation * (total - i - 1)
        prct = (i + 1) / total
        print("ETA: {:4.2f}s [{:4.0%}][{:=>{}}{:{}}] {}/{} \
| elapsed time elapsed {:4.2f}s".format(
            eta,
            prct,
            '=', i * 25 / total,
            '>', 25 - i * 25 // total, i + 1,
            total, elapsed), end='\r')
        yield i


if __name__ == "__main__":
    listy = range(1000)
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)

    listy = range(3333)
    ret = 0
    for elem in ft_progress(listy):
        ret += elem
        sleep(0.005)
    print()
    print(ret)
