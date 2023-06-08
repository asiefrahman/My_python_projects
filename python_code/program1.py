# print name and age as user input

Name=input('Enter your name: ')
age= input('Enter your age: ')


print('My name is '+ Name)
print('I am', age, 'years old')

p = 'My name is {}\nI am {} years old'
print(p.format(Name, age))

