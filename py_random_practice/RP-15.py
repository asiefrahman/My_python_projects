# reversing string

def reverse_string(a):
    b = a.split(' ')
    print(b)
    result = ''
    for char in b:
        result = ' ' + char + result
    return result


x = input('Enter your string with space: ')
print(reverse_string(x))
