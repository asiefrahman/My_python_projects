
import random
x=['x','o']

a=random.choice(x)
b=random.choice(x)
c=random.choice(x)
d=random.choice(x)
e=random.choice(x)
f=random.choice(x)
g=random.choice(x)
h=random.choice(x)
i=random.choice(x)

f=[[a,b,c],
   [d,e,f],
   [g,h,i]]
if f[0][0]==f[0][1]==f[0][2]==x[0] or f[1][0]==f[1][1]==f[1][2]==x[0] or f[2][0]==f[2][1]==f[2][2]==x[0] or f[0][0]==f[1][0]==f[2][0]==x[0] or f[0][1]==f[1][1]==f[2][1]==x[0] or f[0][2]==f[1][2]==f[2][2]==x[0] or f[0][0]==f[1][1]==f[2][2]==x[0] or f[0][2]==f[1][1]==f[2][0]==x[0]:
    print('Player-1 wins')
elif f[0][0]==f[0][1]==f[0][2]==2 or f[1][0]==f[1][1]==f[1][2]==x[1] or f[2][0]==f[2][1]==f[2][2]==x[1] or f[0][0]==f[1][0]==f[2][0]==x[1] or f[0][1]==f[1][1]==f[2][1]==x[1] or f[0][2]==f[1][2]==f[2][2]==x[1] or f[0][0]==f[1][1]==f[2][2]==x[1] or f[0][2]==f[1][1]==f[2][0]==x[1]:
    print('Player-2 wins')
else:
   print('Game drawn')

print(f)
print()
