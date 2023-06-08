# Source: Hackerrank.com
# Challenge: Linear algebra

import numpy
from numpy import array

N = int(input())
A = array([[float(x) for x in input().split()] for _ in range(N)])

a = numpy.linalg.det(A)

# print(round(numpy.linalg.det(A), 2))
print("a = ", a)
print(round(a, 2))
