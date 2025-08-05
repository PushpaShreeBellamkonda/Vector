n=int(input())
l=list(map(int,input().split()))
e=l[0]
mc=1
for i in set(l):
    c=l.count(i)
    if c>mc:
        mc=c
        e=i
print(e)
