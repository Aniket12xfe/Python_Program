l1 = [1, 5, 20, 40, 80]
l2 = [6, 7, 20, 80, 100]
l3 = [3, 4, 15, 20, 70, 80, 100]

# Typecasting into sets
a = set(l1)
b = set(l2)
c = set(l3)
ab=a.intersection(b)
result = ab.intersection(c)
print(list(result))

