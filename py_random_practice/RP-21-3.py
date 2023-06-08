# creating new text file and name it on the basis of user's choice by taking user input

z = str(input("Put the name of the new file as you desired: "))+'.txt'
x = z+'.txt'
new_file = open(z, "w")
new_file.close()
