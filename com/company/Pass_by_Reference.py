def printList(lst):
    lst.append(4)
    print("Inside function: ", lst)

lst = [1,2,3]
printList(lst)
print("Outside function: ", lst)