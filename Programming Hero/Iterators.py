# introducing iterators

iterable_value = 'Programming Hero'
interate_obj = iter(iterable_value)
a = []

while True:
    try:
        item = next(interate_obj)
        a.append(item)
    except StopIteration:
        print(a)
        break

# Creating iterator
class Data:
    def __init__(self, limit):
        self.limit = limit
    def __iter__(self):
        self.value = 0
        return self
    def __next__(self):
        x = self.value
        if x > self.limit:
            raise StopIteration
        else:
            self.value = x + 1
            return x

for i in Data(5):
    print(i)

# Generator
# Generators create iterators in Python

import random

def datum():
    for i in range(5):
        yield random.randint(1, 10)

for num in datum():
    print('num = ', num)
