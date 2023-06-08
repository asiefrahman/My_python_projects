#Programming Hero
#Reversing string

a=input('Enter your string: ')
b=''
for char in a:
    b=char+b
print('In normal method: ', b)

#reversibg string in stack method

c=[]
for i in a:
    c.append(i)
#print(c)
b1=''
while len(c)>0:
    L=c.pop()
    b1=b1+L
print('In stack mathod: ', b1)

#Reversing string in recursive method

def rev_rec(str):
    if len(str)>0:
        return rev_rec(str[1:]) + str[0]
    else:
        return str
j=rev_rec(a)
print('in recursive method: ', j)

#Smartest way
print('The smartest way: ', a[::-1])