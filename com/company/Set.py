names = {"Aniket", "Om", "Bhavesh", "Ashwini"}
print(names)
print(len(names))
print(type(names))

for x in names:
    print(x)


# For add Elements in set
names.add("Mitali")
print(names)

nm = ("Ann", "Poo")
names.update(nm)
print(names)

names.remove("Ann")
names.discard("Pan") # this function will not throw an error if value is not present in your set
print(names)

# Union function
s1 = {"A", "B", "C"}
s2 = {"c", "D", "E", "F"}
# Updating at end of s1
# s1.update(s2)
# print(s1)

s3 = s1.union(s2)
print(s3)

#keep only duplicates values
# s1.intersection_update(s2)
# print(s1)

# Keep only non-duplicates values
s1.symmetric_difference_update(s2)
print(s1)