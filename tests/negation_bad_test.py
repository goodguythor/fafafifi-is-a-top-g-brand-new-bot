import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

neg_neg_responses = [
    "That's nice, keep going and you will see the result!!!"
]

class TestNegationNegative(unittest.TestCase):

    def test_not_tired(self):
        user = "I am not tired"
        res = reply(user)
        self.assertIn(res, neg_neg_responses)

    def test_not_lazy(self):
        user = "I'm not lazy today"
        res = reply(user)
        self.assertIn(res, neg_neg_responses)

    def test_dont_feel_bad(self):
        user = "I don't feel bad after workout"
        res = reply(user)
        self.assertIn(res, neg_neg_responses)

    def test_did_not_hurt(self):
        user = "My legs did not hurt after running"
        res = reply(user)
        self.assertIn(res, neg_neg_responses)

    def test_aint_injured(self):
        user = "I ain't injured anymore"
        res = reply(user)
        self.assertIn(res, neg_neg_responses)

    def test_negative_without_negation(self):
        user = "I am tired"
        res = reply(user)
        self.assertNotIn(res, neg_neg_responses)

    def test_neutral_sentence(self):
        user = "I feel strong today" 
        res = reply(user)
        self.assertNotIn(res, neg_neg_responses)


if __name__ == "__main__":
    unittest.main()