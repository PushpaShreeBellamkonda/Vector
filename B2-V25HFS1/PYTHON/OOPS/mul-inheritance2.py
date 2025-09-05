# initialising parent class constructor in multiple inheritance
class A:
    def __init__(s,a,b):
        s.a=a
        s.b=b
    def disp(s):
        print(s.a,s.b,end=" ")
        super().disp()  #to get both parents features to child
class B:
    def __init__(s,c,d):
        s.c=c
        s.d=d
    def disp(s):
        print(s.c,s.d,end=" ")
class C(A,B):
    def __init__(s,a,b,c,d,e):
        A.__init__(s,a,b)
        B.__init__(s,c,d)
        s.e=e
    def disp(s):
        super().disp()
        print(s.e)

c=C(1,2,3,4,5)
c.disp()