import utility
from movies import Movie, ACTION, COMEDY, DRAMA

class Rental:
    pass

class Info:
    def __init__(self, phone_number: str, address: str, email: str) -> None:
        self.phone_number = phone_number
        self.address = address
        self.email = email

    def __str__(self) -> str:
        return f"phone number: {self.phone_number}, address: {self.address}, email: {self.email}"

    @property
    def phone_number(self) -> str:
        return self._phone_number

    @phone_number.setter
    @utility.check_phone_number
    def phone_number(self, new_phone_number: str) -> None:
        self._phone_number = new_phone_number

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    @utility.check_str_data
    def address(self, new_address: str) -> None:
        self._address = new_address

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    @utility.check_email
    def email(self, new_email: str) -> None:
        self._email = new_email

class Customer:
    def __init__(self, name: str, contact_information: str) -> None:
        self.name = name
        self.contact_information = contact_information
        self._movies = []
        self._history = []

    def __str__(self) -> str:
        return f"name: {self.name},\ncontact information:\n {self.contact_information}"

    def add_movie(self, movie: Movie, duration: int) -> None:
        if not isinstance(movie, Movie) or not isinstance(duration, int):
            raise ValueError("...")
        self._movie.append(movie)
        self._history.append(Rental(self, movie, duration).get_info() + " -> rented!")

    def return_m(self, movie: Movie) -> None:
        if not isinstance(movie, Movie):
            raise ValueError("...")
        for i in self.movie:
            if i == movie:
                self._history.append(Rental(self, movie, 0) + " -> return")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.check_str_data
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def contact_information(self):
        return self._contact_information.__str__()

    @contact_information.setter
    def contact_information(self, new_contact_information: Info) -> None:
        self._contact_information = new_contact_information

def main():
    i = Info("077858584", "dads", "afd.sdfs@sfs.fsd")
    c = Customer("poxos", i)
    movie = Movie("fff", ACTION, 5)
    print(c)

if __name__ == "__main__":
    main()

