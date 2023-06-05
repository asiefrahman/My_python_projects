#get a cube sum from a given numebr

def cub_sum(num):
    a=range(1, num+1)
    b=0
    c=''
    for n in a:
        if n<=num+1:
            b=b+pow(n,3)
        if n<num+1:
            c=c+str(n)+'^3+'
        if n==num+1:
            c = c + str(n) + '^3'
    return c + '=' + str(b)

num=int(input('Please enter yoyr number: '))
print(cub_sum(num))