n=int(input())
l=list(map(int,input().split()))
f=[]
if min(l)==max(l):
    print(n)
else:
    for i in range(min(l),max(l)):
        c=l.count(i)+l.count(i+1)
        f.append(c)
    print(max(f))
    

