dic = {"Aniket": 4101008,
       "Ashwini": 4101006,
       "Om": 4101015,
       "Mitali": 4101007,
       "Bhavesh": 4101002
       }
print(dic)
print(type(dic))
print(len(dic))

# Access the items in dic
print(dic["Mitali"])
print(dic.get("Aniket"))
print(dic.keys())

# updating values in dic
# dic["Aniket"] = 4101008
# print(dic)

# add item in dic.
dic["Aniket Chaudhari"] = 4101008
print(dic)

# update form another dic.
# dic1 = {"Aniket": 8
#         }
# dic.update(dic1)
# print(dic)

# remove the item
# dic.pop("Aniket Chaudhari")
# print(dic)
dic.popitem()       # last item removed
print(dic)

# Checking item in dic.
for items in dic:       # printing with keys only
    print(items, end=" ")
print()

for x in dic:           # printing with values only
    print(dic[x], end=" ")
print()

for x in dic.items():    # printing with key value pair
    print(x, end=" ")
print()

for x,y in dic.items():    # printing with key value pair differently
    print(x,y, end=" ")
print()

# nested dictionary
dict1 = {
    "Family":{
        "Aniket": 8999175577,
        "Vaishnavi": 9420103801,
        "Rajendra": 9665247377},
               "Friends" :{
                   "Ashwini": 4101006,
                    "Om": 4101015,
                    "Mitali": 4101007,
                    "Bhavesh": 4101002
                    }
               }
print(dict1)

# Zip function to add to datatypes in dictionary
s1 = "abc"
s2 = "def"
s3 = dict(zip(s1, s2))
print(s3)