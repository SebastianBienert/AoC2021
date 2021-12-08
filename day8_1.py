input = [x.split() for x in open("Data/day8.txt", "r").readlines()]
outputs = [x[11:] for x in input]

def getSumOfUniqueValues(line):
    unique_set = {2, 4, 3, 7}
    return len([x for x in line if len(x) in unique_set])

result = sum([getSumOfUniqueValues(x) for x in outputs])
print(result)