import numpy
import collections

input = [list(x.rstrip()) for x in open("Data/day3.txt", "r").readlines()]
transposed = numpy.transpose(input)

gamma_rate = ''.join([collections.Counter(x).most_common(1)[0][0] for x in transposed])
epsilon_rate = ''.join([collections.Counter(x).most_common(2)[1][0] for x in transposed])

gamma_rate_dec = int(gamma_rate, 2)
epsilon_rate_dec = int(epsilon_rate, 2)
print(gamma_rate_dec * epsilon_rate_dec)