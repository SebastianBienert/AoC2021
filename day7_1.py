from statistics import median

input = [int(x) for x in open("Data/day7.txt", "r").read().strip().split(',')]
med = median(input)
result = sum([abs(x - med) for x in input])
print(result)