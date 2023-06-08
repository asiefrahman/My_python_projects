# Practicing inheritance

class SmartDevices:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def recharge(self):
        print('I recharge through my charger!')


class Phone(SmartDevices):

    def __init__(self, brand, price, network):
        SmartDevices.__init__(self, brand, price)
        self.network = network


class SmartWatch(SmartDevices):

    def __init__(self, brand, price, has_gps):
        SmartDevices.__init__(self, brand, price)
        self.has_gps = has_gps


my_phone = Phone('xioami', 200, 'Tmobile')
my_phone.recharge()

My_watch = SmartWatch('fibit', 120, False)
My_watch.recharge()
