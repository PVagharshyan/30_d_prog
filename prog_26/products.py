from abc import ABC, abstractmethod
from typing import List
import utility

class Product:
    def __init__(self, name: str, description: str, price: float, availability: int):
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, new_name: str):
        self._name = new_name

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    @utility.type_checking(str)
    def description(self, new_description: str):
        self._description = new_description

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    @utility.type_checking((int, float))
    def price(self, new_price: float):
        self._price = new_price

    @property
    def availability(self) -> int:
        return self._availability

    @availability.setter
    @utility.type_checking((int, float))
    def availability(self, new_availability: int):
        self._availability = new_availability

class ElectronicsProduct(Product):
    def __init__(self, name: str, description: str, price: float, availability: int, brand: str):
        super().__init__(name, description, price, availability)
        self.brand = brand

class ClothingProduct(Product):
    def __init__(self, name: str, description: str, price: float, availability: int, size: str):
        super().__init__(name, description, price, availability)
        self.size = size
