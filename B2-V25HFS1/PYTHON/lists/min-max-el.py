l=list(map(int,input().split()))
min=max=l[0]
for i in l:
    if i<min:
        min=i
    elif i>max:
        max=i
print(min,max)