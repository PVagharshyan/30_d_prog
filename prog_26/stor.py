from products import Product
from customers import Customer
from orders import Order
from abc import ABC, abstractmethod
from typing import List
import utility

class ECommercePlatform(ABC):
    @abstractmethod
    def browse_products(self):
        pass

    @abstractmethod
    def purchase_products(self, customer: Customer, products: List[Product]):
        pass

    @abstractmethod
    def view_past_orders(self, customer: Customer):
        pass

    @abstractmethod
    def leave_review(self, customer: Customer, product: Product, review: str):
        pass

class OnlineStore(ECommercePlatform):
    def __init__(self):
        self.products: List[Product] = []

    def browse_products(self):
        return self.products

    def purchase_products(self, customer: Customer, products: List[Product]):
        if not isinstance(customer, Customer) or not isinstance(products, list):
            raise ValueError("...")

        for i in products:
            if not isinstance(i, Product):
                raise ValueError("...")

        if all(product.availability > 0 for product in products):
            order = Order(customer, products)
            customer.past_orders.append(order)
            for product in products:
                product.availability -= 1
            return order
        else:
            return None

    @utility.type_checking(Customer)
    def view_past_orders(self, customer: Customer):
        return customer.past_orders

    @utility.type_checking(Customer, Product, str)
    def leave_review(self, customer: Customer, product: Product, review: str):
        pass
