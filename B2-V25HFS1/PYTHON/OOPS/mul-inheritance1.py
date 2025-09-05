class A:
    def m1(s):
        print("m-1")
    def disp(s):
        print("class A")
class B:
    def m2(s):
        print("m-2")
    def disp(s):
        super().disp() #to inherit both parents features
        print("class B")
class C(B,A):
    pass
c=C()
c.disp()
c.m1()
c.m2()