# Source: Hackerrank.com
# Challenge: Sum and Prod
import numpy
from numpy import array

N, M = [int(x) for x in input("put the numbers of rows & columns = ").split()]

my_array = array([[int(x) for x in input().split()] for m in range(N)])
# print(my_array)

w = numpy.sum(my_array, axis =0)
print("Matrix Sum: ", w)
print("Matrix product: ", numpy.prod(w, axis =0))

# Source: Hackerrank.com
# Challenge: Min and Max

w1 = numpy.min(my_array, axis =1)
print("Matrix max value: ", numpy.max(w))

# Source: Hackerrank.com
# Challenge: Mean, Var, and Std

print("Mean: ", numpy.mean(my_array))
print("Standard variation: ", numpy.std(my_array))
print("Variance: ", numpy.var(my_array))

# Source: Hackerrank.com
# Challenge: Dot and Cross

print("Dot operation: ", numpy.dot(my_array, my_array))

# Source: Hackerrank.com
# Challenge: Inner & Outer
# Inner tool returns the inner products & Outer tool returns the outer products
print("Inner:", numpy.inner(my_array, my_array))
print("Outer:", numpy.outer(my_array, my_array))

# Source: Hackerrank.com
# Challenge: Polynomials

n = numpy.array([int(x) for x in input().split()])
x = int(input())
print(numpy.polyval(n, x))
