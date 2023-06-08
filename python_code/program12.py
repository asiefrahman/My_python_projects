country='America'
a=country[-7]
print(a)
b=[]
d=''
for c in country:
    b.append(c)
    if len(d)!=0:
        d=d+' '+c
    else:
        d=d+c
print(b)
print(d)
str = "a quick brown fox jumps over the lazy dog"
z=[]
for c in "abcdefghijklmnopqrstuvwxyz":
    z.append(c)
    z.append(str.count(c))
    print(z)
    z=[]