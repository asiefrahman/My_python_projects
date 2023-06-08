num1=float(input('Put first number= '))
num2=float(input('Put second number= '))
num3=float(input('Put third number= '))
if num1 > num2 and num2 > num3:
    print('First number is greatest')
elif num1<num2 and num2>num3:
    print('Second number is greatest')
else:
    print('Third number is greatest')

let1=str(input('Put a letter= '))
if let1=='a' or let1=='e' or let1=='i' or let1=='o' or let1=='u':
    print("It's a vowel")
else:
    print("it's a consonant")
