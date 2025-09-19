# Create a base class Employee and derived class Manager.Use super() to initialise base class
# attributes inside Manager

class Employee:
    def __init__(s,eid,phno,sal):
        s.eid=eid
        s.phno=phno
        s.sal=sal
    def disp(s):
        print(s.eid,s.phno,s.sal,end=" ")
class Manager(Employee):
    def __init__(s,eid,phno,sal,dept):
        super().__init__(eid,phno,sal)
        s.dept=dept
    def disp(s):
        super().disp()
        print(s.dept)
e1=Manager(101,3654092,30000,"Testing")
e1.disp()