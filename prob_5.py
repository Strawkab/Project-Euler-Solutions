
def numberFinder():
	dividend = 1
	divisors = [8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
	while True:
		for i in divisors:
			if dividend % i != 0:
				break
		else:
			return dividend

		dividend += 1
		print(dividend)
print(numberFinder())