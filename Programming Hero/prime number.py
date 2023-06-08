def tell_prime(num):
    for i in range(2, num):
        if num%i==0:
            return False
        return True


def prime_list(num):
    show_prime = []
    for j in range(2, num+1):
       if tell_prime(j) is True:
           show_prime.append(j)
    return show_prime

num=int(input('Enter your number: '))
show_prime=prime_list(num)
print('List of Prime numbers: ', show_prime)
print(len(show_prime))