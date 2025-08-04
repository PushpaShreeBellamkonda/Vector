n=int(input())
l=list(map(int,input().split()))
min=max=l[0]
minc=0
maxc=0
for i in l:
    if i > max:
        max=i
        maxc+=1
    elif i < min:
        min=i
        minc+=1
print(maxc,minc)
    