import unittest
from utils import is_alpha_string, is_english_word, is_english_compound_word


class TestIsAlphaString(unittest.TestCase):
    def test_alpha_string(self):
        self.assertFalse(is_alpha_string("[keo(r)]"), "Error: '[keo(r)]' is not a valid alpha string")
        self.assertFalse(is_alpha_string("ab"), "Error: 'ab' is not a valid alpha string because it's length is less than 3")
        self.assertFalse(is_alpha_string("123"), "Error: '123' is not a valid alpha string")
        self.assertFalse(is_alpha_string(""), "Error: '' is not a valid alpha string because it's length is less than 3")
        self.assertFalse(is_alpha_string(" "), "Error: '' is not a valid alpha string because it's length is less than 3")
        self.assertTrue(is_alpha_string("abc"), "Error: 'abc' is a valid alpha string")
        self.assertFalse(is_alpha_string("aBc"), "Error: 'abc' is a not valid alpha string")
        self.assertTrue(is_alpha_string("carpet"), "Error: 'carpet' is a valid alpha string")
        self.assertTrue(is_alpha_string("bad sheet"), "True: 'bad sheet' is a valid alpha string because it's a compound words")
        self.assertTrue(is_alpha_string("chemist's"), "True: 'chemist's' is a valid alpha string")


# class TestIsEnglishWord(unittest.TestCase):
#     def test_is_english_word(self):
#         # 'hotline', 'powerpoint','reflectance','sunshield'
#         self.assertTrue(is_english_word('powerpoint'))
#         self.assertTrue(is_english_word('hotline'))
#         self.assertTrue(is_english_word('reflectance'))
#         self.assertTrue(is_english_word('sunshield'))
#         self.assertTrue(is_english_word('feedback'))
#         self.assertTrue(is_english_word('feedbacks'))
#         self.assertFalse(is_english_word('notaword'))
#         self.assertTrue(is_english_word("chemist's"))
#         self.assertFalse(is_english_word("[keo(r)]"))
#         self.assertFalse(is_english_word("abc"))
#         self.assertFalse(is_english_word(""))
#         self.assertFalse(is_english_word(" "))
#         self.assertTrue(is_english_compound_word("bad sheet"))
#         self.assertTrue(is_english_compound_word("bed ass"))

if __name__ == '__main__':
    unittest.main()