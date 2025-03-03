# class Student:
#     name = "Aniket Chaudhari"
#
# s1 = Student()
# print(s1)
# print(s1.name)

class Student:
    # Default constructor
    # def __int__(self):
    #     pass

    college_name = "Sinhgad Institute of Technology and Science Narhe"
    # name = ""   # class attribute

    # Parameterize constructor
    def __init__(self, fullname, marks):
        self.name = fullname
        self.marks = marks   # obj attribute > class attribute
        # print("Student full name adding into database..")

    @staticmethod
    def hello():
        print("Hello Aniket")

    def PassOrFail(self):
        if self.marks < 27:
            print("Student is Fail,",self.name)
        else:
            print("Student is pass,",self.name)


s1 = Student("Aniket Chaudhuri", 26)

print("Student Name is",s1.name)
print("Student Marks in Maths is",s1.marks)
print("Student College Name is",s1.college_name)
s1.PassOrFail()

print(" ")

s2 = Student("Ashwini Bhide", 99)
print("Student Name is",s2.name)
print("Student Marks in Maths is",s2.marks)
print("Student College Name is",s2.college_name)
s2.PassOrFail()
s2.hello()