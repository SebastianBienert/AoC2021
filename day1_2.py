input = [int(x) for x in open("Data/day1.txt", "r").readlines()]
sums = [x + input[index + 1] + input[index + 2] for index, x in enumerate(input[:-2])]
increasing_sums = [x for index, x in enumerate(sums) if index != 0 and x - sums[index - 1] > 0]

print(len(increasing_sums))