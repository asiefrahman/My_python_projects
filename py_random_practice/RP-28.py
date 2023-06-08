
def var(a, b, c):
    if a > b > c:
        # print(a, 'is the greatest number')
        return a
    elif a < b < c:
        # print(c, 'is the greatest number')
        return c
    elif a < b and b > c:
        # print(b, 'is the greatest number')
        return b
    print(var(a, b, c))


w = int(input('put your first number= '))
v = int(input('put your second number= '))
u = int(input('put your third number= '))

x = var(w, v, u)
print('from our program: ', x)
print('from python function: ', max(w, v, u))
