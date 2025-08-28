# row with max sum
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
r=l[0]
t=0
for i in l:
    s=sum(i)
    if s>t:
        s=t
        r=i
print(r)