# Counting number of vowels

c = input('Enter your word: ')
a = c.lower()
# x=list(num)
# y=x.splt()
# y=[]
for m in a:
    counta = a.count('a')
    counte = a.count('e')
    counti = a.count('i')
    counto = a.count('o')
    countu = a.count('u')
    b = counta + counte + counti + counto + countu

print('Total number of vowels =', b)

if counta > 0:
    print('No of a', counta)
if counte > 0:
    print('No of e', counte)
if counti > 0:
    print('No of i', counti)
if counto > 0:
    print('No of o', counto)
if countu > 0:
    print('No of u', countu)
