import collections

allLines = [x for x in open("Data/day14.txt", "r").readlines()]
polymerWord = allLines[0].strip()
templates = { x.split('->')[0].strip(): x.split('->')[1].strip() for x in allLines[2:]}

#print(templates)


def getRulesToApply(word, rules):
    rulesToApply = []
    for index in range(0, len(word) - 1):
        key = word[index] + word[index + 1]
        #print(key)
        if key in rules:
            rulesToApply.append((index + 1, rules[key]))
                
    return rulesToApply

def applyRules(word, rules):
    for (index, rule) in enumerate(rules):
        indexToInsert = rule[0] + index
        word = word[:indexToInsert] + rule[1] + word[indexToInsert:]
    return word
    
word = polymerWord
for step in range(10):
    rules = getRulesToApply(word, templates)
    word = applyRules(word, rules)
    
commons = collections.Counter(word).most_common()
max = commons[0]
min = commons[-1]
result = max[1] - min[1]

print(result)