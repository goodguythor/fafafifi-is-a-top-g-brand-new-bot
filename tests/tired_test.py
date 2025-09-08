import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

tired_responses = [
    "Remember, progress is made one step at a time. You got this!",
    "Everyone feels tired sometimes. Just keep moving forward!"
]

class TestTired(unittest.TestCase):

    def test_simple_tired(self):
        user = "I am tired"
        res = reply(user)
        self.assertIn(res, tired_responses)

    def test_simple_lazy(self):
        user = "I'm lazy today"
        res = reply(user)
        self.assertIn(res, tired_responses)

    def test_my_tired_body(self):
        user = "My body is tired"
        res = reply(user)
        self.assertIn(res, tired_responses)

    def test_abbreviation(self):
        user = "I've been tired lately"
        res = reply(user)
        self.assertIn(res, tired_responses)

    def test_negative_case(self):
        user = "I am very energetic today"
        res = reply(user)
        self.assertNotIn(res, tired_responses)

if __name__ == "__main__":
    unittest.main()