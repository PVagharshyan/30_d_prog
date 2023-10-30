from products import Product, ClothingProduct, ElectronicsProduct
from customers import Customer
from orders import Order
from stor import OnlineStore


def main():
    customer1 = Customer("Alice", "alice@example.com")
    customer2 = Customer("Bob", "bob@example.com")
    electronics_product = ElectronicsProduct("Smartphone", "High-end smartphone", 599.99, 10, "Samsung")
    clothing_product = ClothingProduct("T-Shirt", "Cotton T-shirt", 19.99, 50, "Medium")

    store = OnlineStore()
    store.products = [electronics_product, clothing_product]

    order1 = store.purchase_products(customer1, [electronics_product, clothing_product])
    order2 = store.purchase_products(customer2, [electronics_product])

    past_orders1 = store.view_past_orders(customer1)
    past_orders2 = store.view_past_orders(customer2)

if __name__ == "__main__":
    main()
