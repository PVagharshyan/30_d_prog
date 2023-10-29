from cars import Car, EconomyCar, LuxuryCar
from customers import Customer
from info import Info
from rentals import Rental

if __name__ == "__main__":
    economy_car = EconomyCar("Toyota", "Corolla", 40.0)
    luxury_car = LuxuryCar("BMW", "X5", 100.0)

    i1 = Info("093494949", "dasdas", "paylak.vagharshyan@gamil.com")
    i2 = Info("093494945", "dasdas", "paylak.vagharshyan@gamil.com")
    customer1 = Customer("Alice", i1)
    customer2 = Customer("Bob", i2)

    rental1 = customer1.rent_car(economy_car, 5)
    rental2 = customer2.rent_car(luxury_car, 3)

    print(rental1)
    print(rental2)

    customer1.return_car(rental1)
    customer2.return_car(rental2)

    print(f"{customer1.name}'s Rental History:")
    for rental in customer1.rental_history:
        print(rental)

    print(f"{customer2.name}'s Rental History:")
    for rental in customer2.rental_history:
        print(rental)
