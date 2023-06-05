#check palindrome

def chk_pal(a):
    c=a[::-1]
    if a[::-1]==a[:]:
        print(a, 'is a palindrome')
    else:
        print(a, 'is not a palindrome')

b=input('please enter your number: ')
print(chk_pal(b))