from abc import ABC, abstractmethod
from typing import List
from users import User
from exercises import Exercise
from workout_plans import WorkoutPlan
import utility

class FitnessTracker(ABC):
    @abstractmethod
    def track_progress(self, user: User, exercise: Exercise):
        pass

    @abstractmethod
    def create_workout_plan(self, user: User, exercises: List[Exercise], duration: int):
        pass

    @abstractmethod
    def connect_with_others(self, user: User, other_users: List[User]):
        pass

class FitnessApp(FitnessTracker):
    @utility.type_checking(User, Exercise)
    def track_progress(self, user: User, exercise: Exercise):
        print(f"{user.name} tracked progress for exercise: {exercise.name}")

    def create_workout_plan(self, user: User, exercises: List[Exercise], duration: int):
        if not isinstance(user, User) or not isinstance(exercises, list) or not isinstance(duration, int):
            raise ValueError("...")
        for i in exercises:
            if not isinstance(i, Exercise):
                raise ValueError("...")
        plan = WorkoutPlan(user, exercises, duration)
        return plan

    def connect_with_others(self, user: User, other_users: List[User]):
        print(f"{user.name} connected with other users: {[u.name for u in other_users]}")
