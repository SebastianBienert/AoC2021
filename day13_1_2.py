input = [x.strip() for x in open("Data/day13.txt", "r").readlines() if len(x.strip()) > 0]
initial_points = [( int(line.split(',')[0]), int(line.split(',')[1]) ) for line in input if line[0].isnumeric()]
folds = [ (line.split('=')[0][-1], int(line.split('=')[1]) ) for line in input if line[0] == 'f']

maxX = max(x[0] for x in initial_points)
maxY = max(x[1] for x in initial_points)

def print2D(input):
    for y in range(len(input)):
        print(input[y])
        
def fillPlane(input, points):
    for point in points:
        input[point[1]][point[0]] = '#'
        
def get_marked_points(plane):
    points = []
    for x in range(len(plane[0])):
        for y in range(len(plane)):
            if plane[y][x] == '#':
                points.append((x, y))
    return points
        
def foldUp(input, yLine):
    pointsUnder = [point for point in get_marked_points(input) if point[1] > yLine]
    newPoints = [(point[0], yLine - (point[1] - yLine) ) for point in pointsUnder]
    fillPlane(input, newPoints)
    del input[yLine:]
    
def foldLeft(input, xLine):
    pointToRight = [point for point in get_marked_points(input) if point[0] > xLine]
    newPoints = [(xLine - (point[0] - xLine) , point[1]) for point in pointToRight]
    fillPlane(input, newPoints)
    for verticalLine in input:
        del verticalLine[xLine:]

plane = [['.' for x in range(maxX + 1)] for y in range(maxY + 1)]
fillPlane(plane, initial_points)


for fold in folds:
    if fold[0] == 'y':
        foldUp(plane, fold[1])
    else:
        foldLeft(plane, fold[1])
    print(len(get_marked_points(plane)))
   
print2D(plane)



