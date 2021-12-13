import re
from collections import defaultdict
regexes = [re.search(r"(\w+)-(\w+)", x).groups() for x in open("Data/day12.txt", "r").readlines()]

def get_nodes(input):
    return set([x[0] for x in input]).union(set([x[1] for x in input]))

def get_adjacent_nodes(input, node):
    result = []
    for x in input:
        if x[0] == node:
            result.append(x[1])
        if x[1] == node:
            result.append(x[0])
    return result

def get_dict(input):
    nodes = get_nodes(regexes)
    dict = {x: get_adjacent_nodes(input, x) for x in nodes}
    return dict

def get_dict_counter():
    nodes = get_nodes(regexes)
    dict = {x: -1000000000000 if x == 'start' else 0 for x in nodes}
    return dict

def find_path(dict, counter, current):
    if current[0].islower() and current != 'end':
        counter[current] += 1
         
    adjacents = [x for x in dict[current] if x != 'start' and (counter[x] < 1 or all(y < 2 for y in counter.values()))]
    #print(counter)
    if current == 'end':
        return 1
    
    if len(adjacents) == 0:
        return 0
    
    result = sum(find_path(dict, counter.copy(), x) for x in adjacents)
    
    return result

dict = get_dict(regexes)
counters = get_dict_counter()
#print(counters)
small_caves = set([x for x in get_nodes(regexes) if not x[0].isupper()])
result = find_path(dict, counters, 'start')
#print(counters)

print(result)