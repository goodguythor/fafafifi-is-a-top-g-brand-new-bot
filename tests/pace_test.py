import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

pace_responses = [
    "That's a great pace, keep up the good work!!!",
    "Wow, you could've been an athlete if you keep doing this consistently."
]

class TestPace(unittest.TestCase):

    def test_running_with_pace(self):
        user = "I run with a pace of 5"
        res = reply(user)
        self.assertIn(res, pace_responses)

    def test_running_decimal_pace(self):
        user = "My running pace is 6.3"
        res = reply(user)
        self.assertIn(res, pace_responses)

    def test_walking_with_pace(self):
        user = "I walk with a pace of 12"
        res = reply(user)
        self.assertIn(res, pace_responses)

    def test_cycling_with_pace(self):
        user = "I am cycling pace 3.5"
        res = reply(user)
        self.assertIn(res, pace_responses)

    def test_pace_without_number(self):
        user = "I have a good pace"
        res = reply(user)
        self.assertNotIn(res, pace_responses)

    def test_number_without_pace(self):
        user = "I ran 10 miles today"
        res = reply(user)
        self.assertNotIn(res, pace_responses)

if __name__ == "__main__":
    unittest.main()