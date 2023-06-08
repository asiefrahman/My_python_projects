# Real Python Practice problem no 1
# Caesar Cipher
import string
x = string.ascii_lowercase
print(x[:])
m = x[4:] + x[:4]
print(m)
a = str.maketrans(x, m)
print(a)
