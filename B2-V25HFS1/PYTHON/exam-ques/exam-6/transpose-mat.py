# transpose a matrix
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
l2=[]
for i in range(n):
    l1=[]
    for j in range(n):
            l1.append(l[j][i])
    l2.append(l1)
print(l2)