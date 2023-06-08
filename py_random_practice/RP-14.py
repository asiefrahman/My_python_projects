#From a given list, make another list which contains the duplicate elements
# and make another list which contains only the unique elements.

a=[1,4,7,5,6,9,9,6,65,5,5,5,6,56,6,5,6,6]
d=[]
e=[]
for n in a:
    if a.count(n)>1:
        d.append(n)
        c=list(set(d))
    elif a.count(n)==1:
        e.append(n)
print(c)
print(e)