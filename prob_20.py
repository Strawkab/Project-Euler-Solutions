def digitSum(integer):
	summed_digits = 0

	while integer > 0:
		last_digit = integer % 10
		summed_digits += last_digit
		integer //= 10 

	return summed_digits

def factorial(integer):
	product = 1

	for i in range(1, integer + 1):
		product *= i

	return product

print(digitSum(factorial(100)))