from abc import ABC, abstractmethod

class MedicalStaff(ABC):
    def __init__(self, name, position):
        self._name = name
        self._position = position

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
        self._position = new_position

class Surgeon(MedicalStaff):
    @abstractmethod
    def to_operate(self):
        ...

class Checker(MedicalStaff):
    @abstractmethod
    def check_ups(self):
        ...

class Thirsty(MedicalStaff):
    @abstractmethod
    def provide_service(self):
        ...

class Driver(Thirsty):
    def provide_service(self):
        print("Move to the appropriate location")

class Nurse(Checker, Surgeon):
    def check_ups(self):
        print("Move to the appropriate location!")

    def provide_service(self):
        print("care and provide appropriate medication")

def main():
    ...

if __name__ == "__main__":
    main()
