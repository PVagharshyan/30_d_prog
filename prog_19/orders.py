from items import MenuItem
from review import Review
from typing import List
import copy
import utility

class Customer:
    ...

class Order:
    def __init__(self, customer: Customer, menu_items: List[MenuItem]):
        self.customer = customer
        self.menu_items = menu_items
        self._total_price = sum(item.price for item in menu_items)
        self._reviews: List['Review'] = []

    @property
    def customer(self):
        return self._customer

    @customer.setter
    @utility.type_checking(Customer)
    def customer(self, value: Customer):
        self._customer = value

    @property
    def menu_items(self):
        return self._menu_items

    @menu_items.setter
    @utility.container_type_checking(list, MenuItem)
    def menu_items(self, value: List[MenuItem]):
        self._menu_items = value

    @property
    def total_price(self):
        return self._total_price

    @utility.type_checking(int, str)
    def add_review(self, rating: int, comments: str):
        review = Review(rating, comments)
        self._reviews.append(review)

    @property
    def reviews(self):
        return copy.deepcopy(self._reviews)
