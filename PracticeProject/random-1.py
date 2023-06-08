
colors = ['white', 'black', 'red', 'green', 'orange', 'grey', 'pink', 'golden', 'blue', 'violate', 'yellow']

i1 = []
i2 = []
for x in colors:
    if len(x) <= 5:
        i1.append(x)
    else:
        i2.append(x)
print('i1 = ', i1, 'i2 = ', i2)
################################
dic = []
for x1 in colors:
    dic.append((x1, colors.index(x1)+1))

print('dict = ', dict(dic))
# print(dic)
################################
colors_dict = {}
for x2 in colors:
    colors_dict[colors.index(x2)+1] = x2

print('Colors dictionary = ', colors_dict)
# print(colors_dict.keys())
# print(colors_dict.values())
# print(dict(dic).get('red'))
# print(colors_dict.items())
################################
# List comprehension practice
i3 = [x3 for x3 in colors if len(x3) <= 5]
i4 = [x4 for x4 in colors if len(x4) > 5]
print(i3, i4)
print([x4 for x4 in colors if len(x4) > 4])
################################
# letters = [let for let in [color for x3 in colors]]
let = []
for q in range(len(colors)):
    letters = [letter for letter in colors[q]]
    let = let + letters

print('let = ', let)
uniq_letters = [uniq for uniq in let]
print(sorted(list(set(let))))

letter_dict = {}
for x5 in uniq_letters:
    letter_dict[x5] = let.count(x5)
print('Letter dictionary: ', letter_dict)
################################
print(letter_dict['e'])
