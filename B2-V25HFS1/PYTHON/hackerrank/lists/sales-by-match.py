n=int(input())
l=list(map(int,input().split()))
mc=0
for i in set(l):
    c=l.count(i)
    mc+=c//2
print(mc)
    