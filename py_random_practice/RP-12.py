#making a list containing the first & last elements of another given list

def first_last(list):
    l=[]
    l.append(list[0])
    l.append(list[len(list)-1])
    return l

import random
p=random.sample(range(2001), 80)
print(first_last(p))
