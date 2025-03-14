# class method decorator

class Student:
    name = "Aniket" # class attribute

    @classmethod
    def ClassMethod(self, name):
        self.name = name

s1 = Student()
s1.ClassMethod("Aniket Chaudhari")
print(s1.name)
print(Student.name)

    