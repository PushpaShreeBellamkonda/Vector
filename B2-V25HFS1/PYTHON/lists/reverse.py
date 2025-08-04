# reverse the list
# m-1

l=list(map(int,input().split()))
for i in range(len(l)):
    x=l.pop()
    l.insert(i,x)
print(l)

# m-2

l=list(map(int,input().split()))
i=0
j=len(l)-1
while i<j:
    l[i],l[j]=l[j],l[i]
    i+=1
    j-=1
print(l)