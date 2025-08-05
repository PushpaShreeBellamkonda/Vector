n=int(input())
l=list(map(int,input().split()))
l1=[]
d,m=map(int,input().split())
for i in range(len(l),0,-1):
    for j in range(len(l)-i+1):
        sl=l[j:j+i]
        l1.append(sl)
c=0
for i in l1:
    if len(i)==m and sum(i)==d:
        c+=1
print(c)