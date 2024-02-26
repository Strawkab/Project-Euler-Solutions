import itertools

def sumOfDivisors(integer):
	divisors = []
	
	for i in range(1, integer):
		if integer % i == 0:
			divisors.append(i)

	return sum(divisors)

def areAmicableNumbers(a, b):
	if a != b and sumOfDivisors(a) == b and sumOfDivisors(b) == a:
		return True
	else:
		return False

summed_ammicable_numbers = 0
for a, b in itertools.combinations(range(10000), r=2):
	if areAmicableNumbers(a, b):
		summed_ammicable_numbers += a + b
		print(a, b)
	print(a, b)

print(summed_ammicable_numbers)
