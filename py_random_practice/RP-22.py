# reading name list from a text file, make a list of those, find total number and list unique names in the list

name_list = open("namelist.txt", "r")
x = set([d.strip("\n") for d in name_list.readlines()])
q = list(x)
print(q, "\n", len(q))
