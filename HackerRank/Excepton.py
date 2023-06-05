# Source: Hackerrank.com
# Challenge: Exception

n=int(input())

for i in range(n):
    l=input().split (' ')
    try:
        print(int(l[0])//int(l[1]))
    except Exception as e:
        print("Error Code:", e)