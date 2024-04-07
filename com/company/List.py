Fruits = ["Apple", "Banana", "Kiwi"]
print(Fruits)
print(type(Fruits))
print(len(Fruits))

if "Banana" in Fruits:
    print("Yes")

if "Mango" not in Fruits:
    print("Yes")
else:
    print("No")

print(Fruits[-3])


# Append element in last
Fruits.append("Water mellon")
print(Fruits)

# Adding element at particular index
Fruits.insert(2, "Small Banana")
print(Fruits)

#Mixing two list and make it one
List = ["Aniket", "Mitali"]
Fruits.extend(List)
print(Fruits)

#remove element
Fruits.remove("Aniket")

#remove item from index or else last item
Fruits.pop(2)
Fruits.pop()
print(Fruits)

#updating items in list
Fruits[1] = "cheery"

#updating items in list by using range
Fruits[2:3] = ["Kiwi", "Banana"]
print(Fruits)

#sorting of list
Fruits.sort()
print(Fruits)   # Ascending order
Fruits.sort(reverse=True)    # Descending order
print(Fruits)

Fruits.reverse()
print(Fruits)

#list Comprehension
# newline = [fruit for fruit in Fruits if "a" in fruit]
# print(newline)

#copy list
newline = Fruits.copy()
print(newline)

#Concatination
new_fruits = newline + Fruits
print(new_fruits)

Name = list("Aniket")
print(Name)
Name = list(["Aniket", "Om", "Bhavesh", "Ashwini"])
print(Name)