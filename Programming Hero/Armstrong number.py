# finding a armstrong number
a=int(input('How many numbers do you want enter: '))
b=[]
c=list(range(1, a+1))
f=''
#print(c)
for m in c:
    if m<=len(c):
        d=int(input('put your number: '))
        b.append(d)
print(b)

e=[]
for n in b:
    if b.index(n)<=len(b):
        e.append(pow(n,a))
        f=f+str(n)
print('e=', e)
print('f=', f)
print('sum of e: ', sum(e))
g=str(sum(e))
if str(sum(e))==set(f):
    print('these numbers are Armstrong number: ', b)
else:
    print('these are mot armstrong')
