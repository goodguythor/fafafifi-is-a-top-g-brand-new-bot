import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

rest_responses = [
    "Rest is just as important as training! Enjoy your recovery.",
    "Rest days help your muscles grow stronger. Take it easy!"
]

class TestRest(unittest.TestCase):

    def test_simple_rest(self):
        user = "I need rest"
        res = reply(user)
        self.assertIn(res, rest_responses)

    def test_rest_day(self):
        user = "Today is my rest day"
        res = reply(user)
        self.assertIn(res, rest_responses)

    def test_resting_now(self):
        user = "I'm resting after a hard workout"
        res = reply(user)
        self.assertIn(res, rest_responses)

    def test_my_rest_day(self):
        user = "My rest day is on Sunday"
        res = reply(user)
        self.assertIn(res, rest_responses)

    def test_non_rest_sentence(self):
        user = "I am working hard today"
        res = reply(user)
        self.assertNotIn(res, rest_responses)

    def test_rest_without_i_or_my(self):
        user = "Taking rest is important"  # should not match because no "I" or "my"
        res = reply(user)
        self.assertNotIn(res, rest_responses)

if __name__ == "__main__":
    unittest.main()