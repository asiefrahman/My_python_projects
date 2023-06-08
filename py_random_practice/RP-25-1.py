# Guessing game 2, using binary search

import random

max_choice = int(input("Choose your maximum range to guess= "))
user = int(input("choose a number= "))

system = random.randint(1, max_choice)
print("system guess no 1= ", system)

low = 1
high = max_choice
# mid=(low+high)//2
count = 1

if user == system:
    print('The machine guess the correct number: ', system)
else:
    while system != user:
        if low <= user < system:
            high = system - 1
            system = random.randint(low, high)
            print("The machine guesses wrong number, New guess", system, 'Next range: ', low, 'to', high)
            count = count + 1
        elif low <= user and user > system:
            low = system + 1
            system = random.randint(low, high)
            print("The machine guesses wrong number, New guess", system, 'Next range: ', low, 'to', high)
            count = count + 1
        elif user == system:
            print("the machine guess the correct number now: ", system)
            count = count + 1
            continue

    print('Final guess:', system, 'total guess= ', l)
