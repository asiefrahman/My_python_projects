# Picking a random word from a list of words saved in a text file

import random

word = open("SOWPODS.txt", "r")
word_read = list(d.strip("\n") for d in word.readlines())
word.close()

chose = random.sample(word_read, 1)
print(chose)

word_chose = ''
word_chose = word_chose + str(chose)
print('see as list: ', word_chose)
