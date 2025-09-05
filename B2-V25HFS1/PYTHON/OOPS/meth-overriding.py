# if both child class and parent class have same method names,then child class method
# overrides functionality of parent class
class A:
    def dis(s):
        print("A")
class B(A):
    def dis(s):
        print("B")
class C(A):
    def dis(s):
        print("C")
b=B()
b.dis()
c=C()
c.dis()