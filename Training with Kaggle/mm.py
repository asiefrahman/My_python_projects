'''
def search_key(doc_list, keyword):
    """
    """
    #a = list(doc_list)
    for d in doc_list:
        if d.count(keyword) >= 1:
            print(d)
        else:
            pass
    return d
'''
doc_list = ["The Learn Python Challenge Casino.", "They bought a car, and a horse", "Casinoville"]
keyword = 'car'
d = []
for doc in doc_list:
    if '.' in doc:
        w1 = str(doc.strip('.')).lower().strip(',').split(' ')
        if keyword.lower() in w1:
            d.append(doc_list.index(doc))
    elif ',' in doc:
        w2 = str(doc.strip(',')).lower().strip().split(' ')
        if keyword.lower() in w2:
            d.append(doc_list.index(doc))
    else:
        w3 = str(doc).lower().split(' ')
        if keyword.lower() in w3:
            d.append(doc_list.index(doc))
print(d)


