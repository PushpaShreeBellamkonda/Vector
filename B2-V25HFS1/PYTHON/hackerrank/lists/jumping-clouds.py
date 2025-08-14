n=int(input())
l=list(map(int,input().split()))
i=0
c=0
while i<n-1:
    if (i+2)<n and l[i+2]==0:
        i+=2 
    else:
        i+=1
    c+=1
print(c)
    