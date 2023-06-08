# creating new text file

new_file = open("new_text_file_2.txt", 'w')
# use "w" for rewrite the existing file with the same name and use " x" to create new file without duplicate existence

new_file.close()

# Adding new text to the new file
new_file = open("new_text_file_2.txt", 'w')
new_file.write('Hello there!\nThis is a new text file created for you!\nAnd it was overwritten!')
new_file.close()

# reading text from the text file
new_file = open("new_text_file_2.txt", 'r')
c = new_file.read()
new_file.close()
print(c)

# copy from one text file to another new file
new_file2 = open("new_file-2.txt", "a")
new_file2.write(c)
new_file2.close()
