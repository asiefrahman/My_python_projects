# finding overlapping elements in two different text files

# making list from first text file
prime_number = open("primenumbers.txt", "r")
x = set([d.strip("\n") for d in prime_number.readlines()])
q = list(x)
print('Prime numbers = ', q)

# making list from second text file
happy_numbers = open("happynumbers.txt", "r")
x1 = set([d.strip("\n") for d in happy_numbers.readlines()])
q1 = list(x1)
print('Happy numbers = ', q1)

a = []  # Declaring a list to group all overlapping elements between two lists
z = []  # declaring a list to group the repeated elements in a single list
for b in q1:
    if q.count(b) != 0:
        a.append(b)
    elif q.count(b) > 0:  # checking duplicate entries
        z.append(b)
    else:
        continue
print('a=', a, '\n', 'z=', z, '\n', len(a))
