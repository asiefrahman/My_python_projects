
import string
import random
s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.digits
s4 = string.punctuation
plen = int(input('enter the password: \n'))
s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
print('your password is: ')
# print(''.join(s[0:plen]))
# for z in range(plen):
final = ''.join([random.choice(str(elem)) for elem in s])
if type(plen) is not int:
    print('Please put an integer number')
else:
    print(final[0:plen])