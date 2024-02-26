def collatz(integer):
	chain_length = 1
	while integer > 1:
		if integer % 2 == 0:
			integer /= 2
		else:
			integer = integer * 3 + 1
		chain_length += 1
	return chain_length

longest_chain = 0
starting_number = 0
for i in range(1, 1000000):
	print(i)
	length = collatz(i)
	if length > longest_chain:
		longest_chain = length
		starting_number = i
		print(starting_number, longest_chain)
print(starting_number)