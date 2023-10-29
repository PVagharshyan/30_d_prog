import utility

class Order:
    def __init__(self, customer, order_items, total_price):
        self.customer = customer
        self.order_items = order_items
        self.total_price = total_price

    def display_order(self) -> str:
        result = f"Customer: {self.customer.name}" + "\n"
        result += "Order Items:" + "\n"
        for item in self.order_items:
            result += item + "\n"
        result += f"Total Price: ${self.total_price}" + "\n"
        return result

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, new_customer):
        self._customer = new_customer

    @property
    def order_items(self):
        return self._order_items

    @order_items.setter
    @utility.check_order_items
    def order_items(self, new_order_items):
        self._order_items = new_order_items

    @property
    def total_price(self):
        return self._total_price

    @total_price.setter
    @utility.check_num_data
    def total_price(self, new_total_price):
        self._total_price = new_total_price
