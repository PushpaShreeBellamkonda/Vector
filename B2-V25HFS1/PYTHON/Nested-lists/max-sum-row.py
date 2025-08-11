r=int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
print(l)
s=0
r=l[0]
for i in l:
    t=sum(i)
    if t>s:
        s=t
        r=i
print(r)




