from statistics import median

input = [int(x) for x in open("Data/day7.txt", "r").read().strip().split(',')]
med = median(input)


def distance(a, b):
    d = abs(b - a)
    return ((1 + d) * d) / 2

def sumOfDistances(input, point):
    return sum([distance(point, x) for x in input])

min = 10000000000000
for i in range(0, len(input) // 2, 1):
    x = med - i
    y = med + i
    
    sum_x = sumOfDistances(input, x)
    if sum_x < min:
        min = sum_x
    
    sum_y = sumOfDistances(input, y)
    if sum_y < min:
        min = sum_y

print(min)