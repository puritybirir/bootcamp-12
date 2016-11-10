def prime_checker(n):

	if n==2:
		return True
	if n<=1:
		return False

	for m in range(2, int(n**0.5) + 1):
		if n%m == 0:  
			return False
	return True

#check for prime numbers between zero and n

def generate_primes(n):
	prime = []
	for i in range (1,n+1):
		if prime_checker(i):
			prime.append(i)
			return primes







