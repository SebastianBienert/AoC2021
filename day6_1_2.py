from math import floor
from functools import lru_cache

input = [int(x) for x in open("Data/day6.txt", "r").read().strip().split(',')]

@lru_cache(maxsize=None)
def calucalteFishes2(initial, days):
    if initial == 8:
        childs = min(floor(days / 9), 1) + floor(((days - 9) if days - 9 > 0 else 0 ) / 7)
    else:
        childs = floor((days + 6 - initial) / 7)
        
    if initial > days:
        return 0
    
    childs_result = sum([calucalteFishes2(8, days - (initial + 1) - (7 * i)) for i in range(0, childs, 1)])
    return childs + childs_result

sum_1 = sum([1 + calucalteFishes2(number, 80) for number in input])
sum_2 = sum([1 + calucalteFishes2(number, 256) for number in input])
print(sum_1, sum_2)