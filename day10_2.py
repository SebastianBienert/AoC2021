import statistics

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
                return (True, sign, get_autocomplete(stack))
    return (False, None, get_autocomplete(stack))


def get_autocomplete(stack):
    opening_list = ['(', '[','{','<']
    closing_list = [')', ']','}','>']
    result = []
    while len(stack) > 0:
        index_of_opening = opening_list.index(stack.pop())
        result.append(closing_list[index_of_opening])
    return result
        
def get_autocomplete_score(line):
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    sum = 0
    for char in line:
        sum *= 5
        sum += points[char]
        
    return sum

    
completions = [''.join(isLineCorrupted(line)[2]) for line in input if not isLineCorrupted(line)[0]]
scores = [get_autocomplete_score(line) for line in completions]
print(statistics.median(scores))
#print(scores)

            
