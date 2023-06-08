#finding divisors of any given number.

x=str(input('Put your words:'))
y=list(range(1,int(x)+1))
z=[]
#print(y)
for n in y:
    if int(x)%n==0:
        z.append(n)
    else:
        continue
print(z)