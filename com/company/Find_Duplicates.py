def find_Duplicates(m):
    seen = set()
    duplicates = set()
    for i in m:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return list(duplicates)



my_list = [1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 5]
print(find_Duplicates(my_list))