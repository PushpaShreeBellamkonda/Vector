# Create a class Bird with method fly().Create a subclass Penguinthat overrides fly()
# to print "Penguins cant fly"

class Bird:
    def fly(s):
        print("Birds can fly")
class penguin(Bird):
    def fly(s):
        print("Penguins cant fly")
obj=penguin()
obj.fly()