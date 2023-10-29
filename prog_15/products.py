from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name: str, price: float, description: str):
        self.name = name
        self.price = price
        self.description = description

class ProductWithReview(Product):
    def __init__(self, name: str, price: float, description: str):
        super().__init__(name, price, description)
        self.reviews = []

    def add_review(self, customer: 'Customer', review: str):
        self.reviews.append((customer, review))

class ElectronicProduct(ProductWithReview):
    def __init__(self, name: str, price: float, description: str, brand: str):
        super().__init__(name, price, description)
        self.brand = brand

class ClothingProduct(ProductWithReview):
    def __init__(self, name: str, price: float, description: str, size: str):
        super().__init__(name, price, description)
        self.size = size
