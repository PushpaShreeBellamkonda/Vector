# find max element from each row and column in a n*4 matrix
r=int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
x=0
y=0
for j in range(4):
    min=max=l[0][j]
    for i in range(r):
        if l[i][j]<min:
            min=l[i][j]
        if l[i][j]>max:
            max=l[i][j]
    x=x*10+max
    y=y*10+min
print(x)
print(y)
