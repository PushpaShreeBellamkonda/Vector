l=list(map(int,input().split()))
for i in range(len(l)-1):
    t=i
    for j in range(i+1,len(l)):
        if l[j]<l[i]:
            t=j
    l[i],l[j]=l[j],l[i]
print(l)