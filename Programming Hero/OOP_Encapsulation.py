# OOP Encapsulation

class Bank:
    def __init__(self, name, __balance):
        self.name = name
        self.__balance = __balance   # double underscore is used to protect access from outside

    def get_balance(self):  # introducing method to access the protected or encapsulated elements
        return self.__balance


a = 'Asief Rahman'
myaccount = Bank(a, 20000)
print(myaccount.name)
print(myaccount.get_balance())
