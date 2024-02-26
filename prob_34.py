def factorial(integer):
	factorial = 1
	for i in range(1, integer + 1):
		factorial *= i

	return factorial

def isCurious(integer):
	sum_of_factorial = 0
	copy_integer = integer
	while integer > 0:
		sum_of_factorial += factorial(integer % 10)
		integer //= 10

	if copy_integer == sum_of_factorial:
		return True
	else:
		return False

counter = 1
while True:
	if isCurious(counter):
		print(counter)
	counter += 1
