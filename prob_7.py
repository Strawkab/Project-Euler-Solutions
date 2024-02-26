def isPrime(integer):
	if integer < 1:
		return -1
	if integer == 1:
		return False
	for i in range(2, integer):
		if integer % i == 0:
			return False
	return True

primes = []
number = 2
while len(primes) < 10001:
	if isPrime(number):
		primes.append(number)
		print(len(primes))
	number += 1

print(primes[-1])
