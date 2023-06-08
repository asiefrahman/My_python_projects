x=str(input('put numbers for List 1'))
y=str(input('put numbers for List 2'))
z=[]
#print(x)
for m in x:
    if m in y:
        z.append(m)
    else:
        continue
#now removing duplicate elements of the list
list=list(dict.fromkeys(z))
#removing specific element such as ' '
list.remove(' ')
#sorting elements
list1=sorted(list)
print(list)
print(list1)
