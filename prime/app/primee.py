def prime_checker(n):

	if n==2:
		return True
	if n<1:
		return False

	for m in range(2, int(n**0.5) + 1):
		if n%m == 0:  
			return False
	return True

#check for prime numbers between zero and n

prime = []
for m in range (100):
	if prime_checker(m):
		prime.append(m)

print(prime)







