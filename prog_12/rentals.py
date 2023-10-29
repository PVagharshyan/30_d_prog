from cars import Car
import utility

class Customer_r:
    ...

class Rental:
    def __init__(self, customer: Customer_r, car: Car, duration: int, cost: float):
        self.customer = customer
        self.car = car
        self.duration = duration
        self.cost = cost

    def __str__(self) -> str:
        return f"Rental of {self.car.make} {self.car.model} for {self.duration} days at a cost of ${self.cost}"

    @property
    def customer(self) -> Customer_r:
        return self._customer

    @customer.setter
    @utility.type_checking(Customer_r)
    def customer(self, customer: Customer_r) -> None:
        self._customer = customer

    @property
    def car(self) -> Car:
        return self._car

    @car.setter
    @utility.type_checking(Car)
    def car(self, car: Car) -> None:
        self._car = car

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    @utility.type_checking(int)
    def duration(self, duration: int) -> None:
        self._duration = duration

    @property
    def cost(self) -> float:
        return self._cost

    @cost.setter
    @utility.type_checking(float)
    def cost(self, cost: float) -> None:
        self._cost = cost
