import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

cycling_responses = [
    "How long do you cycle?",
    "Cycling is fun."
]

class TestSimpleCycling(unittest.TestCase):

    def test_basic_cycling(self):
        user = "I am cycling today"
        res = reply(user)
        self.assertIn(res, cycling_responses)

    def test_cycled_past(self):
        user = "I cycled yesterday"
        res = reply(user)
        self.assertIn(res, cycling_responses)

    def test_cycle_singular(self):
        user = "I cycle every morning"
        res = reply(user)
        self.assertIn(res, cycling_responses)

    def test_cycles_plural(self):
        user = "I am someone who cycles a lot"
        res = reply(user)
        self.assertIn(res, cycling_responses)

    def test_not_cycling(self):
        user = "I am running today"
        res = reply(user)
        self.assertNotIn(res, cycling_responses)

if __name__ == "__main__":
    unittest.main()