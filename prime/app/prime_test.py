from primee import prime_checker
import unittest

class PrimeTestCase(unittest.TestCase):
	#check if number is two , hence prime
	def test_primes(self):
		self.assertTrue(prime_checker(2), "This is a prime number")
	#checks if number is negative
	def test_negative(self):
		self.assertFalse(prime_checker(-5),"Entrer a positive number")
	#checks for a zero type error.
	def test_zero(self):
		self.assertFalse(prime_checker(0), "Number is zero, not prime")
	#checks if number is one
	def test_one(self):
		self.assertFalse(prime_checker(1), "One is not a prime number.")
	#checks if number is two, a prime number
	def test_two(self):
		self.assertTrue(prime_checker(2), "Two is a prime number")
	#checks if number is even, hence not prime
	def test_if_number_is_even(self):
		self.assertFalse(prime_checker(4), "Number is not prime")
	#checks if number is divivsible by 3
	def test_if_number_is_divisible_by_3(self):
		self.assertFalse (prime_checker(6), "Not a prime number")
	#checks if number is divisible by 5
	def test_if_number_i_divisible_by_5(self):
		self.assertFalse(prime_checker(15), "Not a prime number")
	#checks if number is divisible by 7
	def test_if_number_is_divisible_by_7(self):
		self.assertTrue(prime_checker(7), "seven is a prime number")
	#checks if numbe is composite
	def test_composites(self):
		self.assertFalse(prime_checker(4),"Number is composite, not prime" )
	
	





if __name__ =="__main__":
	unittest.main()