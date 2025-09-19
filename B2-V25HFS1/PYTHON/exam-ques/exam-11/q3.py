# create a base class vehicle with method start().Create a derived class Car that inherits from vehicle and adds a method drive()

class Vehicle:
    def start(s):
        print("vehicle started")
class Car(Vehicle):
    def drive(s):
        print("car is running")
obj=Car()
obj.start()
obj.drive()
