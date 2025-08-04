# delete duplicate elements in the list

# m-1 (doesnt maintain insertion order)

l=list(map(int,input().split()))
print(list(set(l)))

# m-2 (maintains insertion order but we have to use anoother list)

l=list(map(int,input().split()))
r=[]
for i in l:
    if i not in r:
        r.append(i)
print(r)

# m-3  (effecient one)

l=list(map(int,input().split()))
i=0
while i<len(l)-1:
    j=i+1
    while j<len(l):
        if l[i]==l[j]:
            del l[j]
        else:
            j+=1
    i+=1
print(l)