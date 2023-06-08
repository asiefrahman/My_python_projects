# Source: Hackerrank,com
# Challenge: Eye and Identity
import numpy

N, M = input("put numbers = ").split(" ")
print(numpy.eye(int(N), int(M), k=0))
