import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

walk_responses = [
    "How long do you walk?",
    "Walking is a great way to refresh your mind."
]

class TestSimpleWalk(unittest.TestCase):

    def test_walk_base(self):
        user = "I walk every evening"
        res = reply(user)
        self.assertIn(res, walk_responses)

    def test_walking_ing(self):
        user = "I am walking to the park"
        res = reply(user)
        self.assertIn(res, walk_responses)

    def test_walked_past(self):
        user = "I walked yesterday morning"
        res = reply(user)
        self.assertIn(res, walk_responses)

    def test_walks_third_person(self):
        user = "My friend walks with me daily"
        res = reply(user)
        self.assertNotIn(res, walk_responses)

    def test_no_match(self):
        user = "I am running today"
        res = reply(user)
        self.assertNotIn(res, walk_responses)

if __name__ == "__main__":
    unittest.main()