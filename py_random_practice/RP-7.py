a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# x=list(num)
# y=x.splt()
y = []
for m in a:
    if int(m) % 2 == 0:
        y.append(m)
    else:
        continue

print(y)

