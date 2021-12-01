input = [int(x) for x in open("Data/day1.txt", "r").readlines()]
numbers = [x for index, x in enumerate(input) if index != 0 and x - input[index - 1] > 0]
print(len(numbers))