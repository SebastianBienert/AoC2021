input = [x.strip() for x in open("Data/day10.txt", "r").readlines()]

def isLineCorrupted(line):
    opening_list = ['(', '[','{','<']
    closing_list = [')', ']','}','>']
    stack = []
    for sign in line:
        if sign in opening_list:
            stack.append(sign)
        else:
            index_of_closing = closing_list.index(sign)
            index_of_opening = opening_list.index(stack.pop())
            if index_of_closing != index_of_opening:
                return (True, sign)
    return (False, None)

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

result = sum(points[isLineCorrupted(line)[1]] for line in input if isLineCorrupted(line)[0])
print(result)

            
