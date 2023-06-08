# OOP inheritance
# a Phone class
class Phone:
    video_call = True

    def __init__(self, brand, price, network):
        self.brand = brand
        self.price = price
        self.network = network

    def recharge(self):
        print('Eating electricity :-)')
        print('Electrons are yummy!')


my_phone = Phone('Xioami', 200, 'Tmobile')
my_phone.recharge()


# a Watch class
class Watch:

    def __init__(self, brand, price, has_gps):
        self.brand = brand
        self.price = price
        self.step_count = 0
        self.has_gps = has_gps

    def recharge(self):
        print('Eating electricity :-)')
        print('Electrons are yummy!')


my_watch = Watch('Fitbit', 150, False)
my_watch.recharge()


# Creating a class to inherit to another class, i.e: Parent class or Base class
class Smartdevice:

    def recharge(self):
        print('Eating electricity :-)')
        print('Electrons are yummy!')


# inheriting a class to another class, i.e: Child class or derived class
class Smartphone(Smartdevice):

    def __init__(self, brand, price, network):
        self.brand = brand
        self.price = price
        self.network = network


my_smart_phone = Smartphone('Walton', 130, 'Stmobile')
my_smart_phone.recharge()


class Smartwatch(Smartdevice):

    def __init__(self, brand, price, has_gps):
        self.brand = brand
        self.price = price
        self.has_gps = False


my_smart_watch = Smartwatch('Fitbit', 120, False)
my_smart_watch.recharge()
