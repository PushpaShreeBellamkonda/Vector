# to find even count
l=list(map(int,input().split()))
even=0
for i in l:
    if i%2==0:
        even+=1
print(even)

# seperate even and odd elements in diff lists

l=list(map(int,input().split()))
even=[]
odd=[]
for i in l:
    if i%2==0:
        even.append(i)
    elif i%2==1:
        odd.append(i)
print(even)
print(odd)
