from customers import Customer
from dishes import *
from menus import Menu

if __name__ == "__main__":
    menu = Menu()
    menu.add_item(Appetizer("Salad", 5.99))
    menu.add_item(Entree("Pasta", 12.99))
    menu.add_item(Appetizer("Garlic Bread", 4.49))
    menu.add_item(Entree("Steak", 19.99))

    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")

    customer1.place_order(menu, ["Salad", "Steak"])

    customer2.place_order(menu, ["Pasta", "Garlic Bread"])

    print(customer1.view_order_history())
    print(customer2.view_order_history())
