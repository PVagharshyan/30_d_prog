from abc import ABC, abstractmethod
from typing import List
from exercises import Exercise, CardioExercise, StrengthExercise
from users import User
from workout_plans import WorkoutPlan
from fitness_app import FitnessApp

def main():
    user1 = User("Alice", "alice@example.com")
    user2 = User("Bob", "bob@example.com")
    exercise1 = CardioExercise("Running", 30)
    exercise2 = StrengthExercise("Push-ups", 3, 15)

    user1.favorite_exercises = [exercise1, exercise2]

    app = FitnessApp()

    app.track_progress(user1, exercise1)
    plan = app.create_workout_plan(user1, [exercise1, exercise2], 60)
    app.connect_with_others(user1, [user2])

if __name__ == "__main__":
    main()
