# Source: Hackerrank.com
# Challenge: Any or All

N = int(input())
L = [x for x in input().split()]
print(True if all(int(s)>0 for s in L) and any(str(a) == str(a[::-1]) for a in L) else False)
