# write to a file using python
# getting current program file directory

import os
# getting current working directory
a = os.getcwd()
print(a)
# copy a string multiple times in a text file
x = int(input('how many time do you want to copy? '))
a = range(x)
for n in a:

    file1 = open("text_file.txt", "w")
    file1.write('My name is Khan\nWho are you? \nI am very glad to meet you\n')
    file1.close()
    print(file1)
