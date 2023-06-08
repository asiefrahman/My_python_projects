#Source: Hackerrank.com
# Challenge: Floor, Ceil and Rint

import numpy
from numpy import array

# my_array = numpy.array([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
# my_array = numpy.array([float(x) for x in input().split()])

# M = list(map(float, input().split()))
my_array = numpy.array(input().split(), float)
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))
