from abc import ABC, abstractmethod
import utility

class Product(ABC):
    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self) -> str:
        return f"name: {self.name}, price: {self.price}, description: {self.description}"

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, value: str) -> None:
        self._name = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    @utility.type_checking(float)
    def price(self, value: float) -> None:
        self._price = value

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    @utility.type_checking(str)
    def description(self, value: str) -> None:
        self._description = value

class Electronics(Product):
    def __init__(self, name: str, price: float, description: str, brand: str) -> None:
        super().__init__(name, price, description)
        self.brand = brand

    def __str__(self):
        return super().__str__() + f"\nBrand: {self.brand}"

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    @utility.type_checking(str)
    def brand(self, value: str) -> None:
        self._brand = value

class Clothing(Product):
    def __init__(self, name: str, price: float, description: str, size: int) -> None:
        super().__init__(name, price, description)
        self.size = size

    def __str__(self):
        return super().__str__() + f"\nSize: {self.size}"

    @property
    def size(self) -> int:
        return self._size

    @size.setter
    @utility.type_checking(int)
    def size(self, value: int) -> None:
        self._size = value
