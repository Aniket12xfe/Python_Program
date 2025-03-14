# Super method used for calling parent class methods.

class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car stopped")

class Bmw(Car):
    def __init__(self, type, name):
        super().__init__(type)
        self.name = name
        super().start()
    
obj = Bmw("SUV", "BMW")
obj.stop()
#static method call from class
Bmw.start()
print(obj.name)
print(obj.type)
        