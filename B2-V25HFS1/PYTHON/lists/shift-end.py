# shift all zeroes to end of list
# m-1

l=list(map(int,input().split()))
i=0
for j in range(len(l)):
    if l[j]!=0:
        l.insert(i,l.pop(j))
        i+=1
print(l)

# m-2

l=list(map(int,input().split()))
c=l.count(0)
while 0 in l:
    l.remove(0)
for i in range(c):
    l.append(0)
print(l)

