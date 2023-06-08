# Source: Hackerrank.com
# Challenge: Collections/Orderdict

from collections import OrderedDict

number = OrderedDict()
print(number)

number['four'] = 4
number['five'] = 5
number['five'] = 6
print(number)

n, m = list(map(str, input().split()) for i in range(3))
print((n, m))
