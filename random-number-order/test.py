import unittest
from main import random_number_order, random_number_order_simple

class TestRandomNumberOrder(unittest.TestCase):

    def test_random_number_order_simple(self):
        # Test for count = 10
        result = random_number_order_simple(10)

        # Ensure the list contains numbers from 1 to count
        self.assertEqual(sorted(result), list(range(1, 11)))
        
        # Ensure the list is of the correct length
        self.assertEqual(len(result), 10)
        
        # Ensure no duplicates in the result
        self.assertEqual(len(result), len(set(result)))

    def test_random_number_order(self):
        # Test for count = 10
        result = random_number_order(10)

        # Ensure the list contains numbers from 1 to count
        self.assertEqual(sorted(result), list(range(1, 11)))
        
        # Ensure the list is of the correct length
        self.assertEqual(len(result), 10)
        
        # Ensure no duplicates in the result
        self.assertEqual(len(result), len(set(result)))
    
    def test_random_number_order_edge_case(self):
        # Test for a small count (e.g., 1)
        result = random_number_order_simple(1)
        self.assertEqual(result, [1])

        result = random_number_order(1)
        self.assertEqual(result, [1])

if __name__ == "__main__":
    unittest.main()