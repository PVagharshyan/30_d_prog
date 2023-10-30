from users import User
from exercises import Exercise
from abc import ABC, abstractmethod
from typing import List
import utility

class WorkoutPlan:
    def __init__(self, user: User, exercises: List[Exercise], duration: int):
        self.user = user
        self.exercises = exercises
        self.duration = duration

    @property
    def user(self):
        return self._user

    @user.setter
    @utility.type_checking(User)
    def user(self, new_user):
        self._user = new_user

    @property
    def exercises(self):
        return self._exercises

    @exercises.setter
    @utility.container_type_checking(list, Exercise)
    def exercises(self, new_exercises):
        self._exercises = new_exercises

    @property
    def duration(self):
        return self._duration

    @duration.setter
    @utility.type_checking(int)
    def duration(self, new_duration):
        self._duration = new_duration
