# random password generator

import random
a = list({'a', 'f', 'h', 'e', 't', 'u', 'i', 'z', 's', 'c', 'v', 'b', 'n', 'm', 'k', 'l', 'p', 'i', 'u'})
# print(a)
b = list(
    {'A', 'Z', 'G', 'Q', 'D', 'S', 'S', 'E', 'T', 'Y', 'U', 'I', 'Y', 'G', 'F', 'H', 'O', 'L', 'K', 'M', 'N', 'B', 'W'})
c = ['@', '#', '$', '%', '/', '*']
# print(a)

e = random.sample(a, 4)
f = random.sample(b, 4)
g = random.sample(c, 4)
D = random.sample(list(range(0, 10)), 4)
d1 = ''
for o in D:
    d1 = d1+str(o)

print(D)
print(d1)

ask = str(input('what level of password you want to put?: '))
if ask == 'strong':
    h = random.sample(e+f+g+list(d1), 6)
    H = ''
    for char in h:
        H = H+char
    print(H)
elif ask == 'moderate':
    j = random.sample(e + f + list(d1), 6)
    J = ''
    for char in j:
        J = J + char
    print(J)
elif ask == 'weak':
    k = random.sample(e+list(d1), 6)
    K = ''
    for char in k:
        K = K + char
    print(K)
'''print(H)
print(j)
print(K)

#print(len(H))'''