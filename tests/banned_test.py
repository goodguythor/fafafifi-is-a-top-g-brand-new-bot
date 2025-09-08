import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bot import reply

banned_responses = [
    "My mom said that you can't use bad words if you want to go to the heaven 🥺",
    "Mom, I'm scared 🥺"
]

class TestBannedWords(unittest.TestCase):

    def test_f_word(self):
        res = reply("fuck you")
        self.assertIn(res, banned_responses)

    def test_uppercase_banned(self):
        res = reply("FUCK this")
        self.assertIn(res, banned_responses)

    def test_mixed_case_banned(self):
        res = reply("ShIt happens")
        self.assertIn(res, banned_responses)

    def test_bitch_word(self):
        res = reply("You bitch")
        self.assertIn(res, banned_responses)

    def test_ass_inside_word_not_banned(self):
        res = reply("This is a class example")
        self.assertNotIn(res, banned_responses)

    def test_retard_word(self):
        res = reply("You retard")
        self.assertIn(res, banned_responses)

    def test_multiple_banned_words(self):
        res = reply("fuck you bitch")
        self.assertIn(res, banned_responses)

    def test_banned_in_middle_sentence(self):
        res = reply("That was stupid of me")
        self.assertIn(res, banned_responses)

    def test_banned_with_punctuation(self):
        res = reply("fuck! this hurts")
        self.assertIn(res, banned_responses)

    def test_repeated_banned_words(self):
        res = reply("fuck fuck fuck")
        self.assertIn(res, banned_responses)

    def test_almost_swear_word(self):
        res = reply("Fuc bitc stup as retar")
        self.assertNotIn(res, banned_responses)

    def test_no_banned_words(self):
        res = reply("I am feeling strong today")
        self.assertNotIn(res, banned_responses)

if __name__ == "__main__":
    unittest.main()
