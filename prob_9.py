import math

for a in range (334, 999):
	for b in range(1000 - a):
		c = 1000 - a - b
		if a**2 + b**2 == c**2:
			print(a, b, c)



