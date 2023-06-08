# Source: Hackerrank.com
# Challenge: Tuples
'''
q = [a for a in range(10)]
w =map(len(q)-1, q)
print(hash(w))

a = int(input('put the no of integer = '))
b = input()
d = b.split()
print('d =', d)
c = [int(s) for s in d]
print(z for z in c)

print(hash(tuple(d)))
'''

a = int(input())
b = input()
s = b.split()
t = []
print(s, len(s))
for i in s:
    t.append(int(i))
    # print(i, type(i))
# s = [1, 2,]
print(t)
print(hash(tuple(map(int, s))))
print(hash(tuple(t)))

