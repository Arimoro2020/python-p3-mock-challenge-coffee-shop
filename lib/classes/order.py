
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

@property
def price(self):
    return self._price
@price.setter
def price(self, value):
    if type(value) == int and 1<=value<=10:
        self._price = value
    else:
        raise Exception("value must be an integer between 1 and 10")
    
