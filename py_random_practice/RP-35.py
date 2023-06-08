# Loading dictionary from a JSON file and counting number of months in the dictionary
import json
from datetime import datetime
from collections import Counter

file = open("BD.JSON", "r")
d = json.load(file)
''' print(d)
print(d.keys(), '\n', d.values()) '''
a = list(d.values())
# print(a, type(a))
b = []

for x in a:
    x1 = datetime.strptime(x, '%d/%m/%Y')
    b.append(x1.strftime('%B'))
print(b)
print(Counter(b))
