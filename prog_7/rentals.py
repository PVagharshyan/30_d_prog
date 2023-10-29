from movies import Movie, ACTION, COMEDY, DRAMA
from customers import Customer, Info

class Rental:
    def __init__(self, customer: Customer, movie: Movie, duration: int) -> None:
        self.customer = customer
        self.movie = movie
        self.duration = duration

    @property
    def customer(self) -> Customer:
        return self._customer

    @customer.setter
    def customer(self, new_customer: Customer) -> None:
        if isinstance(new_customer, Customer):
            self._customer = new_customer
        else:
            raise ValueError("Customer must be an instance of the Customer class")

    @property
    def movie(self) -> Movie:
        return self._movie

    @movie.setter
    def movie(self, new_movie: Movie) -> None:
        if isinstance(new_movie, Movie):
            self._movie = new_movie
        else:
            raise ValueError("Movie must be an instance of the Movie class")

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, new_duration: int) -> None:
        if isinstance(new_duration, int) and new_duration > 0:
            self._duration = new_duration
        else:
            raise ValueError("Duration must be a positive integer")

    def get_info(self) -> str:
        return f"Customer: {self.customer.name}, Movie: {self.movie.title}, Duration: {self.duration} days"

def main():
    i = Info("030303030", "ddddd", "asfda.dfds@fdsf.am")
    c = Customer("dssds", i)
    m = Movie("sfdsfd", ACTION(), 4)
    r = Rental(c, m, 48)
    print(r.get_info())

if __name__ == "__main__":
    main()
