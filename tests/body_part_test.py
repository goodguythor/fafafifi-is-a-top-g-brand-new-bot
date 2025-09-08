import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply, reflect

body_responses = [
    "Yeah Buddy {X}, You must've been stronger rn.",
]

class TestBodyPartExercise(unittest.TestCase):

    def test_train_arm(self):
        user = "I train my arm"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in body_responses])

    def test_workout_legs(self):
        user = "I'm workout my legs"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in body_responses])

    def test_exercise_core(self):
        user = "I am exercising my core"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in body_responses])

    def test_back_training(self):
        user = "I've been training my back"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in body_responses])

    def test_not_body_part(self):
        user = "I train my dog"
        res = reply(user)
        self.assertNotIn(res, [r.format(X=reflect(user)) for r in body_responses])

    def test_plural_arms(self):
        user = "I workout my arms"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in body_responses])

    def test_plural_legs(self):
        user = "I exercise my legs"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in body_responses])

    def test_with_contraction(self):
        user = "I'm training my back"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in body_responses])

    def test_case_insensitivity(self):
        user = "i WORKOUT my CORE"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in body_responses])

    def test_sentence_context(self):
        user = "Today I am going to workout my arms"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in body_responses])

if __name__ == "__main__":
    unittest.main()
