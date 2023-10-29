from abc import ABC, abstractmethod

class Dish(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_description(self):
        pass

class Appetizer(Dish):
    def get_description(self):
        return f"Appetizer: {self.name}, Price: ${self.price}"

class Entree(Dish):
    def get_description(self):
        return f"Entree: {self.name}, Price: ${self.price}"
