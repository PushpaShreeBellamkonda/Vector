n=int(input())
l=[]
for _ in range(n):
    l.append(list(map(int,input().split())))
print(l)
c1=0
c2=0
for i in range(n):
    for j in range(n):
        if i==j:
            c1+=l[i][j]
        if i+j==n-1:
            c2+=l[i][j]
d=abs(c1-c2)
print(d)

