# Determine summation & multiplication of numbers starting from 1

x=int(input('Put the last number: '))
sum=0
for x in range(1, x+1, 1):
    sum=sum+x
print(sum)

mul=1
sum1=0
for y in range(1, x+1, 1):
    mul=mul*y
    sum1=sum1+mul
print(sum1)

