# Create a base class Shape and derive Circle,Rectangle,and Triangle classes from it.
# Each should implement their own area
from abc import *
class shape(ABC):
    def __init__(s,d1,d2=0):
        s.d1=d1
        s.d2=d2
    @abstractmethod
    def area(s):
        pass
class rec(shape):
    def area(s):
        print(s.d1*s.d2)
class cir(shape):
    def area(s):
        print(3.14*s.d1*s.d1)
class tra(shape):
    def area(s):
        print(0.5*s.d1*s.d2)
r=rec(5,8)
t=tra(8,6)
c=cir(5)
r.area()
t.area()
c.area()