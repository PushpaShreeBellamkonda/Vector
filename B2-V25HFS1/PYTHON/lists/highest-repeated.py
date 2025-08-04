# highest occuring element's count
# m-1

l=list(map(int,input().split()))
m=[]
maxc=0
for i in set(l):
    c=l.count(i)
    if c>maxc:
        maxc =c
        m.clear()
        m.append(i)
    elif c==maxc:
        m.append(i)
print(*m) 

# m-2

l=list(map(int,input().split()))
e=l[0]
mc=1
for i in set(l):
    c=l.count(i)
    if c>mc:
        mc=c
        e=i
print(e)

# m-3 (not working if tmore than one  elements are repeated more no of times)

l=list(map(int,input().split()))
co=[]
for i in l:
    c=0
    for j in l:
        if j==i:
            c+=1
    co.append(c)
print(co)
max_val=max(co)
for i in range(len(co)):
    if co[i]==max_val:
        print(l[i],end=" ")
        break
