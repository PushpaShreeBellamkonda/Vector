from abc import *
class Vh(ABC):
    @abstractmethod
    def start(s):
        pass
    @abstractmethod
    def stop(s):
        pass
    @abstractmethod
    def run(s):
        pass
class car(Vh):
    def start(s):
        print("car started")
    def run(s):
        print("car is running")
    def tl(s):
        print("car turned left")
    def stop(s):
        print("car is stopped")
obj=car()
obj.start()
obj.run()
obj.tl()
obj.stop()

# example 2
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