from customers import Customer
from items import MenuItem, Appetizer, Entree
from orders import Order
from review import Review

if __name__ == "__main__":
    appetizer1 = Appetizer("Salad", 7.99, ["Lettuce", "Tomato", "Cucumber"])
    entree1 = Entree("Pasta", 12.99, ["Pasta", "Tomato Sauce", "Parmesan"])

    customer1 = Customer("Alice", "alice@example.com")

    order1 = customer1.place_order([appetizer1, entree1])
    order1.add_review(4, "Delicious pasta!")

    customer2 = Customer("Bob", "bob@example.com")
    order2 = customer2.place_order([entree1])
    order2.add_review(5, "Fantastic meal!")

    print(f"{customer1.name}'s Order History:")
    for order in customer1.view_order_history():
        print(f"Order Total: ${order.total_price:.2f}")
        for item in order.menu_items:
            print(f"- {item.name}: ${item.price:.2f}")
        for review in order.reviews:
            print(f"Review: Rating {review.rating} - {review.comments}")
        print()

    print(f"{customer2.name}'s Order History:")
    for order in customer2.view_order_history():
        print(f"Order Total: ${order.total_price:.2f}")
        for item in order.menu_items:
            print(f"- {item.name}: ${item.price:.2f}")
        for review in order.reviews:
            print(f"Review: Rating {review.rating} - {review.comments}")
        print()
