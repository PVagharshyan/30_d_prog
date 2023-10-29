from abc import ABC, abstractmethod
from typing import List, Union
import utility

class Car(ABC):
    def __init__(self, make: str, model: str, rental_price: float):
        self.make = make
        self.model = model
        self.rental_price = rental_price
        self.available = True

    @abstractmethod
    def get_car_type(self) -> str:
        pass

    @property
    def make(self) -> str:
        return self._make

    @make.setter
    @utility.type_checking(str)
    def make(self, make: str) -> None:
        self._make = make

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    @utility.type_checking(str)
    def model(self, model: str) -> None:
        self._model = model

    @property
    def rental_price(self) -> float:
        return self._rental_price

    @rental_price.setter
    @utility.type_checking(float)
    def rental_price(self, rental_price: float) -> None:
        self._rental_price = rental_price

    @property
    def available(self) -> bool:
        return self._available

    @available.setter
    @utility.type_checking(bool)
    def available(self, available: bool) -> None:
        self._available = available

class EconomyCar(Car):
    def get_car_type(self) -> str:
        return "Economy"

class LuxuryCar(Car):
    def get_car_type(self) -> str:
        return "Luxury"
