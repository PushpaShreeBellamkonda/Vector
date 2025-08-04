# sort 1st k elements in ascending order and remaining in descending order
l=list(map(int,input().split()))
k=int(input())
for i in range(k+1):
    for j in range(i+1,len(l)):
        if l[j]<l[i]:
            l[i],l[j]=l[j],l[i]
for i in range(k,len(l)-1):
    for j in range(i+1,len(l)):
        if l[j]>l[i]:
            l[i],l[j]=l[j],l[i]
print(l)