# define a class Animal with method speak().Create a subclass Dog that
#  overrides speak() method

class Animal:
    def speak(s):
        print("Animal is speaking")
class Dog(Animal):
    def speak(s):
        print("Dog is barking")
obj=Dog()
obj.speak()
