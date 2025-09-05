# same method with diff no.of args or diff type of args
class A:
    def disp(s,a,b=0,c=0):
        print(a,b,c)
o=A()
o.disp(5)
o.disp(7,"hii")
o.disp(3,4)
o.disp(3,4,5)