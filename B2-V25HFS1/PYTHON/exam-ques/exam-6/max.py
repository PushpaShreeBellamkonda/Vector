# find the maximum number in a nested list
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
m=l[0][0]
for i in range(n):
    for j in range(n):
        if l[i][j]>m:
            m=l[i][j]
print(m)

