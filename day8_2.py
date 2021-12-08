input = [x.split() for x in open("Data/day8.txt", "r").readlines()]
inputs = [x[:10] for x in input]
outputs = [x[11:] for x in input]

def solveLine(line, output):
    allLetters = "abcdefg"
    letters_decoded = {x: None for x in allLetters}
    dic = {i: None for i in range(10)}
    dic[1] = next(x for x in line if len(x) == 2)
    dic[4] = next(x for x in line if len(x) == 4)
    dic[7] = next(x for x in line if len(x) == 3)
    dic[8] = next(x for x in line if len(x) == 7)
    dic[6] = next(x for x in line if (len(x) == 6 and (dic[1][0] not in x or dic[1][1] not in x)))
    letters_decoded['c'] = next(letter for letter in allLetters if letter not in dic[6])
    letters_decoded['f'] = next(letter for letter in dic[1] if letter != letters_decoded['c'])
    dic[5] = next(x for x in line if len(x) == 5 and letters_decoded['c'] not in x)
    letters_decoded['e'] = next(letter for letter in allLetters if letter not in dic[5] and letter != letters_decoded['c'])
    dic[9] = next(x for x in line if len(x) == 6 and letters_decoded['e'] not in x)
    dic[2] = next(x for x in line if len(x) == 5 and letters_decoded['f'] not in x)
    letters_decoded['b'] = next(letter for letter in allLetters if letter not in dic[2] and letter != letters_decoded['f'])
    dic[3] = next(x for x in line if len(x) == 5 and letters_decoded['b'] not in x and letters_decoded['e'] not in x)
    dic[0] = next(word for word in line if word not in dic.values())
    letters_decoded['d'] = next(letter for letter in allLetters if letter not in dic[0])
    letters_decoded['g'] = next(letter for letter in allLetters if letter not in dic[7] and letter != letters_decoded['b'] and letter != letters_decoded['d'] and letter != letters_decoded['e'])
    letters_decoded['a'] = next(letter for letter in allLetters if letter not in dic[4] and letter != letters_decoded['g'] and letter != letters_decoded['e'])
    output_digits = [word_to_digit(letters_decoded, word) for word in output]
    result = array_to_int(output_digits)
    return result
    
def decode_word(letters_decoded, word):
    return ''.join([letters_decoded[x] for x in word])

def word_to_digit(letters_decoded, word):
    dic = [
         set("abcefg"),
         set("cf"),
         set("acdeg"),
         set("acdfg"),
         set("bcdf"),
         set("abdfg"),
         set("abdefg"),
         set("acf"),
         set("abcdefg"),
         set("abcdfg")
    ]
    decoded_dic = [set(decode_word(letters_decoded, "".join(x))) for x in dic]
    digit = next(index for index, x in enumerate(decoded_dic) if set(word) == x)
    return digit

def array_to_int(numList):
    s = ''.join(map(str, numList))
    return int(s)
    
results = [solveLine(inputs[i], outputs[i]) for i in range(len(inputs))]
print(sum(results))