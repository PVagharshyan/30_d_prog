from utility import Utility

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
    def phone_number(self, new_phone_number: str) -> None:
        Utility.check_phone_number(new_phone_number)
        self._phone_number = new_phone_number

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    def address(self, new_address: str) -> None:
        Utility.check_address(new_address)
        self._address = new_address

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, new_email: str) -> None:
        Utility.check_email(new_email)
        self._email = new_email

class Customer:
    def __init__(self, name: str, contact_information: Info) -> None:
        self._contact_information = contact_information
        self.name = name

    def __str__(self) -> str:
        return f"contact information:\n {self._contact_information},\n name: {self._name}"

    @property
    def contact_information(self) -> str:
        return self._contact_information.__str__()

    @contact_information.setter
    def contact_information(self, new_contact_information: Info) -> None:
        self._contact_information = new_contact_information

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name) -> None:
        Utility.check_name(new_name)
        self._name = new_name

def main():
    i_1 = Info("077993788", "Antar 5rd", "paylak.vagharshyan@gmail.com")
    c_1 = Customer("Paylak", i_1)
    print(c_1)

if __name__ == "__main__":
    main()
