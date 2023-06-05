# determine who are fashionably late

def fash_late(guests):
    r = []
    w = range(0, len(guests))
    for a in w:
        if a > len(guests)//2 and a != len(guests)-1:
            r.append(guests[a])
        else:
            pass
    print(r)

guests_list = ['l', 'x', 'u', 'f', 'q', 'j', 'h', 's', 'n', 'c', 't', 'f', 'e', 't']

print(fash_late(guests_list))

