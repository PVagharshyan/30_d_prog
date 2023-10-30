from abc import ABC, abstractmethod
from typing import List
import utility

class Exercise:
    def __init__(self, name: str, muscle_group: str):
        self.name = name
        self.muscle_group = muscle_group

    @property
    def name(self):
        return self._name

    @name.setter
    @utility.type_checking(str)
    def name(self, new_name):
        self._name = new_name

    @property
    def muscle_group(self):
        return self._muscle_group

    @muscle_group.setter
    @utility.type_checking(str)
    def muscle_group(self, new_muscle_group):
        self._muscle_group = new_muscle_group


class CardioExercise(Exercise):
    def __init__(self, name: str, duration: int):
        super().__init__(name, "Cardio")
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    @utility.type_checking(int)
    def duration(self, new_duration):
        self._duration = new_duration


class StrengthExercise(Exercise):
    def __init__(self, name: str, sets: int, reps: int):
        super().__init__(name, "Strength")
        self.sets = sets
        self.reps = reps

    @property
    def sets(self):
        return self._sets

    @sets.setter
    @utility.type_checking(int)
    def sets(self, new_sets):
        self._sets = new_sets

    @property
    def reps(self):
        return self._reps

    @reps.setter
    @utility.type_checking(int)
    def reps(self, new_reps):
        self._reps = new_reps
