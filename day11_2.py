def get_adjacents(plane, x, y):
    yMax = len(plane) - 1
    xMax = len(plane[0]) - 1
    adjacents = []
    if x > 0:
        adjacents.append((x - 1, y, int(plane[y][x - 1])))
        if y > 0:
           adjacents.append((x - 1, y - 1, int(plane[y - 1][x - 1])))
        if y < yMax:
           adjacents.append((x - 1, y + 1, int(plane[y + 1][x - 1])))
    if x < xMax:
        adjacents.append((x + 1, y, int(plane[y][x + 1])))
        if y > 0:
           adjacents.append((x + 1, y - 1, int(plane[y - 1][x + 1])))
        if y < yMax:
           adjacents.append((x + 1, y + 1, int(plane[y + 1][x + 1])))
    if y > 0:
        adjacents.append((x, y - 1, int(plane[y - 1][x])))
    if y < yMax:
        adjacents.append((x, y + 1, int(plane[y + 1][x])))
        
    return adjacents

def print2D(input):
    for y in range(len(input)):
        print(input[y])
    
def arr_to_ints(list):
    return [int(x) for x in list]

def increase_by_one(input):
    for y in range(len(input)):
        for x in range(len(input[0])):
            input[y][x] += 1
            
def flash(input, x, y):
    adjacents = get_adjacents(input, x, y)
    for adjacent in adjacents:
        input[adjacent[1]][adjacent[0]] += 1
                   
def check_flash(input):
    for y in range(len(input)):
        for x in range(len(input[0])):
            if(input[y][x] > 9):
                input[y][x] = -1000000000000000
                flash(input, x, y)
                return True
    return False

def clear_flashed(input):
    for y in range(len(input)):
        for x in range(len(input[0])):
            if(input[y][x] < 0):
                input[y][x] = 0
         
input = [list(arr_to_ints(x.strip())) for x in open("Data/day11.txt", "r").readlines()]

result = 0
for step in range(2000):
    increase_by_one(input)
    while check_flash(input):
        result += 1
    clear_flashed(input)
    if result == 100:
        print(step + 1)
        break
    result = 0

