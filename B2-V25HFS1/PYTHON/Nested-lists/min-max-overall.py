r=int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
min=max=l[0][0]
for i in l:
    for j in i:
        if j>max:
            max=j
        elif j<min:
            min=j
print(min,max)