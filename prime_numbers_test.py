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

    def test_returns_list(self):
        """
        The function returns an element of type list
        """
        self.assertEqual(isinstance(prime_generator(10)), isinstance(['1']))
    
    