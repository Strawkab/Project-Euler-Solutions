def isPrime(integer):
	if integer <= 1:
		return False
	for i in range(2, integer):
		if integer % i == 0:
			return False
	return True

def isTruncatablePrime(integer):
	copy = integer

	while copy > 0: #truncate from right
		if not isPrime(copy):
			return False
		copy //= 10

	while integer > 0: #truncate from left
		if not isPrime(integer):
			return False
		if integer < 10:
			break
		integer = int(str(integer)[1:])


	return True
truncatable_primes = []
counter = 11
while len(truncatable_primes) < 11:
	if isTruncatablePrime(counter):
		truncatable_primes.append(counter)
		print(truncatable_primes)
	counter += 2
	print(counter)

print(sum(truncatable_primes))
