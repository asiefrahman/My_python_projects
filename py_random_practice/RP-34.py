# Loading a dictionary to a JSON file

import json
BD_dictionary = {
    "Asief": "03/02/1987",
    "Shushmita": "20/06/1988",
    "Sajjad": "21/06/1988",
    "Riddho": "25/09/1989",
    "Snigdho": "11/05/1989",
    "Albert Einstein": "14/03/1879",
    "Ada Byron Lovelace": "10/12/1815",
    "Benjamin Franklin": "17/01/1706",
    "Sheikh Mujib": "14/03/1913"
}

file = open("BD.JSON", "w")
json.dump(BD_dictionary, file)
file = open("BD.JSON", "r")
print(file.readlines())
file.close()

file1 = open("BD.JSON", "r")
BD = list([d.strip("\n") for d in file1.readlines()])
print('BD = ', BD)
