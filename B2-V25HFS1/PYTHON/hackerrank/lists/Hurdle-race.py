n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in l:
    m=max(l)
if k<m:
    print(m-k)
else:
    print(0)