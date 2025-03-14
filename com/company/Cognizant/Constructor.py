class studnet():
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display(self):
        print(self.name, self.age, self.roll_no)

s1 = studnet("John", 20, 123456)
s1.display()

s2 = studnet("Doe", 21, 123457)
s2.display()

s3 = studnet("Jane", 22, 123458)
s3.display()



import array
arr = array.array('i', [1, 2, 3, 4, 5])
for i in arr:
    print(i, end=" ")
arr = array.array('i',['1', '2', 'String'])
arr = ['1', '2', 'String']
for i in arr:
    print(i, end=" ")