counter = 1
spiral_digit = 1
while counter <= 500:
	for i in range(4):
		spiral_digit += counter * 2
		summed_digits += spiral_digit
		print(spiral_digit)
	counter += 1 

print(summed_digits)