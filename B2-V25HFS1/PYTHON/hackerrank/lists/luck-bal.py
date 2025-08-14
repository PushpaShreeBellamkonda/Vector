n,k=map(int,input().split())
l1=[]
t1=[]
for i in range(n):
    l,t=map(int,input().split())
    l1.append(l)
    t1.append(t)
print(l1)
print(t1)
l1.sort()
print(l1)
ones=t1.count(1)
print(ones)
diff=abs(k-ones)
print(diff)
s=0
for i in range(diff):
    s=s+l1[i]
print(s)
ts=0
for i in l1:
    ts+=i
print(ts-s)
    