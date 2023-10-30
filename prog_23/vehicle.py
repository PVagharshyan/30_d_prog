import utility

class Vehicle:
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year

    @property
    def make(self):
        return self._make

    @make.setter
    @utility.type_checking(str)
    def make(self, new_make):
        self._make = new_make

    @property
    def model(self):
        return self._model

    @model.setter
    @utility.type_checking(str)
    def model(self, new_model):
        self._model = new_model

    @property
    def year(self):
        return self._year

    @year.setter
    @utility.type_checking(int)
    def year(self, new_year):
        self._year = new_year

class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, num_doors: int):
        super().__init__(make, model, year)
        self.num_doors = num_doors

    @property
    def num_doors(self):
        return self._num_doors

    @num_doors.setter
    @utility.type_checking(int)
    def num_doors(self, value: int):
        self._num_doors = value

class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, year: int, has_sidecar: bool):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    @property
    def has_sidecar(self):
        return self._has_sidecar

    @has_sidecar.setter
    @utility.type_checking(bool)
    def has_sidecar(self, value: bool):
        self._has_sidecar = value
