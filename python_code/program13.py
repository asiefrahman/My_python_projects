# make 4 separate strings from single string which will show upper case, lower case, number & symbols.

a='abcdefghijklmnopqrstuvwxyz'
b=a.upper()
c='0123456789'

a1=''
b1=''
c1=''
d1=''
e=input('Put your test here: ')
for m in e:
    if m in a:
        a1=a1+m
    elif m in b:
        b1=b1+m
    elif m in c:
        c1=c1+m
    else:
        d1=d1+m
print(a1)
print(b1)
print(c1)
print(d1)