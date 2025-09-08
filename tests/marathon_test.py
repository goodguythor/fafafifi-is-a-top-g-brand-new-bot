import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply, reflect

marathon_responses = [
    "Wow, {X}??? You're an endurance monster.",
    "{X}? That's incredible! How did you feel during the race?"
]

class TestMarathon(unittest.TestCase):

    def test_half_marathon_run(self):
        user = "I ran a half marathon yesterday"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in marathon_responses])

    def test_full_marathon_walk(self):
        user = "I walked a full marathon"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in marathon_responses])

    def test_marathon_cycle(self):
        user = "I'm cycling a marathon"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in marathon_responses])

    def test_plain_marathon(self):
        user = "I am running a marathon today"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in marathon_responses])

    def test_no_marathon(self):
        user = "I ran a long distance race"
        res = reply(user)
        self.assertNotIn(res, [r.format(X=reflect(user)) for r in marathon_responses])

if __name__ == "__main__":
    unittest.main()