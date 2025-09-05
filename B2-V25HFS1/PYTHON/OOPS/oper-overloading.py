# providing additional functionality to the existing operator
class A:
    def __init__(s,a,b):
        s.a=a
        s.b=b
    def disp(s):
        print(s.a,s.b)
    def __add__(s,o):
        return A(s.a+s.b,o.a+o.b)
o=A(4,5)
o1=A(8,7)
o2=o+o1
o2.disp()