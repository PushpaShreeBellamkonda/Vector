i,j,k=map(int,input().split())
c=0
for x in range(i,j+1):
    r=0
    t=x
    while t!=0:
        d=t%10
        r=r*10+d
        t=t//10
    f=(x-r)/k
    if f.is_integer():
        c+=1
print(c)