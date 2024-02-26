def isPalindrome(word):
	for i in range(len(word) // 2):
		if word[i] != word[-(i + 1)]:
			return False
	return True

def palindromeFinder(): # inefficient since it doesnt account for redundancy 102 * 101 == 101 * 102
	palindromes = []
	for x in range(100, 1000):
		for y in range(100, 1000):
			if isPalindrome(str(x * y)):
				palindromes.append(x * y)
				print(palindromes)

	return palindromes

print(max(palindromeFinder()))