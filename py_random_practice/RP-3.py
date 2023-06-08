# Removing elements from a list with specific condition ant print a new list

list=[1,2,5,7,8,6,4,6,58,6,8,4,5,3,9,2,6,4,0]
new_list=[]
m=int(input('Please put maximum value to count='))
for n in list:
    if n<=m:
        new_list.append(n)
    else:
        continue
print(new_list)
