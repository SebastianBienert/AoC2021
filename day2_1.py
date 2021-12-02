from functools import reduce

input = [(x.split()[0], int(x.split()[1])) for x in open("Data/day2.txt", "r").readlines()]
forward = sum([x[1] for x in input if x[0][0] == 'f'])
depth = reduce(lambda acc, v: acc + v[1] if v[0][0] == 'u' else (acc - v[1] if v[0][0] == 'd' else acc), input, 0)
print(abs(depth * forward)) 