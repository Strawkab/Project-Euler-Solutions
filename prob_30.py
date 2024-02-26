def sumPowerDigit(base, exp):
	summed_digits = 0

	while base > 0:
		summed_digits += (base % 10)**exp
		base //= 10

	return summed_digits

counter = 1
while True:
	if counter == sumPowerDigit(counter, 5):
		print(counter)
	counter += 1

