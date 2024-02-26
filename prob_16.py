summed_digits = 0
for digit in str(2**1000):
	summed_digits += int(digit)

print(summed_digits)