# Count how many possible pairs are there in a given list , such that sum of pair should be divisible by k

l=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        print(l[i],l[j])
        if (l[i]+l[j])%k==0:
            c+=1
print(c)