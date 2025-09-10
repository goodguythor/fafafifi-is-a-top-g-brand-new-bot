import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply, reflect

duration_responses = [
    "{X}? That's a great time!",
    "Wow, {X}, at what pace do you run?"
]

class TestDuration(unittest.TestCase):

    def test_run_minutes(self):
        user = "I ran 30 minutes"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in duration_responses])

    def test_run_minutes_short(self):
        user = "I ran 30m"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in duration_responses])

    def test_walk_hour(self):
        user = "I'm walking 1 hour"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in duration_responses])

    def test_walk_hour_short(self):
        user = "I'm walking 1h"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in duration_responses])

    def test_cycle_decimal_hours(self):
        user = "I have cycled 2.5 hours"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in duration_responses])

    def test_cycle_decimal_hours_short(self):
        user = "I have cycled 2.5h"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in duration_responses])

    def test_running_minutes(self):
        user = "I am running 45 minutes"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in duration_responses])

    def test_running_minutes_short(self):
        user = "I am running 45m"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in duration_responses])

    def test_walked_hour(self):
        user = "I walked 2 hours"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in duration_responses])

    def test_walked_hour_short(self):
        user = "I walked 2h"
        res = reply(user)
        self.assertIn(res, [r.format(X=reflect(user)) for r in duration_responses])

    def test_no_duration(self):
        user = "I ran fast today"
        res = reply(user)
        self.assertNotIn(res, [r.format(X=reflect(user)) for r in duration_responses])

    def test_irrelevant_sentence(self):
        user = "I read a book for 1 hour"
        res = reply(user)
        self.assertNotIn(res, [r.format(X=reflect(user)) for r in duration_responses])


if __name__ == "__main__":
    unittest.main()