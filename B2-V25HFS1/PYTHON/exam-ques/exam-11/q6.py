# create three classes:LivingBeing,Animal,and Dog where each class inherits from 
# the previous one.Add methods like is_alive(),breathe(),bark()

class LivingBeing:
    def is_alive(s):
        print("Living beings are alive")
class Animal(LivingBeing):
    def breathe(s):
        super().is_alive()
        print("Animal is breathing")
class Dog(Animal):
    def bark(s):
        super().breathe()
        print("Dog is barking")
d=Dog()
d.bark()