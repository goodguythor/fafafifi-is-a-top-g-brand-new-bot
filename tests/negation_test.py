import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply, reflect

negation_responses = [
    "It's ok to not doing anything in a day, just take your time to recover and relax"
]

class TestNegation(unittest.TestCase):

    def test_simple_not(self):
        user = "I am not working out today"
        res = reply(user)
        self.assertIn(res, negation_responses)

    def test_dont_case(self):
        user = "I don't feel like exercising"
        res = reply(user)
        self.assertIn(res, negation_responses)

    def test_do_not_case(self):
        user = "I do not want to train my legs"
        res = reply(user)
        self.assertIn(res, negation_responses)

    def test_didnt_case(self):
        user = "I didn't run yesterday"
        res = reply(user)
        self.assertIn(res, negation_responses)

    def test_aint_case(self):
        user = "I'm tired so I ain't exercising"
        res = reply(user)
        self.assertIn(res, negation_responses)

    def test_no_negation(self):
        user = "I am running today"
        res = reply(user)
        self.assertNotIn(res, negation_responses)

if __name__ == "__main__":
    unittest.main()