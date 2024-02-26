def champernowneDigit(integer): #returns integer digit of champernowne's constant 
	champer_constant = "1"
	counter = 2

	while len(champer_constant) < integer:
		champer_constant += str(counter)
		counter += 1

	return int(champer_constant[integer - 1])


def champernowneDigitss(integers): 
	champer_constant = "1"
	counter = 2
	champer_digits = []
	for i in integers:
		while len(champer_constant) < i:
			champer_constant += str(counter)
			counter += 1
			print(counter)
		champer_digits.append(int(champer_constant[i - 1]))

	return champer_digits

product = 1
for i in champernowneDigitss([1, 10, 100, 1000, 10000, 100000, 1000000]):
	product *= i
print(product)