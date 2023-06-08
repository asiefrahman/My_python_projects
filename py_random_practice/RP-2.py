'''
num = int(input('Please enter a number= '))
if num % 2 == 0:
    print('It is an even number')
else:
    print('It is a an odd number')

if num % 4 == 0:
    print('the number is a multiple of 4')
else:
    print('it is not a multiple of 4')
'''

x, y = input('Please enter 2 numbers= ').split()

if int(x) % int(y) == 0:
    print('first number {} is divisible by second number {}'.format(x,y))
else:
    print('first number {} is not divisible by second number {}'.format(x, y))
