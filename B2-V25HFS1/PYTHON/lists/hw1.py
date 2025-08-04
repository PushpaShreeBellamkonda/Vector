# arrange even index elements in increasing order and odd index elements in decreasing order
#  in a given sorted list

# m-1

l=list(map(int,input().split()))
i=1
while i<len(l)-1:
    l.insert(i,l.pop())
    i=i+2
print(l)

# m-2

l=list(map(int,input().split()))
for i in range(len(l)):
    if i%2==0:
        pass
    else:
        l.insert(i,l.pop())
print(l)

# m-3

l=list(map(int,input().split()))
e=[]
o=[]
for i in range(len(l)):
    if i%2==0:
        e.append(l[i])
    elif i%2==1:
        o.append(l[i])
e.sort()
o.sort(reverse=True)

# if l is even length
# l2=[]
# for i in range(len(e)):
#     l2.append(e[i])
#     l2.append(o[i])
# print(l2)

# if l is odd or even length
l2=[]
le=len(e)
lo=len(o)
for i in range(max(le,lo)):
    if i<le:
        l2.append(e[i])
    if i < lo:
        l2.append(o[i])
print(l2)


