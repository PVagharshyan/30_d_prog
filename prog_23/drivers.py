from vehicle import Vehicle
from user import User
from rides import Ride, Driver as Driver_r
import utility
import copy

class Driver(User, Driver_r):
    def __init__(self, name: str, contact_info: str, vehicle: Vehicle):
        super().__init__(name, contact_info)
        self.vehicle = vehicle
        self._rides: List['Ride'] = []

    @property
    def vehicle(self):
        return self._vehicle

    @vehicle.setter
    @utility.type_checking(Vehicle)
    def vehicle(self, value: Vehicle):
        self._vehicle = value

    @property
    def rides(self):
        return self._rides

    @utility.type_checking(Ride)
    def receive_ride_request(self, ride: 'Ride'):
        self._rides.append(ride)

    @utility.type_checking(Ride)
    def accept_ride(self, ride: 'Ride'):
        ride.accept_ride(self)

    @utility.type_checking(Ride)
    def complete_ride(self, ride: 'Ride'):
        ride.complete_ride()
