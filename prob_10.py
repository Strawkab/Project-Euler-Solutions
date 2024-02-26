def isPrime(integer):
	if integer <= 1:
		return False
	for i in range(2, integer):
		if integer % i == 0:
			return False
	return True

primes_sum = 0
for i in range(1, 2000000):
	print(i)
	if isPrime(i):
		primes_sum += i
print(primes_sum)