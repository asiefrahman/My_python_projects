# Source: Hackerrank.com
# Challenge: sorting / ginortS

a = input()


def sort_out(i):
    L = ''
    U = ''
    n = ''
    N = ''
    sorted_word=''
    for char in i:
        if char.islower():
            L = L+char
        elif char.isupper():
            U = U + char
        elif char.isdigit() and int(char) % 2 != 0:
            n = n + char
        elif char.isdigit() and int(char) % 2 == 0:
            N = N + char
        else:
            continue
    print(''.join(sorted(L) + sorted(U) + sorted(n) + sorted(N)))


sort_out(a)
