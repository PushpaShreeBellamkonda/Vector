n=int(input())
for _ in range(n):
    a=int(input())
    c=0
    t=a
    while t>0:
        d=t%10
        if d!=0 and a%d==0:
            c+=1
        t=t//10
    print(c)
