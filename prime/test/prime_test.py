import primee

import unittest

class PrimeTestCase(unittest.TestCase):

	def _test_numbers_less_than_one(self):
		self.assertEqual(primee.prime_checker(-1), "Number is less than one")
	def _test_number_equal_to_two(self):
		self.assertEqual(primee.prime_checker(2), "Number is prime")



