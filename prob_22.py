file = open("0022_names.txt", "r")
names = file.read().split(",")
names = [i.replace('"', "") for i in names]
names.sort()

alpha_numberic = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 
'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18,
 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
def nameToNumber(name):
	summed_letters = 0

	for character in name:
		if character in alpha_numberic:
			summed_letters += alpha_numberic[character]

	return summed_letters

summed_names = 0
for name in names:
	summed_names += nameToNumber(name) * (names.index(name) + 1)
	print(name)

print(summed_names)