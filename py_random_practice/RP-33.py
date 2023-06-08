# Birthday dictionary

BD_dictionary = {
    "Asief": "03/02/1987",
    "Shushmita": "20/06/1988",
    "Sajjad": "21/06/1988"
}
print(BD_dictionary.keys())
print(BD_dictionary["Shushmita"])
user = input("put your name: ")
if user in BD_dictionary.keys():
    print(user, 'was born on ', BD_dictionary[user])
