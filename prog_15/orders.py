from abc import ABC, abstractmethod
from typing import List
from products import Product
import utility

class Customer:
    ...

class Order:
    def __init__(self, customer: 'Customer', products: List['Product']):
        self.customer = customer
        self.products = products
        self.total_price = sum(product.price for product in products)

    @property
    def customer(self) -> 'Customer':
        return self._customer

    @customer.setter
    @utility.type_checking(Customer)
    def customer(self, value: 'Customer'):
        self._customer = value

    @property
    def products(self) -> List['Product']:
        return self._products

    @products.setter
    @utility.container_type_checking(list, Product)
    def products(self, value: List['Product']):
        self._products = value

    @property
    def total_price(self) -> float:
        return self._total_price

    @total_price.setter
    @utility.type_checking((float, int))
    def total_price(self, value: float):
        self._total_price = value

class OnlineShoppingPlatform(ABC):
    @abstractmethod
    def search_products(self, keyword: str) -> List['Product']:
        pass

    @abstractmethod
    def purchase_product(self, customer: 'Customer', product: 'Product') -> 'Order':
        pass

    @abstractmethod
    def view_order_history(self, customer: 'Customer') -> List['Order']:
        pass

class OnlineShoppingSite(OnlineShoppingPlatform):
    def __init__(self):
        self._products = []
        self._customers = []

    @utility.type_checking(str)
    def search_products(self, keyword: str) -> List[Product]:
        return [product for product in self._products if keyword in product.name or keyword in product.description]

    @utility.type_checking(Customer, Product)
    def purchase_product(self, customer: Customer, product: Product) -> Order:
        if product in self._products:
            order = customer.place_order([product])
            return order
        else:
            raise ValueError("Product not found")

    @utility.type_checking(Customer)
    def view_order_history(self, customer: Customer) -> List[Order]:
        return customer.order_history

    @property
    def products(self) -> List[Product]:
        return self._products

    @property
    def customers(self) -> List[Customer]:
        return self._customers
