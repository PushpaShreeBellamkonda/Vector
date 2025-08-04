n=int(input())
l=list(map(int,input().split()))
pc=0
nc=0
zc=0
for i in l:
    if i>0:
        pc+=1
    elif i<0:
        nc+=1
    elif i==0:
        zc+=1
p=(pc/len(l))
n=(nc/len(l))
z=(zc/len(l))
print("%.6f"%(p))
print("%.6f"%(n))
print("%.6f"%(z))