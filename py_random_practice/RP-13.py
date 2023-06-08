def fibonacci(num):
    fibo = [0, 1]
    i = 2
    while i <= num:
        next_fibo = fibo[i-1]+fibo[i-2]
        fibo.append(next_fibo)
        i += 1
    return fibo


a = int(input('enter your number: '))-1
print(fibonacci(a))
