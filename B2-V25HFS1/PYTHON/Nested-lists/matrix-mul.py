r1=int(input())
c1=int(input())
r2=int(input())
c2=int(input())
if c1==r2:
    a=[[int(input()) for j in range(c1)] for i in range(r1)]
    b=[[int(input()) for j in range(c2)] for i in range(r2)]
    c=[]
    for i in range(r1):
        x=[]
        for j in range(c2):
            s=0
            for k in range(c1):
                s=s+a[i][k]*b[k][j]
            x.append(s)
        c.append(x)
    print(c)
else:
    print("Multiplication not possible")

# m-2
r1=int(input())
c1=int(input())
r2=int(input())
c2=int(input())
if c1==r2:
    a=[[int(input()) for j in range(c1)] for i in range(r1)]
    b=[[int(input()) for j in range(c2)] for i in range(r2)]
    c=[[[0]*c2 for i in range(c1)]]
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                c[i][j]+=a[i][k]*b[k][j]
else:
    print("Multiplication not possible")