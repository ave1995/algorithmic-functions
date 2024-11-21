import unittest
from main import most_frequent_ascii_char

class TestMostFrequentAsciiChar(unittest.TestCase):

    def test_single_char(self):
        input_string = "aaaaa"
        char, freq = most_frequent_ascii_char(input_string)
        self.assertEqual(char, 'a')
        self.assertEqual(freq, 5)

    def test_multiple_chars(self):
        input_string = "aaaabbaacccccc"
        char, freq = most_frequent_ascii_char(input_string)
        self.assertEqual(char, 'a')
        self.assertEqual(freq, 6)

    def test_empty_string(self):
        input_string = ""
        char, freq = most_frequent_ascii_char(input_string)
        self.assertEqual(char, None)
        self.assertEqual(freq, 0)

    def test_non_ascii_characters(self):
        input_string = "abcüxyz"
        char, freq = most_frequent_ascii_char(input_string)
        self.assertEqual(char, 'a')
        self.assertEqual(freq, 1)  # 'ü' should be ignored as it is non-ASCII

    def test_multiple_same_frequency(self):
        input_string = "abcabc"
        char, freq = most_frequent_ascii_char(input_string)
        self.assertIn(char, ['a', 'b', 'c'])  # Any of 'a', 'b', or 'c' is fine
        self.assertEqual(freq, 2)

    def test_mixed_case(self):
        input_string = "aAaAaa"
        char, freq = most_frequent_ascii_char(input_string)
        self.assertEqual(char, 'a')
        self.assertEqual(freq, 4)

    def test_special_characters(self):
        input_string = "@!$@!$"
        char, freq = most_frequent_ascii_char(input_string)
        self.assertEqual(char, '@')
        self.assertEqual(freq, 2)

if __name__ == "__main__":
    unittest.main()
