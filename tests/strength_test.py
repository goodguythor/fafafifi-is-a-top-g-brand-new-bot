import unittest
import sys
import os
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

strength_responses = [
    "Wow, Ronnie Coleman must be so proud of you! Which body part did you just train?",
    "Strength training is the key to gains! What exercises did you do today?"
]

class TestStrength(unittest.TestCase):

    def test_train_my_muscles(self):
        user = "I train my muscles every day"
        res = reply(user)
        self.assertIn(res, strength_responses)

    def test_training_strength(self):
        user = "I'm training my strength now"
        res = reply(user)
        self.assertIn(res, strength_responses)

    def test_workout_my_muscle(self):
        user = "I did a workout my muscle today"
        res = reply(user)
        self.assertIn(res, strength_responses)

    def test_exercise_my_strength(self):
        user = "I exercise my strength to get better"
        res = reply(user)
        self.assertIn(res, strength_responses)

    def test_plural_muscles(self):
        user = "I am working out my muscles"
        res = reply(user)
        self.assertIn(res, strength_responses)

    def test_no_strength_context(self):
        user = "I am running fast today"
        res = reply(user)
        self.assertNotIn(res, strength_responses)

    def test_missing_my_keyword(self):
        user = "I train muscles"
        res = reply(user)
        self.assertNotIn(res, strength_responses)  # should fail since "my" is required

if __name__ == "__main__":
    unittest.main()