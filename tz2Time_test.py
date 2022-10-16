from time import time
from tz2 import _max, _min, _sum, _mult
from random import randint

file = []
for i in range(1, 1_000_002, 100000):
    if i == 1000001:
        i = 1000000
    for q in range(i):
        file.append(randint(-1000, 1000))
    firsttime = time()
    # написать любую функцию(_min, _max, _mult, _sum)
    # например:
    _max(file)
    secondtime = time()
    print(f'{i} чисел: ' + str(secondtime - firsttime) + ' секунд')