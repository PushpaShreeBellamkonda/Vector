class prod:
    def __init__(s,name,desc,price,rating):
        s.name=name
        s.desc=desc
        s.price=price
        s.rating=rating
    def disp(s):
        print(s.name,s.desc,s.price,s.rating)
    def __lt__(s,o):
        return s.price<o.price
p1=prod("mbl1","ok",23000,3.5)
p2=prod("mbl2","ok",22000,3.3)
p3=prod("mbl3","ok",26000,3.9)
print(p1<p2)
print(p2<p3)

# overloading operator between two class objects
class A:
    def __init__(s,a):
        s.a=a
    def __add__(s,o):
        return A(s.a+o.x)
    def __str__(s):
        return str(s.a)
class B:
    def __init__(s,x):
        s.x=x
    def __add__(s,o):
        return A(s.x,o.a)
o1=A(5)
o2=B(7)
o3=o1+o2
print(o3)