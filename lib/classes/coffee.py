class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._customers = []
        Coffee.all.append(self)


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if type(value) == str and not hasattr(self, 'name'):
            self._name = value
        else:
            raise Exception("value must be a string and value cannot be changed if exists")
        
    def orders(self, new_order=None):
        from classes.order import Order
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        from classes.order import Order
        if isinstance(new_customer, Customer):
            self._customers.append(new_customer)
        return [order.customer for order in Order.all if order.coffee == self]

    
    def num_orders(self):
        from classes.order import Order
        return len([order.coffee for order in Order.all if order.coffee == self])
    
    def average_price(self):
        from classes.order import Order
        sum = 0
        price_list = [order.price for order in Order.all if order.coffee == self]
        number_orders  = len(price_list)
        for price in price_list:
            sum += price
        try:
            return sum / number_orders
        except ValueError:
            raise ValueError("denominator cannot be zero")

        