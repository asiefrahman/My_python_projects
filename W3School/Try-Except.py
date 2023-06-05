a = input('Enter your first number = ')
b = input('Enter your second number = ')


def take_input():
    p = input('Enter your first number = ')
    q = input('Enter your second number = ')
    int(p) + int(q)


try:
    print('Sum = ', int(a) + int(b))
except Exception:
    print('Please enter valid numbers')
    take_input()
