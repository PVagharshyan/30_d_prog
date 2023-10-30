import utility
class Theater:
    def __init__(self, location: str, seating_capacity: int):
        self.location = location
        self.seating_capacity = seating_capacity

    @property
    def location(self) -> str:
        return self._location

    @location.setter
    @utility.type_checking(str)
    def location(self, new_location: str):
        self._location = new_location

    @property
    def seating_capacity(self) -> int:
        return self._seating_capacity

    @seating_capacity.setter
    @utility.type_checking(int)
    def seating_capacity(self, new_seating_capacity: int):
        if new_seating_capacity >= 0:
            self._seating_capacity = new_seating_capacity
        else:
            raise ValueError("Seating capacity must be non-negative")


class StandardTheater(Theater):
    def __init__(self, location: str, seating_capacity: int):
        super().__init__(location, seating_capacity)

class IMAXTheater(Theater):
    def __init__(self, location: str, seating_capacity: int):
        super().__init__(location, seating_capacity)
