import unittest
from prime_numbers import generate_prime

class TestPrime(unittest.TestCase):
    """
    Tests that prime generator works correctly
    """

    def test_accepts_numbers_only(self):
        """
        The parameter given should be of type int
        """
        self.assertEqual(generate_prime('str'), 'Pass numbers only')

    def test_accepts_positive_numbers(self):
        """
        The function should work with positive numbers
        """
        self.assertEqual(generate_prime(10), [2, 3, 5, 7])
    
    def test_rejects_negative_values(self):
        """
        The function should reject prime numbers
        """
        self.assertEqual(generate_prime(-10), "Provide a positive number")

    def test_returns_list(self):
        """
        The function returns an element of type list
        """
        self.assertIsInstance(generate_prime(10), list)

    def test_rejects_list_arguments(self):
        """
        The function should reject arguments of type list
        """
        self.assertEqual(generate_prime([1, 2, 3]), 'Pass numbers only')
    
    def test_does_not_return_an_empty_list(self):
        """
        The function should return a list containing prime numbers given valid arguments
        """
        self.assertNotEqual(generate_prime(-10), [])

    def test_returns_list_of_correct_length(self):
        """
        The function should return a list of the correct length
        """
        self.assertEqual(len(generate_prime(5)), 3)

    def test_generates_empty_list_for_1(self):
        """
        The function should generate an empty list when given 1
        """
        self.assertEqual(generate_prime(1), [])

    def test_generates_list_with_2_only_when_called_with_2(self):
        """
        The function should return a list with 2 only when called with 2
        """
        self.assertEqual(generate_prime(2), [2])

    def test_generates_empty_list_given_0(self):
        """
        The function should return an empty list given 0 as the argument
        """
        self.assertEqual(generate_prime(0), [])