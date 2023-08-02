import unittest
from utils import is_alpha_string


class TestIsAlphaString(unittest.TestCase):
    def test_alpha_string(self):
        self.assertFalse(is_alpha_string("[keo(r)]"), "Error: '[keo(r)]' is not a valid alpha string")
        self.assertFalse(is_alpha_string("ab"), "Error: 'ab' is not a valid alpha string because it's length is less than 3")
        self.assertFalse(is_alpha_string("123"), "Error: '123' is not a valid alpha string")
        self.assertFalse(is_alpha_string(""), "Error: '' is not a valid alpha string because it's length is less than 3")
        self.assertFalse(is_alpha_string(" "), "Error: '' is not a valid alpha string because it's length is less than 3")
        self.assertTrue(is_alpha_string("abc"), "Error: 'abc' is a valid alpha string")
        self.assertTrue(is_alpha_string("carpet"), "Error: 'carpet' is a valid alpha string")
        self.assertTrue(is_alpha_string("bad sheet"), "True: 'bad sheet' is a valid alpha string because it's a compound words")
        self.assertTrue(is_alpha_string("chemist's"), "True: 'chemist's' is a valid alpha string")


if __name__ == '__main__':
    unittest.main()