# finding GCD of anyb given numvers

def factors(numbers):
    P=[]
    for L in range(1, numbers+1):
        if numbers%L==0:
            P.append(L)
    return P

a=int(input('How many numbers do you want enter: '))
b=[]
c=list(range(1, a+1))
#print(c)
for m in list(range(1, a+1)):
    if m<=a:
        d=int(input('put your number: '))
        b.append(d)
print('b=', b)
f=[]
W=[]
for O in b:
    f=f+factors(O)
print('f=', f)
for G in f:
    if f.count(G)==a:
        W.append(G)
    else:
        continue
print('W=', list(set(W)))
print('GCD of your given numbers: ', max(W))

