from functools import reduce

input = [(x.split()[0][0], int(x.split()[1])) for x in open("Data/day2.txt", "r").readlines()]
aim = 0
hpos = 0
depth = 0
for command, value in input:
    if command == 'u':
        aim += value
    elif command == 'd':
        aim -= value
    else:
        hpos += value
        depth += aim * value

print(abs(hpos * depth))
