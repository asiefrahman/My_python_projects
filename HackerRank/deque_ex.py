# Source: Hackerrank.com
# Challenge: collections deque

from collections import deque

d = deque()

N = int(input())
m = [[x for x in input().split()] for i in range(N)]
# print(m)

for element in m:
    if element[0] == 'append':
        d.append(element[1])
    elif element[0] == 'appendleft':
        d.appendleft(element[1])
    elif element[0] == 'pop':
        d.pop()
    elif element[0] == 'popleft':
        d.popleft()

print(' '.join(e for e in d ))
