from drivers import Driver
from passengers import Passenger
from rides import Ride
from user import User
from vehicle import Vehicle, Car, Motorcycle

if __name__ == "__main__":
    car1 = Car("Toyota", "Camry", 2020, 4)
    car2 = Car("Honda", "Civic", 2021, 2)
    motorcycle1 = Motorcycle("Harley-Davidson", "Sportster", 2019, False)

    passenger1 = Passenger("Alice", "alice@example.com")
    driver1 = Driver("Bob", "bob@example.com", car1)
    driver2 = Driver("Charlie", "charlie@example.com", motorcycle1)

    ride1 = passenger1.request_ride(driver1, "Airport", 30.0)
    driver1.accept_ride(ride1)
    driver1.complete_ride(ride1)

    print(f"{passenger1.name} took a ride with {driver1.name} to {ride1.destination} for ${ride1.fare}.")
