products = []
for a in range(2, 101):
	for b in range(2, 101):
		products.append(a**b)

products = set(products)
print(len(products))
