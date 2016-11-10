import primee

import unittest

class PrimeTestCase(unittest.TestCase):

#checks if the number is positive
	def test_numbers_less_than_one(self):
		self.assertEqual(primee.prime_checker(-1), "negative numbers are not prime")
#checks if number is equal to three
	def test_number_equal_to_two(self):
		self.assertEqual(primee.prime_checker(2), "n is prime")



if __name__ =="__main__":
	unittest.main()