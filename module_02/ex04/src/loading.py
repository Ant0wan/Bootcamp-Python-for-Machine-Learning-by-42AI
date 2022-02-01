"""
loading

Display like:
ETA: 8.67s [ 23%][=====>                 ] 233/1000 | elapsed time 2.33s
"""

from time import time
from collections import namedtuple

ProgressBar = namedtuple('ProgressBar', ['size', 'edge_position'])


def ft_progress(lst):
    """Yield function"""
    start = time()
    total = len(lst)
    for i in lst:
        elapsed = float(time() - start)
        avg_per_operation = elapsed / (i + 1)
        eta = avg_per_operation * (total - i - 1)
        prct = (i + 1) / total
        pbar = ProgressBar(i * 25 / total, 25 - i * 25 // total)
        print(f"ETA: {eta:4.2f}s [{prct:4.0%}][{'=':=>{pbar.size}}\
{'>':{pbar.edge_position}}] {(i + 1)}/{total} | elapsed time elapsed\
{elapsed:4.2f}s", end='\r')
        yield i
