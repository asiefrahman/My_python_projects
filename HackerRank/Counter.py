

from collections import Counter

x = int(input())  # Number of shoes
s = [x for x in input().split()]  # All shoe sizes in the shop
shoes = Counter(s)
n = int(input())    # the number of customers
# p = [[x for x in input().split()] for _ in range(n)]     # n1 = Shoe size & x1 = price of the shoes
# print(s)
# print(p)
# print(Counter(s))
w = 0

for _ in range(n):
    b = input().split()
    if b[0] in shoes and shoes[b[0]] > 0:
        shoes[b[0]] -= 1
        w += int(b[1])
    # e.append(b[0])
# print(e)
print(w)
