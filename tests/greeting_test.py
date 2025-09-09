import unittest
import sys
import os
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

greeting_responses = [
    "Haiii",
    "Yooo, how are you today?"
]

class TestGreeting(unittest.TestCase):

    def test_hi(self):
        user = "hi"
        res = reply(user)
        self.assertIn(res, greeting_responses)

    def test_hello(self):
        user = "hello"
        res = reply(user)
        self.assertIn(res, greeting_responses)

    def test_hey(self):
        user = "hey there"
        res = reply(user)
        self.assertIn(res, greeting_responses)

    def test_hai(self):
        user = "haiii"
        res = reply(user)
        self.assertIn(res, greeting_responses)

    def test_yo(self):
        user = "yo bro"
        res = reply(user)
        self.assertIn(res, greeting_responses)

    def test_not_greeting(self):
        user = "good night"
        res = reply(user)
        self.assertNotIn(res, greeting_responses)

if __name__ == "__main__":
    unittest.main()