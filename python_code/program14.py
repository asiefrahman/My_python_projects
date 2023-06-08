#replacing position 

a=input('Put your string: ')

def replace_pos(pos):
    x=''
    for m in range(0, len(a)):
        if m<len(a) and m%2!=0:
            x=x+a[m]+a[m-1]
        elif m==len(a)-1:
            x=x+a[m]
    print(x)

print(replace_pos(a))