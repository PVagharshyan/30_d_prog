from utility import Utility
from cars import Car
import copy

class Salespeople:
    def __init__(self, name: str, commission_rate: float, cars: list["Car"]) -> None:
        self.name = name
        self.commission_rate = commission_rate
        self.cars = cars
        self._history = []

    def __str__(self) -> str:
        cars_str = ""
        for i in self.cars:
            cars_str += " " + i.__str__() + "\n"

        sales_history = ""
        for i in self.history:
            sales_history += " " + i.__str__() + "\n"

        return f"name: {self._name}, commission_rate: {self._commission_rate}, cars:\n{cars_str},\nhistory:\n{sales_history}"

    def done(self, car) -> None:
        if len(self.cars) == 0:
            raise Exception("Empty!!")
        elif not isinstance(car, Car):
            raise Exception("...")
        elif not self.search(car):
            raise Exception("Error!!")
        cars_arr = self.cars
        for i in range(len(cars_arr)):
            if cars_arr[i] == car:
                del self._cars[i]
                break
        self._history.append(car)

    def search(self, car) -> bool:
        if len(self.cars) == 0:
            return False
        for i in self.cars:
            if i == car:
                return True
        return False

    @property
    def history(self):
        return copy.deepcopy(self._history)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        Utility.check_name(new_name)
        self._name = new_name

    @property
    def commission_rate(self) -> float:
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, new_commission_rate: float) -> None:
        Utility.check_commission_rate(new_commission_rate)
        self._commission_rate = new_commission_rate

    @property
    def cars(self) -> list["Car"]:
        return copy.deepcopy(self._cars)

    @cars.setter
    def cars(self, cars: list["cars"]):
        Utility.check_cars(cars)
        self._cars = copy.deepcopy(cars)

def main():
    c_arr = [Car("ddd", "bbb", 24) for i in range(10)]
    s = Salespeople("Poxos", 4, c_arr)
    car = s.cars[0]
    print(s)
    s.done(car)
    s.done(car)
    s.done(car)
    s.done(car)
    s.done(car)
    s.done(car)
    s.done(car)
    print(s)

if __name__ == "__main__":
    main()
