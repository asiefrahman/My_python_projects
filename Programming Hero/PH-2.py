#removing duplicates

'''a=input('Enter your word:')
list=list(dict.fromkeys(a))
print(sorted(list))'''


'''def rem_duplicate(sentence):
    for char in sentence:
        s=list(dict.fromkeys(sentence))
    return s

b=input('bull shit')
print(rem_duplicate(b))'''

def rem_duplicate(sentence):
    u=[]
    for char in sentence:
        if char not in u:
            u.append(char)
        else:
            continue
    return u

c=input('please enter ypur words:')
print(rem_duplicate(c))
