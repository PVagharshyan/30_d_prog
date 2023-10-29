from typing import List
from product import Product, Clothing, Electronics
from abc import ABC, abstractmethod
import copy
import utility

class Order(ABC):
    @staticmethod
    def to_count_total_price(products: List['Product']) -> float:
        return sum([i.price for i in products])

    def __init__(self, customer: str, products: List['Product']):
        self.customer = customer
        self.products = copy.deepcopy(products)
        self._total_price = self.to_count_total_price(products)

    def __str__(self) -> str:
        return f"customer: {self.customer}, total price: {self._total_price},\nproducts:\n{utility.display_array(self.products)}"

    @property
    def customer(self) -> str:
        return copy.deepcopy(self._customer)

    @customer.setter
    @utility.type_checking(str)
    def customer(self, value: str) -> None:
        self._customer = value

    @property
    def products(self):
        return copy.deepcopy(self._products)

    @products.setter
    @utility.container_type_checking(list, Product)
    def products(self, value: List['Product']) -> None:
        self._products = copy.deepcopy(value)
        self._total_price = self.to_count_total_price(self._products)

    @property
    def total_price(self) -> float:
        return self.to_count_total_price(self._products)

    @abstractmethod
    def get_order_type(self) -> str:
        ...

class OnlineOrder(Order):
    def get_order_type(self):
        return "Online Order"

class InStoreOrder(Order):
    def get_order_type(self):
        return "In-Store Order"

def main():
    arr = [Electronics("apranq", 45.4, "shat lav apranq", "LG") for i in range(10)]
    arr1 = [Clothing("apranq", 45.4, "shat lav apranq", 10) for i in range(10)]
    o = OnlineOrder("Name", arr)
    o1 = InStoreOrder("Name1", arr1)
    print(o)
    print(o1)
    print("order type:", o.get_order_type())

if __name__ == "__main__":
    main()
