# example for single,multilevel,heirarchical and hybrid inheritance
class person:
    def __init__(s,name,phno,place):
        s.name=name
        s.phno=phno
        s.place=place
    def disp(s):
        print(s.name,s.phno,s.place,end=" ")
class std(person):
    def __init__(s,name,phno,place,sid,dept):
        super().__init__(name,phno,place)
        s.sid=sid
        s.dept=dept
    def disp(s):
        super().disp()
        print(s.sid,s.dept,end=" ")
class result(std):
    def __init__(s,name,phno,place,sid,dept,marks):
        super().__init__(name,phno,place,sid,dept)
        s.marks=marks
    def disp(s):
        super().disp()
        print(s.marks)
class emp(person):
    def __init__(s,name,phno,place,eid):
        super().__init__(name,phno,place)
        s.eid=eid
    def disp(s):
        super().disp()
        print(s.eid)
class customer(person):
    def __init__(s,name,phno,place,cid):
        super().__init__(name,phno,place)
        s.cid=cid
    def disp(s):
        super().disp()
        print(s.cid)
std1=result("pushpa",6988576798,"hyd",101,"cse",99)
std1.disp()
e1=emp("Amar",7544434659,"chn",123)
e1.disp()
c1=customer("Nithin",7563670923,"bnglr",456)
c1.disp()
