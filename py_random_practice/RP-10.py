#random list making, compare & then sorting unique elements in between the list

import random
a=random.sample(range(100), 10)
b=random.sample(range(100), 18)
print(a)
print(b)
c=[]
for m in a:
    if m in b:
        c.append(m)
    else:
        continue
print(c)