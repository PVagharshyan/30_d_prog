from abc import ABC, abstractmethod
from typing import List, Union
from cars import Car
from rentals import Rental, Customer_r
from info import Info
import copy
import utility

class Customer(Customer_r):
    def __init__(self, name: str, contact_info: Info):
        self.name = name
        self.contact_info = contact_info
        self._rental_history: List[Rental] = []

    @utility.type_checking(Car, int)
    def rent_car(self, car: Car, rental_duration: int) -> Union[Rental, None]:
        if car.available:
            rental_cost = car.rental_price * rental_duration
            rental = Rental(self, car, rental_duration, rental_cost)
            car.available = False
            self.rental_history.append(rental)
            return rental
        else:
            print(f"Sorry, the {car.make} {car.model} is not available for rent.")
            return None

    @utility.type_checking(Rental)
    def return_car(self, rental: Rental) -> None:
        rental.car.available = True

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, name: str) -> None:
        self._name = name

    @property
    def contact_info(self) -> str:
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(Info)
    def contact_info(self, contact_info: Info) -> None:
        self._contact_info = contact_info

    @property
    def rental_history(self) -> List[Rental]:
        return copy.deepcopy(self._rental_history)
