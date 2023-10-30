from user import User
from vehicle import Vehicle
from rides import Ride, Passenger as Passenger_r
import utility

class Passenger(User, Passenger_r):
    @utility.type_checking(User, str, (int, float))
    def request_ride(self, driver: User, destination: str, fare: float) -> 'Ride':
        ride = Ride(driver, self, destination, fare)
        driver.receive_ride_request(ride)
        return ride
