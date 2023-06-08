# Source: Hackerrank.com
# Challenge: Array Mathematics

from numpy import array

N, M = [int(x) for x in input().split()]

A = array([[int(x) for x in input().split()] for M in range(N)])
B = array([[int(x) for x in input().split()] for M in range(N)])

print((N, M))
print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A**B)
