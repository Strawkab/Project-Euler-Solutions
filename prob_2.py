fib1 = 0
fib2 = 1
temp_num = 0
sum_of_fib = 0 
while fib2 < 4000000:
	if fib2 % 2 == 0:
		sum_of_fib += fib2
	temp_num = fib2
	fib2 += fib1
	fib1 = temp_num

print(sum_of_fib)
