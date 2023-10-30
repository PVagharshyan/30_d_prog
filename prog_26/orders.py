from customers import Customer, Order as Order_c
from products import Product
from abc import ABC, abstractmethod
from typing import List
import utility

class Order(Order_c):
    def __init__(self, customer: Customer, products: List[Product]):
        self.customer = customer
        self.products = products
        self.order_total = sum(product.price for product in products)

    @property
    def customer(self) -> Customer:
        return self._customer

    @customer.setter
    @utility.type_checking(Customer)
    def customer(self, new_customer: Customer):
        self._customer = new_customer

    @property
    def products(self) -> List[Product]:
        return self._products

    @products.setter
    @utility.container_type_checking(list, Product)
    def products(self, new_products: List[Product]):
        self._products = new_products

    @property
    def order_total(self) -> float:
        return self._order_total

    @order_total.setter
    @utility.type_checking((int, float))
    def order_total(self, value: (int, float)):
        self._order_total = value
