r=int(input())
c=int(input())
a=[[int(input()) for j in range(c)] for i in range(r)]
t=[]
for j in range(c):
    x=[]
    for i in range(r):
        x.append(a[i][j])
    t.append(x)
print(t)
