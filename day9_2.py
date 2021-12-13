import itertools
from queue import Queue

input = [list(x.strip()) for x in open("Data/day9.txt", "r").readlines()]

def get_adjacents(plane, x, y):
    yMax = len(plane) - 1
    xMax = len(plane[0]) - 1
    adjacents = []
    if x > 0:
        adjacents.append((x - 1, y, int(plane[y][x - 1])))
       # if y > 0:
        #    adjacents.append((x - 1, y - 1, int(plane[y - 1][x - 1])))
        #if y < yMax:
          #  adjacents.append((x - 1, y + 1, int(plane[y + 1][x - 1])))
    if x < xMax:
        adjacents.append((x + 1, y, int(plane[y][x + 1])))
       # if y > 0:
          #  adjacents.append((x + 1, y - 1, int(plane[y - 1][x + 1])))
       # if y < yMax:
         #   adjacents.append((x + 1, y + 1, int(plane[y + 1][x + 1])))
    if y > 0:
        adjacents.append((x, y - 1, int(plane[y - 1][x])))
    if y < yMax:
        adjacents.append((x, y + 1, int(plane[y + 1][x])))
        
    return adjacents

low_points = []
for y in range(len(input)):
    for x in range(len(input[0])):
        adjacents = get_adjacents(input, x, y)
        if all(h[2] > int(input[y][x]) for h in adjacents):
            low_points.append((x, y, int(input[y][x])))
            #print(adjacents)
                   
#result = sum(int(p) + 1 for p in low_points)
#print(low_points)

# X - point[0]
# Y - point[1]
# H - point[2]

def get_basin(input, x, y, visited):
    #print(visited)
    visited.add((x, y, int(input[y][x])))
    adjacents = [p for p in get_adjacents(input, x, y) if p[2] < 9 and p not in visited]
    #print(adjacents)
    basin = [get_basin(input, p[0], p[1], visited) for p in adjacents]
    return basin

# xd = []
# xd.append((1,2,3))

basins = []
for point in low_points:
    visited = set()
    get_basin(input, point[0], point[1], visited)
    basins.append(len(visited))
    
    
basins.sort()
result = basins[-1] * basins[-2] * basins[-3]
print(result)

    