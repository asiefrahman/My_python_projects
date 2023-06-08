# simple calculator

a=int(input('Put your 1st number: '))
b=str(input('What do you want to perform? Add, subtract, multiply or division: '))
c=int(input('Put your second number: '))

if b== '+':
    print(a+c)
elif b=='-':
    print(a-c)
elif b=='*':
    print(a*c)
elif b=='/':
    print(float(a/c))
elif b=='%':
    print(a%c)
else:
    print('Wrong operator selected')

