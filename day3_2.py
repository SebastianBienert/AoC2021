import numpy
import collections

input = [list(x.rstrip()) for x in open("Data/day3.txt", "r").readlines()]

def calculate_rating(input, comparisionMethod):
    for index in range(0, len(input[0]), 1):
        transposed = numpy.transpose(input)
        mostCommonBits = collections.Counter(transposed[index]).most_common()
        mostCommonBits.sort(key=comparisionMethod)
        input = [x for x in input if x[index] == mostCommonBits[-1][0]]

    return int(''.join(input[0]), 2)

oxygen_generator_rating = calculate_rating(input, lambda t: (t[1], t[0]))
co2_scrubber_rating = calculate_rating(input, lambda t: (-1 * t[1], 1 if t[0] == '0' else -1))
print(oxygen_generator_rating * co2_scrubber_rating)
