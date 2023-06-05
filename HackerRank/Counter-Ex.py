from collections import defaultdict

m = defaultdict(list)

n, b = list(map(int, input().split()))

for i in range(n):
    m[input()].append(i+1)

for i in range(b):
    print(' '.join(map(str, m[input()])) or -1)
