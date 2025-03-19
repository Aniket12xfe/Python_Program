# calculate percentage based on marks using decorator function property

class Student:
    def __init__(self, phy, math, chem):
        self._validate_marks(phy, math, chem)
        self.phy = phy
        self.math = math
        self.chem = chem
        self._percentage = 0
        self.calculate_percentage()
    
    def _validate_marks(self, phy, math, chem):
        for mark in (phy, math, chem):
            if not isinstance(mark, (int, float)) or mark < 0 or mark > 100:
                raise ValueError("Marks must be numbers between 0 and 100")
    
    def calculate_percentage(self):
        self.total = self.phy + self.math + self.chem
        self._percentage = (self.total / 300) * 100
    
    @property
    def percentage(self):
        return f"{self._percentage:.2f}%"
    
    @percentage.setter
    def percentage(self, value):
        self._percentage = value

def get_marks():
    try:
        phy = float(input("Enter Physics marks (0-100): "))
        math = float(input("Enter Math marks (0-100): "))
        chem = float(input("Enter Chemistry marks (0-100): "))
        return phy, math, chem
    except ValueError:
        print("Please enter valid numbers")
        return get_marks()

if __name__ == "__main__":
    try:
        phy, math, chem = get_marks()
        student = Student(phy, math, chem)
        print(f"\nTotal Percentage: {student.percentage}")
    except ValueError as e:
        print(f"Error: {e}")