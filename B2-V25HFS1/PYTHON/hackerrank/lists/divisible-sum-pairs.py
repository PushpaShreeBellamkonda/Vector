n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if (l[i]+l[j])%k==0:
            c+=1
print(c)
            