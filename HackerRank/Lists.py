# Source: Hackerrank.com
# Challenge: Merge the tools
a = 'qqkkeridklospwe'
k = 3
b = []
c =''
for i in range(0, len(a), k):
    b.append(a[i:i+k])
print(b)
#print(c)
w = ''
for j in b:
    p = set(j)
    print(p)
    for x in p:
        x += x
        print(x)
