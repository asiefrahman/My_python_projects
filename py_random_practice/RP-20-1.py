# finding a number in a list of numbers in iterative method
def binary_search(ar, x1):
    low = 0
    high = len(ar) - 1

    while low <= high:

        mid = (low+high)//2

        if ar[mid] <= x1:
            low = mid+1
        elif ar[mid] > x1:
            high = mid-1
        else:
            return mid
    return -1


A = [11, 45, 89, 10, 36, 49, 75]
B = int(input("put your number: "))

result = binary_search(A, B)

if result != -1:
    print(B, 'is an element of ', A)
else:
    print('The element is not in ', A)
