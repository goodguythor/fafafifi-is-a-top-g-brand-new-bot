import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

run_responses = [
    "How long do you run?",
    "Running is a great way to clear your mind."
]

class TestSimpleRun(unittest.TestCase):

    def test_simple_run(self):
        user = "I run every morning"
        res = reply(user)
        self.assertIn(res, run_responses)

    def test_ran_past(self):
        user = "I ran yesterday"
        res = reply(user)
        self.assertIn(res, run_responses)

    def test_running_present(self):
        user = "I am running right now"
        res = reply(user)
        self.assertIn(res, run_responses)

    def test_ive_been_running(self):
        user = "I've been running daily"
        res = reply(user)
        self.assertIn(res, run_responses)

    def test_irrelevant_sentence(self):
        user = "I am walking to school"
        res = reply(user)
        self.assertNotIn(res, run_responses)

    def test_without_i(self):
        user = "Running is fun"  # should not match since no "I"
        res = reply(user)
        self.assertNotIn(res, run_responses)

if __name__ == "__main__":
    unittest.main()