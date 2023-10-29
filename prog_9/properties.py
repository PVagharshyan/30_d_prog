from abc import ABC, abstractmethod
import utility

class Property(ABC):
    def __init__(self, address: str, price: (float, int), features: str) -> None:
        self.address = address
        self.price = price
        self.features = features

    @property
    def address(self) -> str:
        return self._address

    @address.setter
    @utility.type_checking(str)
    def address(self, value: str) -> None:
        self._address = value

    @property
    def price(self) -> (float, int):
        return self._price

    @price.setter
    @utility.type_checking((float, int))
    def price(self, value: (float, int)) -> None:
        # Add validation logic if needed
        self._price = value

    @property
    def features(self) -> str:
        return self._features

    @features.setter
    @utility.type_checking(str)
    def features(self, value: str) -> None:
        self._features = value

    @abstractmethod
    def property_type(self):
        pass

    def __str__(self):
        return f"{self.property_type()} Property - Address: {self.address}, Price: ${self.price}"

class ResidentialProperty(Property):
    def property_type(self):
        return "Residential"

class CommercialProperty(Property):
    def property_type(self):
        return "Commercial"
