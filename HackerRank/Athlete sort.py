# Source: Hackerrank.com
# Challenge: Athlete sort

N, M = input().split()
m = [[int(x) for x in input().split()] for i in range(int(N))]

a = int(input())
# print(type(a))

# take the second element for sort
def take_second(elem):
    return elem[a]
d = sorted(m, key=take_second)
for i in d:
    print(' '.join(str(j) for j in i))
