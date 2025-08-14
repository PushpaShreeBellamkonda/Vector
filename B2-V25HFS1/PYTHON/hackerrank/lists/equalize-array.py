n=int(input())
l=list(map(int,input().split()))
d={}
for i in l:
    d[i]=d.get(i,0)+1

m= max(d.values())
deletions=n-m
print(deletions)
    


