# Source: Hackerrank.com
# Challenge: Namedtuple

from collections import namedtuple

n = int(input())

students = namedtuple('student', 'ID, MARKS, NAME, CLASS')

data = []

for i in range(n):
    ID = input()
    MARKS = float(input())
    CLASS = input()
    NAME = input()
    data.append(students(ID, MARKS, NAME, CLASS))

total = 0
for j in range(len(data)):
    total += data[j].MARKS

print(total / n)
