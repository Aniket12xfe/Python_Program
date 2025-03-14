class A:
    var1 = "Welocome to class A"

class B:
    var2 = "Welcome to class B"

class C(A, B):
    var3 = "Welcome to class C"

obj = C()
print(obj.var3)
print(obj.var2)
print(obj.var1)