# find minimum value in every row and every column in a n*4 matrix 
r=int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
x=0
y=0
for i in range(r):
    min=max=l[i][0]
    for j in range(4):
        if l[i][j]<min:
            min=l[i][j]
        if l[i][j]>max:
            max=l[i][j]
    x=x*10+min
    y=y*10+max
print(x)
print(y)