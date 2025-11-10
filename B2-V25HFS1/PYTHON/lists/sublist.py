# sublist finding
l=list(map(int,input().split()))
for i in range(len(l),0,-1):
    for j in range(len(l)-i+1):
        print(l[j:j+i] , end="\n")



# k length sublist
l=list(map(int,input().split()))
i=int(input())
for j in range(len(l)-i+1):
    print(l[j:j+i])


# klength sublist with max sum
l=[3,4,7,4]
i=3
f=[]
for j in range(len(l)-i+1):
    x=l[j:j+i]
    s=0
    for m in x:
        s+=m
        f.append(s)
print(max(f))


# sliding window technique
li=[3,4,7,9,5,2]
n=len(li)
l=0
ans=0
temp=0
k=3
for r in range(n):
    temp+=li[r]

    if (r-l==k):
        temp-=li[l]
        l+=1
    
    if (r-l+1==k):
        ans=max(ans,temp)
print(ans)


