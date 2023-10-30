import utility
from typing import List

class MenuItem:
    def __init__(self, name: str, price: float, ingredients: List[str]):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, name: str):
        self._name = name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    @utility.type_checking(float)
    def price(self, price: float):
        self._price = price

    @property
    def ingredients(self) -> List[str]:
        return self._ingredients

    @ingredients.setter
    @utility.container_type_checking(list, str)
    def ingredients(self, ingredients: List[str]):
        self._ingredients = ingredients

class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, ingredients: List[str]):
        super().__init__(name, price, ingredients)

class Entree(MenuItem):
    def __init__(self, name: str, price: float, ingredients: List[str]):
        super().__init__(name, price, ingredients)
