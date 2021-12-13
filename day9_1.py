input = [list(x.strip()) for x in open("Data/day9.txt", "r").readlines()]

#print(input)

def get_adjacents(plane, x, y):
    yMax = len(plane) - 1
    xMax = len(plane[0]) - 1
    adjacents = []
    if x > 0:
        adjacents.append(plane[y][x - 1])
        if y > 0:
            adjacents.append(plane[y - 1][x - 1])
        if y < yMax:
            adjacents.append(plane[y + 1][x - 1])
    if x < xMax:
        adjacents.append(plane[y][x + 1])
        if y > 0:
            adjacents.append(plane[y - 1][x + 1])
        if y < yMax:
            adjacents.append(plane[y + 1][x + 1])
    if y > 0:
        adjacents.append(plane[y - 1][x])
    if y < yMax:
        adjacents.append(plane[y + 1][x])
        
    return adjacents

low_points = []
for y in range(len(input)):
    for x in range(len(input[0])):
        adjacents = get_adjacents(input, x, y)
        if all(h > input[y][x] for h in adjacents):
            low_points.append(input[y][x])
                   
result = sum(int(p) + 1 for p in low_points)
print(result)