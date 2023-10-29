from email_validator import validate_email, EmailNotValidError
from orders import Order, OnlineOrder, InStoreOrder
from product import Product, Clothing, Electronics
from typing import List
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
    @utility.type_checking(str)
    def phone_number(self, new_phone_number: str) -> None:
        self._phone_number = new_phone_number

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    @utility.type_checking(str)
    def address(self, new_address: str) -> None:
        self._address = new_address

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, new_email: str) -> None:
        validate_email(new_email)
        self._email = new_email

class Customer:
    def __init__(self, name: str, contact_information: str) -> None:
        self._history = []
        self._orders = []
        self.name = name
        self.contact_information = contact_information

    def __str__(self) -> str:
        return f"name: {self.name},\ncontact information:\n {self.contact_information}"

    @utility.container_type_checking(list, Product)
    def add_order(self, products: List['Product']) -> None:
        new_order = OnlineOrder(self.name, products)
        self._orders.append(new_order)
        self._history.append(f"{new_order}, ordered")

    def return_order_f(self) -> None:
        self._history.append(f"{self._orders[0]}, return order")
        del self._orders[0]

    def get_history(self) -> str:
        return utility.display_array(self._history)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def contact_information(self):
        return self._contact_information.__str__()

    @contact_information.setter
    @utility.type_checking(Info)
    def contact_information(self, new_contact_information: Info) -> None:
        self._contact_information = new_contact_information

def main():
    i = Info("025454584", "fsgddd", "ddd.rfrwe@sadasas.fd")
    p = Product("dsfdsf", 1323.2, "asfdsfs")
    c = Customer("poxos", i)
    c.add_order([p])
    print(c.get_history())
    print(c)

if __name__ == "__main__":
    main()

