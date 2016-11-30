import unittest

class TestPrime(unittest.TestCase):
    """
    Tests that prime generator works correctly
    """

    def test_accepts_numbers(self):
        """
        The parameter given should be of type int
        """
        self.assertEqual(prime_generator('str'), 'Please pass numbers only')

    def test_accepts_positive_numbers(self):
        """
        The function should work with positive numbers
        """
        self.assertEqual(prime_generator(10), ['2', '3', '5', '7'])
    
    def test_rejects_negative_values(self):
        """
        The function should reject prime numbers
        """
        self.assertEqual(generate_prime(-10), "Please provide a positive value for an angument")

    def test_rejects_numbers_less_than_1(self):
        """
        The function should reject numbers less than 1
        """
        self.assertEqual(generate_prime(0.8), "Please privide a number greater than or equal to 1")

    def test_returns_list(self):
        """
        The function returns an element of type list
        """
        self.assertEqual(isinstance(prime_generator(10)), isinstance(['1']))
    
