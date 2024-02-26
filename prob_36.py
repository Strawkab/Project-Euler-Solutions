def isPalindrome(word):
	for i in range(len(word) // 2):
		if word[i] != word[-(i + 1)]:
			return False
	return True

def powersOfTwo(integer):
	powers = []
	counter = 0
	while 2**counter <= integer:
		powers.append(2**counter)
		counter += 1

	return powers

def binaryConverter(integer):
	binary_number = ""
	powers = powersOfTwo(integer)
	for i in range(1, len(powers) + 1):
		if powers[-i] <= integer:
			binary_number += "1"
			integer -= powers[-i]
		else:
			binary_number += "0"

	return binary_number
print(powersOfTwo(5))
print(binaryConverter(5))

summed_palindroms = 0
for i in range(1, 1000000):
	if isPalindrome(str(i)) and isPalindrome(str(binaryConverter(i))):
		summed_palindroms += i
		print(i, binaryConverter(i))

print(summed_palindroms)
