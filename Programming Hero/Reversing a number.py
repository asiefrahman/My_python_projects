#Reversing a number

def rev_num(number):
    reverse=0
    while number>1:
        last=number%10
        reverse=reverse*10+last
        number=number//10
    return reverse

a=int(input('Pleas enter your number: '))
b=rev_num(a)
print('Reverse of your number: ', b)