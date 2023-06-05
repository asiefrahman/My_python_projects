# Source: Hackerrank.com
# Challenge: perform on the list

w = input('how many inputs = ')

for e in range(len(w)):
    k = input()
    l = k.split()
    a = []
    if l[0] == 'insert':
        #l[1] = int(l[1])
        #l[2] = int(l[2])
        a.insert(l[1], l[2])
    elif l[0] == 'print':
        print(l)
    elif l[0] == 'append':
        a.append(l[1])
    elif l[0] == 'remove':
        a.remove(l[1])
    elif l[0] == 'sort':
        a.sort()
    elif l[0] == 'pop':
        a.pop()
    elif l[0] == 'reverse':
        a.reverse()
    print(a)