def isTriangleNumber(integer):
	triangle = 1
	counter = 1
	while triangle < integer:
		counter += 1
		triangle = ((counter + 1) * counter) / 2
	
	if triangle == integer:
		return True
	else:
		return False

def wordToNumber(word):
	summed_letters = 0
	for character in word:
		summed_letters += ord(character) - 64 #ordinal to numerical place

	return summed_letters

file = open("0042_words.txt", "r")
list_of_words = file.read().split(",")
list_of_words = [i.replace('"', "") for i in list_of_words]
print(list_of_words)
triangle_words = []
for word in list_of_words:
	print(wordToNumber(word))
	if isTriangleNumber(wordToNumber(word)):
		triangle_words.append(word)

print(triangle_words)
print(len(triangle_words))
print(wordToNumber("a"))