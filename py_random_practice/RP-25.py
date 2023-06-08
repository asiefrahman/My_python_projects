# Guessing game 2 using random function

import random
max_choice = int(input("Choose your maximum range to guess= "))
user = int(input("choose a number= "))

system = random.randint(1, max_choice)
print("system guess no 1= ", system)

low = 0
high = max_choice
mid = 0
t = 1
while system != user:
    if system != user:
        system = random.randint(1, max_choice)
        print('Guess no', t, 'not matched', '\nNew guess= ', system)
        t = t+1
    else:
        print("Guess no.", t, 'matched')
        t = t+1
    continue
print('Guess no.', t, 'matched,', 'Final guess: ', system, '\nTotal guess= ', t, )
