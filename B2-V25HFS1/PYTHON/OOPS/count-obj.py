# count how many objects created for a given class
class A:
    c=0
    def __init__(s):
        A.c=A.c+1
    @staticmethod
    def disp():
        return A.c
o1=A()
o2=A()
o3=A()
o4=o1
print(A.disp())