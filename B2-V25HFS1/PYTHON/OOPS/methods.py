class methods:
    d=10
    def __init__(s,a,b,c):
        s.a=a
        s.b=b
        s.c=c
    def disp(s):    #instance method
        print(s.a,s.b,s.c)
    @classmethod
    def cmethod(cls):
        print(cls.d)
    @staticmethod
    def smethod():
        print(methods.d)
o1=methods(7,8,9)
o2=methods(1,2,3)
o1.disp()
o2.cmethod()
o1.smethod()
