class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        self._orders = []
        self._coffees = []
        Customer.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if type(value)== str and 1<=len(value)<=15:
            self._name = value
        else:
            raise Exception("value must be a string and must be at least 1 character long")
        
    def orders(self, new_order=None):
        from classes.order import Order
        if isinstance(new_order, Order):
            self._orders.append(new_order)
        return [order for order in Order.all if order.customer==self]
    
    def coffees(self, new_coffee=None):
        from classes.coffee import Coffee
        from classes.order import Order
        if isinstance(new_coffee, Coffee):
            self._coffees.append(new_coffee)
        coffee_list = [order.coffee for order in Order.all if order.customer==self]
        unique_list = []
        for coffee in coffee_list:
            if coffee not in unique_list:
                unique_list.append(coffee)
        return unique_list

        
    
    def create_order(self, coffee, price):
        from classes.coffee import Coffee
        from classes.order import Order
        if isinstance(coffee, Coffee) and isinstance(price,Order):
            the_order = [order for order in Order.all if order.coffee==coffee and order.price==price]
            self._orders += the_order