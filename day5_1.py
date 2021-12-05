import re

input = [re.search(r"(\d*),(\d*) -> (\d*),(\d*)", x).groups() for x in open("Data/day5.txt", "r").readlines()]
max_coord = int(max([max(line) for line in input]))
line_points = [ [(int(coordinates[0]), int(coordinates[1])), (int(coordinates[2]), int(coordinates[3])) ] for coordinates in input]

not_diagonal_lines = [line for line in line_points if line[0][0] == line[1][0] or line[0][1] == line[1][1]]

print(input)
print(not_diagonal_lines)
print(max_coord)

def isCoordinateInLine(x, y, line):
    
    if x != line[0][0] and y != line[0][1]:
        return False
    y_max = max(line[0][1], line[1][1])
    y_min = min(line[0][1], line[1][1])
    x_max = max(line[0][0], line[1][0])
    x_min = min(line[0][0], line[1][0])
    result = (x == line[0][0] and y >= y_min and y <= y_max) or (y == line[0][1] and x >= x_min and x <= x_max)
    return result

counter = 0
for y in range(0, max_coord + 1, 1):
    for x in range(0, max_coord + 1, 1):
        linesInPoint = len([line for line in not_diagonal_lines if isCoordinateInLine(x, y, line)])
        #print(linesInPoint)
        if linesInPoint >= 2:
            counter += 1



print(counter)