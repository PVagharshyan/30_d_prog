from products import Product
from orders import Order, Customer as Customer_o
from typing import List
import copy
import utility

class Customer(Customer_o):
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self._order_history = []

    @utility.container_type_checking(list, Product)
    def place_order(self, products: List[Product]) -> Order:
        order = Order(self, products)
        self._order_history.append(order)
        return order

    @utility.type_checking(Product, str)
    def leave_review(self, product: Product, review: str):
        product.add_review(self, review)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, value: str):
        self._name = value

    @property
    def contact_info(self) -> str:
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(str)
    def contact_info(self, value: str):
        if not isinstance(value, str):
            raise ValueError("Contact info must be a string")
        self._contact_info = value

    @property
    def order_history(self) -> List['Order']:
        return copy.deepcopy(self._order_history)
