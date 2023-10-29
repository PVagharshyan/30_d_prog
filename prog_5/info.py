import utility

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

