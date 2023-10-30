import utility

class Driver:
    ...

class Passenger:
    ...

class Ride:
    def __init__(self, driver: Driver, passenger: Passenger, destination: str, fare: float):
        self.driver = driver
        self.passenger = passenger
        self.destination = destination
        self.fare = fare
        self.accepted = False
        self.completed = False

    @property
    def driver(self):
        return self._driver

    @driver.setter
    @utility.type_checking(Driver)
    def driver(self, new_driver):
        self._driver = new_driver

    @property
    def passenger(self):
        return self._passenger

    @passenger.setter
    @utility.type_checking(Passenger)
    def passenger(self, new_passenger):
        self._passenger = new_passenger

    @property
    def destination(self):
        return self._destination

    @destination.setter
    @utility.type_checking(str)
    def destination(self, new_destination):
        self._destination = new_destination

    @property
    def fare(self):
        return self._fare

    @fare.setter
    @utility.type_checking((float, int))
    def fare(self, new_fare):
        self._fare = new_fare

    @utility.type_checking(Driver)
    def accept_ride(self, driver: Driver):
        if driver == self.driver:
            self.accepted = True

    def complete_ride(self):
        if self.accepted:
            self.completed = True
            self.driver.rides.remove(self)
