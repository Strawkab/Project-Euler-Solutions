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

for i in range(10000):
	if i == sumOfDivisors(sumOfDivisors(i)):
		print(i)
		summed_ammicable_numbers += i 
print(summed_ammicable_numbers)
