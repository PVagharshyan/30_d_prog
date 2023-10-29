from typing import List
from abc import ABC, abstractmethod
from products import Product, ElectronicProduct, ClothingProduct, ProductWithReview
from orders import Order, OnlineShoppingSite, OnlineShoppingPlatform
from customers import Customer

if __name__ == "__main__":
    online_shopping_site = OnlineShoppingSite()
    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")

    phone = ElectronicProduct("Smartphone", 500, "High-end smartphone", "Samsung")
    shirt = ClothingProduct("T-Shirt", 20, "Cotton T-shirt", "L")

    online_shopping_site.products.extend([phone, shirt])
    online_shopping_site.customers.extend([customer1, customer2])

    order1 = online_shopping_site.purchase_product(customer1, phone)
    order2 = online_shopping_site.purchase_product(customer2, shirt)

    customer1.leave_review(phone, "Great phone!")
    customer2.leave_review(shirt, "Comfortable shirt!")

    print(f"Customer 1's order history:")
    for order in online_shopping_site.view_order_history(customer1):
        print(f"Order Total Price: ${order.total_price}")

    print(f"Customer 2's order history:")
    for order in online_shopping_site.view_order_history(customer2):
        print(f"Order Total Price: ${order.total_price}")
