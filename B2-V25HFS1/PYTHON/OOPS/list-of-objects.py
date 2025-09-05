class std:
    def __init__(s,sid,name,dept,s1,s2,s3,s4):
        s.sid=sid
        s.name=name
        s.dept=dept
        s.s1=s1
        s.s2=s2
        s.s3=s3
        s.s4=s4
    def gettotal(s):
        return s.s1+s.s2+s.s3+s.s4
    def getper(s):
        return "{:.2f}".format(s.gettotal()/4)
    def __str__(s):
        return f"{s.sid} {s.name} {s.dept} {s.s1} {s.s2} {s.s3} {s.s4} {s.gettotal()} {s.getper()}"
f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/OOPS/std.txt","r")
stdobj=[]
l=f.readlines()
for data in l:
    x=data.strip().split()
    stdobj.append(std(int(x[0]),x[1],x[2],int(x[3]),int(x[4]),int(x[5]),int(x[6])))
for obj in stdobj:
    print(obj)
print()
stdobj.sort(reverse=True,key=lambda obj:obj.getper())
for obj in stdobj:
    print(obj)