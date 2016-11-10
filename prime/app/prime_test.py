import prime_checker
import unittest

class PrimeTestCase(unittest.TestCase):
	#check if number is two , hence prime
	def test_primes(self):
		self.assertTrue(prime_checker(2), "This is a prime number")
	#checks if numbe is composite
	def test_composites(self):
		self.assertFalse(prime_checker(4),"Number is composite, not prime" )
	#checks if number is negative
	def test_negative(self):
		self.assertFalse(prime_checker(-5),"Entrer a positive number")
	#checks for a zero type error.
	def test_zero(self):
		self.assertFalse(prime_checker(0), "Number is zero, not prime")
	#checks if number is one
	def test_one(self):
		self.assertFalse(prime_checker(1), "One is not a prime number.")






if __name__ =="__main__":
	unittest.main()