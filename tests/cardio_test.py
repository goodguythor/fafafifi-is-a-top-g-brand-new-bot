import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

cardio_responses = [
    "That's great, what kind of cardio did you just have?",
    "Cardio is awesome for your heart! Was it running, cycling, or something else?"
]

class TestCardio(unittest.TestCase):

    def test_simple_cardio(self):
        user = "I did cardio"
        res = reply(user)
        self.assertIn(res, cardio_responses)

    def test_cardio_with_am(self):
        user = "I am doing cardio"
        res = reply(user)
        self.assertIn(res, cardio_responses)

    def test_cardio_with_contraction(self):
        user = "I'm doing cardio today"
        res = reply(user)
        self.assertIn(res, cardio_responses)

    def test_cardio_in_sentence(self):
        user = "Today I am going to do some cardio at the gym"
        res = reply(user)
        self.assertIn(res, cardio_responses)

    def test_cardio_caps(self):
        user = "I AM DOING CARDIO"
        res = reply(user)
        self.assertIn(res, cardio_responses)

    def test_cardio_with_ive(self):
        user = "I've just finished cardio"
        res = reply(user)
        self.assertIn(res, cardio_responses)

    def test_cardio_with_noise(self):
        user = "Umm I am kinda tired but I did some cardio earlier"
        res = reply(user)
        self.assertIn(res, cardio_responses)

    def test_no_cardio_arm_training(self):
        user = "I am going to train my arms"
        res = reply(user)
        self.assertNotIn(res, cardio_responses)

    def test_no_cardio_general_statement(self):
        user = "Cardio is hard for everyone"
        res = reply(user)
        self.assertNotIn(res, cardio_responses)

    def test_no_i_pronoun(self):
        user = "Doing cardio is fun"
        res = reply(user)
        self.assertNotIn(res, cardio_responses)

if __name__ == "__main__":
    unittest.main()
