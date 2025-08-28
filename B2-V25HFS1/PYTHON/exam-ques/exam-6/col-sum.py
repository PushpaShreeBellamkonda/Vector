# display col wise sum
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    s=0
    for j in range(n):
        s=s+l[i][j]
    print(s)