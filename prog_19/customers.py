from items import MenuItem
from orders import Order, Customer as Customer_o
from typing import List
import utility

class Customer(Customer_o):
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self._order_history: List['Order'] = []

    @property
    def name(self):
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, value: str):
        self._name = value

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(str)
    def contact_info(self, value: str):
        self._contact_info = value

    @utility.container_type_checking(list, MenuItem)
    def place_order(self, menu_items: List[MenuItem]) -> 'Order':
        order = Order(self, menu_items)
        self.order_history.append(order)
        return order

    @property
    def order_history(self):
        return self._order_history

    @order_history.setter
    @utility.container_type_checking(list, Order)
    def order_history(self, value: List['Order']):
        self._order_history = value

    def view_order_history(self) -> List['Order']:
        return self.order_history

    @utility.type_checking(Order, int, str)
    def leave_review(self, order: 'Order', rating: int, comments: str):
        order.add_review(rating, comments)
