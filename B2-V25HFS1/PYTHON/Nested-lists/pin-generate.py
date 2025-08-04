r=int(input())
l=[]
for i in range(r):
    l.append(list(map(int,input().split())))
pin=0
min=l[0][0] #overall minimum
for j in range(4):
    min=max=l[0][j]
    for i in range(r):
        if l[i][j]<min:
            min=l[i][j]
        if l[i][j]>max:
            max=l[i][j]
    pin=pin*10+max
pin=pin*10+min
print(pin)
