class Circle:
    def __init__(self, redius):
        self.redius = redius

    def area(self):
        return (22/7) * (self.redius ** 2)

    def perimeter(self):
        return 2 * (22/7) * self.redius

    def showPerimeter(self):
        print("Perimeter of circle is:",self.perimeter())

    def showArea(self):
        print("Area of circle is:",self.area())

c1 = Circle(21)
c1.showArea()
c1.showPerimeter()

