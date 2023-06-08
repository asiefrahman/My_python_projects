# Determine HCF & LCM of two numbers

x,y = input("Enter two integer").split()
x,y = [int(x), int(y)] #convert input string to integers


a = x
b = y

while(b != 0 ):
	t = b
	b = a % b
	a = t

hcf = a
lcm = (x*y)/hcf

print("HCF of %d and %d is %dn" %(x,y,hcf))
print("LCM of %d and %d is %dn" %(x,y,lcm))