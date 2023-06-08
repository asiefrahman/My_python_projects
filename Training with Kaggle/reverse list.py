p = [2, 6, 5]

'''
def rev_list(list1):
    r = []
    while len(r) <= len(list1):
        r.append(list1[len(list1) - len(r)])
    print(r)
rev_list(p)
'''
def purple_shell(racers):
    r = []
    while len(racers)>0:
        L = racers.pop()
        r.append(L)
    print(r)

print(purple_shell(p))