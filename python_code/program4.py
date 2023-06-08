result1=55
result2=float(input('Put Students marks: '))
if result2>= result1:
    if result2>=80:
        print('Congratulations! '+'You have got A+ ' + 'Your score is ', result2)
    elif 70<=result2<80:
        print('Congrates!'+'You have got A '+'Your score is ', result2)
    elif 60<=result2<70:
        print('Congrates!'+'You have got A- '+'Your score is ', result2)
    else:
        print('Please try again the first round')
else:
    print('Sorry You are disqualified for the round')



