s=input()
o=list(s)
r=[]
for i in range(len(o)):
    r.insert(i,o.pop())
if r==list(s):
    print("yes")
else:
    print("No")

