from array import array
import unittest
from main import two_sum

class TestTwoSum(unittest.TestCase):

    def test_pair_found(self):
        numbers = array('i', [2, 7, 11, 15])
        target = 9
        result = two_sum(numbers, target)
        self.assertEqual(result, [2, 7])

    def test_no_pair_found(self):
        numbers = array('i', [1, 2, 3, 4])
        target = 10
        result = two_sum(numbers, target)
        self.assertEqual(result, [])

    def test_multiple_pairs(self):
        numbers = array('i', [3, 2, 4, 7])
        target = 6
        result = two_sum(numbers, target)
        self.assertEqual(result, [2, 4])

    def test_empty_list(self):
        numbers = array('i', [])
        target = 9
        result = two_sum(numbers, target)
        self.assertEqual(result, [])

    def test_single_element(self):
        numbers = array('i', [5])
        target = 5
        result = two_sum(numbers, target)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()