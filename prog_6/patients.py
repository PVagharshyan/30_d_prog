from utility import Utility

class Patients:
    def __init__(self, name, age, medical_history):
        self._name = name
        self._age = age
        self._medical_history = medical_history

    def __str__(self):
        return f"name: {self._name}, age: {self._age}, medical_history: {self._medical_history}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not utility.check_name(new_name):
            raise ValueError("non valid age")
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if not utility.check_age(new_age):
            raise ValueError("non valid age")
        self._age = age

    @property
    def medical_history(self):
        return self._medical_history

    @medical_history.setter
    def medical_history(self, new_medical_history):
        if not utility.check_medical_history(new_medical_history):
            raise ValueError("non valid age")
        self._medical_history = new_medical_history
