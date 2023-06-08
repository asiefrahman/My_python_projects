# Source: Hackerrank,com
# Challenge: Incorrect RegEx

import re

print(True if re.compile('.+/') else False)

import re
for i in range(int(input())):
    try:
        re.compile(input())
        print("True")
    except re.error as e:
            print("False")
print('your query ended')
