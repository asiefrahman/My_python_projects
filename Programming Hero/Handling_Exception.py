# Handle exception

a = input('your first number = ')
b = input('your second number = ')
# c = a/b
try:
    print(int(a)/int(b))
except Exception as e:
    print('Error code:', e)
#except ZeroDivisionError as f:
 #   print('Error code: ', f)

