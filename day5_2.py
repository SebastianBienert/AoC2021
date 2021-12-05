import re

input = [re.search(r"(\d*),(\d*) -> (\d*),(\d*)", x).groups() for x in open("Data/day5.txt", "r").readlines()]
max_coord = int(max([max(line) for line in input]))
line_points = [ [(int(coordinates[0]), int(coordinates[1])), (int(coordinates[2]), int(coordinates[3])) ] for coordinates in input]

def isCoordinateInLine(x, y, line):
    if (line[1][0] - line[0][0]) == 0:
        if x == line[1][0] and (line[0][1] <= y <= line[1][1] or line[1][1] <= y <= line[0][1]):
            return True
        else:
            return False
    
    slope = (line[1][1] - line[0][1]) / (line[1][0] - line[0][0])
    pointOnLine = (y - line[0][1]) == slope * (x - line[0][0])
    pointBetween  = (min(line[0][0], line[1][0]) <= x <= max(line[0][0], line[1][0])) and (min(line[0][1], line[1][1] ) <= y <= max(line[0][1], line[1][1]))
    return pointOnLine and pointBetween
    
counter = 0
for y in range(0, max_coord + 1, 1):
    for x in range(0, max_coord + 1, 1):
        linesInPoint = [line for line in line_points if isCoordinateInLine(x, y, line)]
        if len(linesInPoint) >= 2:
            counter += 1

print(counter)