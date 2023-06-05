# Source: Hackerrank.com
# Challenge: String conversion

def print_formatted(number):
    # your code goes here
    # a = int(input())
    w = len(bin(number)[2:])
    for i in range(1, number + 1):
        j = oct(i)[2:]
        # print(j)
        k = hex(i).upper()[2:]
        # print(k)
        l = bin(i)[2:]
        # print(l)
        p = [str(i), str(j.rjust(w)), str(k.rjust(w)), str(l.rjust(w))]
        print(' '.join(p))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)