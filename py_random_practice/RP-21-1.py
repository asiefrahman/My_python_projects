# reading text from a text file as string

file1 = open("text_file.txt", "r")
a = file1.read()
file1.close()
print(a, type(a))
