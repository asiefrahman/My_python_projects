a = list(range(0, 100, 20))
# print(a)
b = 0
c = []
for x in a:
    if x % 20 == 0:
        b = b + x
        c.append(x)
    else:
        continue

print(b)
d = ''
for x1 in c:
    if c.index(x1) < len(c):
        d = d + '+' + str(x1)

print(d[3:len(d)], '=', b)
