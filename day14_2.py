from functools import lru_cache

allLines = [x for x in open("Data/day14.txt", "r").readlines()]
polymerWord = allLines[0].strip()
rules = { x.split('->')[0].strip(): x.split('->')[1].strip() for x in allLines[2:]}

allChars = set(rules.values())

@lru_cache(maxsize=None)
def get_length_of_added_string(word, steps, char):
    if steps == 0:
        return 0
    
    sum = 0
    for index in range(0, len(word) - 1):
        key = word[index] + word[index + 1]
        if key in rules:
            if char == rules[key]:
                sum += 1 + get_length_of_added_string(word[index] + rules[key] + word[index + 1], steps - 1, char)
            else:
                sum += get_length_of_added_string(word[index] + rules[key] + word[index + 1], steps - 1, char)
            
    return sum
             
dict = {char: get_length_of_added_string(polymerWord, 40, char) + len([x for x in polymerWord if x == char]) for char in allChars}
maxKey = max(dict, key=dict.get)
minKey = min(dict, key=dict.get)
result = dict[maxKey] - dict[minKey]
print(maxKey, dict[maxKey])
print(minKey, dict[minKey])
print(result)