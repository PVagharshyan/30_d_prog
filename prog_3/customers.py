from orders import Order
from menus import Menu
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

class Customer:
    def __init__(self, name: str, contact_information: str) -> None:
        self.name = name
        self.contact_information = contact_information
        self._order_history = []

    def __str__(self) -> str:
        order_history = ""
        for i in order_history:
            order_history += i.display_order() + "\n"
        return f"name: {self.name},\ncontact information:\n {self.contact_information},\norder history:\n{order_history}"

    def place_order(self, menu, order_items):
        total_price = 0
        order_details = []
        for item_name in order_items:
            for dish in menu.menu_items:
                if item_name == dish.name:
                    total_price += dish.price
                    order_details.append(dish.get_description())
                    break
        order = Order(self, order_details, total_price)
        self._order_history.append(order)

    def view_order_history(self):
        result = f"Order History for {self.name}:" + "\n"
        for order in self._order_history:
            result += order.display_order() + "\n"
        return result

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
    i = Info("077789547", "dada", "paydd.dddd@gamil.com")
    c = Customer("Poxos", i)
    print(c)

if __name__ == "__main__":
    main()
