# Guessing game
a=int(input('guess a number between i to 10:'))
import random
b=random.randint(1,11)
print(b)
x='you won'
y='you lost'
z=0
if a==b:
    z=z+10
    print(x)
else:
    print(y)
f=[]
f.append(a)
i=1
count_win=0

while i>=1:
    c=str(input('do you want to play more:'))
    if c=='yes':
        e=int(input('put your number: '))
        f.append(e)
        d=random.randint(1,9)
        if e==d:
            z=z+10
            count_win+=1
            print(x)
        else:
            print(y)
        print(d)
        i=i+1
    elif c=='no':
        print('thank you for playing')
        print('Your total attempt: ', len(f))
        print(f)
        print('your total wins: ', count_win)
        break
    else:
        print('wrong choice')
        print('Your total attempt: ', len(f))
        print(f)
        print('your total wins: ', count_win)
        break
print('Your score: ', z)