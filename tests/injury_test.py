import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

injury_responses = [
    "You need to warm up before doing workout to avoid injury and wear a proper gear. If the injury isn't getting better soon, I suggest you to see a doctor ASAP!",
    "Ouch! Make sure to rest and recover. If it hurts a lot, maybe see a doctor."
]

class TestInjury(unittest.TestCase):

    def test_simple_hurt(self):
        user = "I am hurt"
        res = reply(user)
        self.assertIn(res, injury_responses)

    def test_hurting(self):
        user = "I'm hurting after my workout"
        res = reply(user)
        self.assertIn(res, injury_responses)

    def test_my_injury(self):
        user = "My injury is painful"
        res = reply(user)
        self.assertIn(res, injury_responses)

    def test_injured(self):
        user = "I've been injured during football"
        res = reply(user)
        self.assertIn(res, injury_responses)

    def test_injuries(self):
        user = "My injuries are getting worse"
        res = reply(user)
        self.assertIn(res, injury_responses)

    def test_not_injury_context(self):
        user = "This movie really hurts my brain"
        res = reply(user)
        self.assertNotIn(res, injury_responses)

if __name__ == "__main__":
    unittest.main()