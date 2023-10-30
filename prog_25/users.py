from exercises import Exercise
from abc import ABC, abstractmethod
from typing import List
import utility

class User:
    def __init__(self, name: str, contact_info: str):
        self.name = name
        self.contact_info = contact_info
        self.favorite_exercises: List[Exercise] = []

    @property
    def name(self):
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, new_name):
        self._name = new_name

    @property
    def contact_info(self):
        return self._contact_info

    @contact_info.setter
    @utility.type_checking(str)
    def contact_info(self, new_contact_info):
        self._contact_info = new_contact_info

    @property
    def favorite_exercises(self):
        return self._favorite_exercises

    @favorite_exercises.setter
    @utility.container_type_checking(list, Exercise)
    def favorite_exercises(self, new_favorite_exercises):
        self._favorite_exercises = new_favorite_exercises
