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

mydict = {
    "name" : "Aniket",
    "age" : 21,
    "gender" : "male",
    "subjects" : {
        "Math" : 90,
        "Physics" : 85,
        "Chemistry" : 88,
        "English" : 92,
        "Hindi" : 95
    }
}

print(mydict)

subject_scores = mydict["subjects"].values()
total_score = sum(subject_scores)
total_subjects = len(subject_scores)
print("Total marks of the student is", total_score)
print("Percentage of the student is", (total_score/total_subjects))
