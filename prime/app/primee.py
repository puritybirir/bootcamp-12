def prime_checker(n):
	if n==2:
		return True
	if n<1:
		return False

	for m in range(2, int(n**0.5) + 1):
		if n%m == 0:  
			return False
	return True

print(prime_checker(9))
