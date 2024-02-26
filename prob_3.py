def isPrime(integer):
	if integer < 1:
		return -1
	if integer == 1:
		return False
	for i in range(2, integer):
		if integer % i == 0:
			return False
	return True

def primeDivider(dividend):
	if isPrime(dividend) == True:
		return int(dividend)
	for i in range(2, dividend):
		if dividend % i == 0:
			return int(i)

	return int(-1)

def primeFactorizer(integer):
	prime_factors = []

	while integer > primeDivider(integer):
		prime_factors.append(primeDivider(integer))
		integer = int(integer / primeDivider(integer))
		print(prime_factors)
		print(integer)

	prime_factors.append(integer)
	return prime_factors

print(primeFactorizer(600851475143))

