def factorsOf(integer):
	factors = []
	
	for i in range(1, integer + 1):
		if integer % i == 0:
			factors.append(i)

	return factors
def isPandigital(integer):
	factors = factorsOf(integer)
	for i in range(int(len(factors) / 2)):
		if ''.join(sorted(str(factors[i]) + str(factors[i * -1 -1]) + str(integer))) == "123456789":
			return True
	else:
		return False 
print(4396 + 5346 + 5796
+6952
+7254
+7632
+7852)
counter = 1
while True:
	if isPandigital(counter):
		print(counter)

	counter += 1