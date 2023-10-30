from typing import List, Optional
import utility

class Room:
    def __init__(self, room_number: int, price: float, amenities: List[str]):
        self.room_number = room_number
        self.price = price
        self.amenities = amenities

    @property
    def room_number(self):
        return self._room_number

    @room_number.setter
    @utility.type_checking(int)
    def room_number(self, value: int):
        self._room_number = value

    @property
    def price(self):
        return self._price

    @price.setter
    @utility.type_checking(float)
    def price(self, value: float):
        self._price = value

    @property
    def amenities(self):
        return self._amenities

    @amenities.setter
    @utility.container_type_checking(list, str)
    def amenities(self, value: str):
        self._amenities = value

class StandardRoom(Room):
    def __init__(self, room_number: int, price: float, amenities: List[str]):
        super().__init__(room_number, price, amenities)

class DeluxeRoom(Room):
    def __init__(self, room_number: int, price: float, amenities: List[str]):
        super().__init__(room_number, price, amenities)
