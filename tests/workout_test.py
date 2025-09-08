import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

workout_responses = [
    "That's cool, is it strength training or cardio?"
]

class TestSimpleWorkout(unittest.TestCase):

    def test_simple_workout(self):
        user = "I workout every morning"
        res = reply(user)
        self.assertIn(res, workout_responses)

    def test_plural_workouts(self):
        user = "I do workouts daily"
        res = reply(user)
        self.assertIn(res, workout_responses)

    def test_working_out(self):
        user = "I'm working out now"
        res = reply(user)
        self.assertIn(res, workout_responses)

    def test_exercise_word(self):
        user = "I exercise a lot"
        res = reply(user)
        self.assertIn(res, workout_responses)

    def test_exercising_form(self):
        user = "I am exercising today"
        res = reply(user)
        self.assertIn(res, workout_responses)

    def test_negative_case(self):
        user = "I am cooking dinner"
        res = reply(user)
        self.assertNotIn(res, workout_responses)

if __name__ == "__main__":
    unittest.main()