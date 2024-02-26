counter = 1
dividend = 1
while True:
	divisors = 0
	for divisor in range(1, int(dividend // 2)):
		if dividend % divisor == 0:
			divisors += 1
	if divisors * 2 >= 500:
		print(dividend, divisors)
		break
	else:
		counter += 1
		dividend += counter
	print(dividend, divisors)


