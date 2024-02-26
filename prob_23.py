def sumOfDivisors(integer):
	divisors = []
	
	for i in range(1, integer):
		if integer % i == 0:
			divisors.append(i)

	return sum(divisors)

def isAbundant(integer):
	if integer > sumOfDivisors(integer):
		return True
	else:
		return False

abundant_numbers = []
for i in range(28123):
	print(i)
	if isAbundant(i):
		abundant_numbers.append(i)

print(abundant_numbers)
def isSummedByAbundantNums(integer):
	1 + 1

