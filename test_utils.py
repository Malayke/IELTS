import unittest
from utils import is_alpha_string, is_english_word, is_english_compound_word


class TestIsAlphaString(unittest.TestCase):
    def test_alpha_string(self):
        self.assertFalse(is_alpha_string("[keo(r)]"), "Error: '[keo(r)]' is not a valid English word")
        self.assertFalse(is_alpha_string("ab"), "Error: 'ab' is not a valid alpha string because it's length is less than 3")
        self.assertFalse(is_alpha_string("123"), "Error: '123' is not a valid English word")
        self.assertFalse(is_alpha_string(""), "Error: '' is not a valid English word because it's length is less than 3")
        self.assertFalse(is_alpha_string(" "), "Error: '' is not a valid English word because it's length is less than 3")
        # self.assertFalse(is_alpha_string("abc"), "Error: 'abc' is a not valid English word")
        self.assertFalse(is_alpha_string("aBc"), "Error: 'abc' is a not valid English word")
        self.assertFalse(is_alpha_string("Tt"), "Error: 'Tt' is a not valid English word")
        self.assertFalse(is_alpha_string("Tt AE JJ"), "Error: 'Tt AE JJ' is a not valid English word")
        self.assertFalse(is_alpha_string("AMAEXIH"), "Error: 'AMAEXIH' is a valid English word")
        self.assertTrue(is_alpha_string("carpet"), "True: 'carpet' is a valid English word")
        self.assertTrue(is_alpha_string("ATM"), "True: ATM is a valid English word")
        self.assertTrue(is_alpha_string("arrive at one's destination"), "True: 'arrive at one's destination' is a valid because it's a compound words")
        self.assertTrue(is_alpha_string("bad sheet"), "True: 'bad sheet' is a valid English word because it's a compound words")
        self.assertTrue(is_alpha_string("chemist's"), "True: 'chemist's' is a valid English word")
        self.assertTrue(is_alpha_string("academic English"), "True: academic English is a valid English word")
        self.assertTrue(is_alpha_string("a series of"), "True: academic English is a valid English word")
        self.assertTrue(is_alpha_string("a (great) variety of"), "True: a (great) variety of is a valid English word")
        self.assertTrue(is_alpha_string("Atlantic Ocean"), "True: 'Atlantic Ocean' is a valid English word")
        self.assertTrue(is_alpha_string("book in advance"), "True: 'book in advance' is a valid English word")
        self.assertTrue(is_alpha_string("face-to-face interview"), "True: 'face-to-face interview' is a valid English word")


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