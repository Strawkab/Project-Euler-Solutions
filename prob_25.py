fib1 = 1
fib2 = 1
placeholder = 0
counter = 2
while fib2 <= 10**999:
	placeholder = fib2
	fib2 += fib1
	fib1 = placeholder
	counter += 1
	print(fib2)

print(counter)