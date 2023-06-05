# Bulls and cows game

a=str(input('Enter our number= '))
b=str(input('Enter our number= '))
bulls=0
cows=0

if a==b:
    print('You win')
else:
    for i in range(len(a)):
        if b[i]==a[i]:
            bulls+=1
        elif b[i] in a:
            cows+=1
    print('bulls= ', bulls)
    print('cows= ', cows)
