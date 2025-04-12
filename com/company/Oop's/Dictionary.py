# dict = {"name":"Aniket", "age":21, "gender":"male"}
# print(dict)

# dict["age"] = 23
# dict["city"] = "Pune"
# print(dict)

# arr = [1, 2, 3, "Aniket", "Pune", "Male"]
# arr.append(23)
# print(arr)

# arr.pop()
# print(arr)

# arr.remove('Aniket')
# print(arr)

# arr.clear()
# print(arr)

# info = {
#     "key" : "value",
#     "college" : "Sinhgad",
#     "name" : "Aniket",
#     "age" : 21,
#     "gender" : "male",
#     "is_Adult" : True,
#     "sem_sgpa" : [9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8],
#     "is_pass" : True,
#     "CGPA" : 9.8,
#     "cgpaToMarks": 78.4
# }

# print(info)

# mydict = {
#     "name" : "Aniket",
#     "age" : 21,
#     "gender" : "male",
#     "subjects" : {
#         "Math" : 90,
#         "Physics" : 85,
#         "Chemistry" : 88,
#         "English" : 92,
#         "Hindi" : 95
#     }
# }
#
# print(mydict)
#
# subject_scores = mydict["subjects"].values()
# total_score = sum(subject_scores)
# total_subjects = len(subject_scores)
# print("Total marks of the student is", total_score)
# print("Percentage of the student is", (total_score/total_subjects))

dic = {
    "Name": "Chaudhari God",
    "marks" : 333,
    "Neha" : 356
}
# print(type(dic))
# print(dic["Neha"])
# print(dic.keys())
# print(dic.values())
#
# for i in dic.keys():
#     print(dic[i])
# for i in dic.keys():
#     print(f"the value corresponding to {i} is {dic[i]}")


ep1 = {
    122 : 85,
    123 : 45,
    145 : 69,
    650 : 90,
}

ep2 = {
    222 : 56,
    566 : 90
}

# ep1.update(ep2)
# ep1.pop(122)
# ep1.popitem()
# del ep1
# del ep1[122]
print(ep1)