import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

great_responses = [
    "That's nice, hope that feelings stay with you for a long time"
]

class TestGreatFeeling(unittest.TestCase):

    def test_simple_good(self):
        user = "I am good"
        res = reply(user)
        self.assertIn(res, great_responses)

    def test_simple_great(self):
        user = "I'm great"
        res = reply(user)
        self.assertIn(res, great_responses)

    def test_simple_happy(self):
        user = "I'm happy"
        res = reply(user)
        self.assertIn(res, great_responses)

    def test_my_great_day(self):
        user = "My day is great"
        res = reply(user)
        self.assertIn(res, great_responses)

    def test_feeling_good_today(self):
        user = "I’ve been feeling good today"
        res = reply(user)
        self.assertIn(res, great_responses)

    def test_non_great_context(self):
        user = "This weather is great"
        res = reply(user)
        self.assertNotIn(res, great_responses) 

    def test_tricky_case(self):
        user = "I'm not that good at math"
        res = reply(user)
        self.assertNotIn(res, great_responses) 

if __name__ == "__main__":
    unittest.main()
