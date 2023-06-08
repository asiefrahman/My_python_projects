g=['rock', 'paper', 'scissor']

a=input('write your choice:')
b=input('write your choice:')


import random
h=random.choice(g)
print(h)

if a==h and b==h:
    print('both a & b win')
elif a==h and b!=h:
    print('only a wins')
elif a!=h and b==h:
    print('only b wins')
else:
    print('both a & b lost')

'''
if a==b:
    print('b wins')
else:
    print('a wins')
'''