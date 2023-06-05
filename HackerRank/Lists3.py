n, m = input("Put number of rows and columns = ").split()

# noinspection PyArgumentList
a = list([map(int(x) for x in input().split() for s in range(n))])
b = list([map(int(x) for x in input().split() for w in range(n))])

print(a, b)
