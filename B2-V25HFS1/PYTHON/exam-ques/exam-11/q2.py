# write a class rectangle with with length , width as data members,Initialise them using 
# a constructor and add a method to calculate area

class Rectangle:
    def __init__(s,l,w):
        s.l=l
        s.w=w
    def area(s):
        print(s.l*s.w)
obj1=Rectangle(4,5)
obj1.area()