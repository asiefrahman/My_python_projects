# Find the types of elements in a list and count the numbers of types used in the list

a = [1, 'w', 3, ')', '-', 0.9]
c=[]
for x in a:
    b = type(x)
    c.append(b)

# print(set(c))

for y in set(c):
    if y in c is True:
        c.count(y)
    print(y, ' is ', c.count(y), ' times used in the list')
