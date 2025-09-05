# After defining the object,to get or to change properties of object,getter and setter methods are used
class emp:
    def __init__(s,eid,name,dept,sal):
        s.eid=eid
        s.name=name
        s.dept=dept
        s.sal=sal
    def disp(s):
        print(s.eid,s.name,s.dept,s.sal)
    def getid(s):
        return s.eid
    def getname(s):
        return s.name
    def getsal(s):
        return s.sal
    def setname(s,name):
        s.name=name
    def setdep(s,dept):
        s.dept=dept
    def setsal(s,sal):
        s.sal=sal
e1=emp(101,"Pushpa","Development",30000)
e2=emp(102,"Shree","Testing",30000)
e1.disp()
print(e1.getid())
print(e2.getsal())
e1.setsal(32000)
print(e1.getsal())
