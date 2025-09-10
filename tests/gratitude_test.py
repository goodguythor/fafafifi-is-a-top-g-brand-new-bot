import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

gratitude_responses = [
    "You're welcome",
    "My pleasure"
]

class TestGratitude(unittest.TestCase):

    def test_thanks(self):
        user = "thanks"
        res = reply(user)
        self.assertIn(res, gratitude_responses)

    def test_thank_you(self):
        user = "thank you so much"
        res = reply(user)
        self.assertIn(res, gratitude_responses)

    def test_ty(self):
        user = "ty"
        res = reply(user)
        self.assertIn(res, gratitude_responses)

    def test_caps(self):
        user = "THANKS"
        res = reply(user)
        self.assertIn(res, gratitude_responses)

    def test_no_gratitude(self):
        user = "hello friend"
        res = reply(user)
        self.assertNotIn(res, gratitude_responses)

if __name__ == "__main__":
    unittest.main()