smallest = None
print("Before:", smallest)
for itervar in [3, 41, 2, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        #break
    #print("Loop:", itervar, smallest)
print("Smallest:", smallest)
