import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply, reflect

distance_responses = [
    "{X}? That's a great distance!",
    "Wow, {X}, at what pace do you run?"
]

class TestDistance(unittest.TestCase):

    def test_run_km(self):
        user = "I ran 5km"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in distance_responses])

    def test_walk_miles(self):
        user = "I walked 3 miles"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in distance_responses])

    def test_cycle_kilometers(self):
        user = "I am cycling 12 kilometers"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in distance_responses])

    def test_run_with_decimal(self):
        user = "I'm running 4.5 km today"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in distance_responses])

    def test_cycle_short(self):
        user = "I cycle 2 km"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in distance_responses])

    def test_uppercase_input(self):
        user = "I RAN 10 KM"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in distance_responses])

    def test_with_ive(self):
        user = "I've walked 7 miles"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in distance_responses])

    def test_no_distance_number(self):
        user = "I ran yesterday"
        res = reply(user)
        self.assertNotIn(res, [r.format(X=reflect(user)) for r in distance_responses])

    def test_no_unit(self):
        user = "I ran 10"
        res = reply(user)
        self.assertNotIn(res, [r.format(X=reflect(user)) for r in distance_responses])

    def test_other_activity(self):
        user = "I train my arms for 5 hours"
        res = reply(user)
        self.assertNotIn(res, [r.format(X=reflect(user)) for r in distance_responses])

if __name__ == "__main__":
    unittest.main()
