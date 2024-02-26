def sumOfSquares(integer):
	sum_of_squares = 0
	
	for i in range(integer + 1):
		sum_of_squares += i*i

	return sum_of_squares

def squareOfSums(integer):
	sum_of_numbers = 0
	for i in range(integer + 1):
		sum_of_numbers += i

	return sum_of_numbers * sum_of_numbers

print(squareOfSums(100) - sumOfSquares(100))