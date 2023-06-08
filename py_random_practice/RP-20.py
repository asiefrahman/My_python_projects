# finding an element in list of elements using if-else function

a = [4, 5, 8, 9, 6, 5, 6, 1, 2, 3, 6, 9, 9, 6, 4, 6, 6]
b = int(input("put your desired number: "))
if b in a:
    print(b, ' is in the list ', a)
else:
    print('No match found')
